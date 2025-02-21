import os
import json
import ollama
from config import SELECTED_MODEL, CUTOFF, SCRIPT_DIR
from utils import clean_json_response

EVALUATION_PROMPT = """Analyze the following code and return a structured JSON response.  
Ensure the JSON  follows this  format:

{
    "Duplication": {
        "summary": "humanlike evaluation/analysis of code duplication, including possible examples (max 3)",
        "advice": "humanlike advice to get higher score",
        "score": score between 1-5 1 is low quality 5 is high quality
    },
   and the same for "Unit Size", "Complexity", "Unit Interfacing", "Coupling" and "Coding Standards" where you evaluate style standards, general vulnaribilities.
}

Do NOT include extra text before or after the JSON and make sure your entire response is JSON parsable.
The json must be correct, check it again and repair if its not.
### Code to Analyze:
"""

def analyze_file(file_path):
    """Analyze a single file using the AI model."""
    filename = os.path.basename(file_path)
    print(f"Processing {filename}...")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        file_content = file.read()[:CUTOFF]

    full_prompt = f"{EVALUATION_PROMPT}\n\n{file_content}"

    response = ollama.chat(
        model=SELECTED_MODEL,
        messages=[{"role": "user", "content": full_prompt}],
        options={"num_ctx": 8192}
    )

    result_text = response["message"]["content"].strip()

    try:
        cleaned_text = clean_json_response(result_text)
        json_data = json.loads(cleaned_text)

        row = [file_path]  # Start row with filename

        # Ensure all categories exist in the JSON response
        categories = ["Duplication", "Unit Size", "Complexity", "Unit Interfacing", "Coupling", "Coding Standards"]
        
        for category in categories:
            category_data = json_data.get(category, {})  # Get category data, or empty dict if missing
            row.append(category_data.get("summary", ""))  # Add summary or empty string
            row.append(category_data.get("advice", ""))  # Add advice or empty string
            row.append(category_data.get("score", ""))  # Add score or empty string

        return row

    except json.JSONDecodeError:
        print(f"⚠️ JSON parsing failed for {filename}. Response:\n{result_text}")
        return [filename] + ["Error"] * 18  # Return an error row with placeholders
