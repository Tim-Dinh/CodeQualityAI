# utils.py
import json
import json5
import re

def clean_json_response(response_text):
    """
    Cleans and repairs JSON responses:
    1. Removes Markdown formatting (```json ... ```)
    2. Fixes broken JSON fields
    3. Uses json5 for flexible parsing
    """
    response_text = response_text.strip()

    # Remove Markdown formatting
    response_text = re.sub(r"^```json\s*", "", response_text)
    response_text = re.sub(r"\s*```$", "", response_text)

    # Remove non-JSON content before `{` and after `}`
    response_text = re.sub(r'^[^{]+', '', response_text)
    response_text = re.sub(r'[^}]+$', '}', response_text)

    # Fix broken lines in JSON
    response_text = re.sub(r'(?<![:,\[{])\n\s*(?!"score")', ' ', response_text)

    # Attempt to parse JSON
    try:
        return json.dumps(json.loads(response_text), indent=4)
    except json.JSONDecodeError:
        try:
            return json.dumps(json5.loads(response_text), indent=4)
        except json.JSONDecodeError:
            return "{}"
