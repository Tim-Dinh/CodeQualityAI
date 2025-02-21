import os
import random
from config import DIRECTORY_PATH, ALLOWED_EXTENSIONS, SELECTION_PROBABILITIES

def get_selected_files():
    """Selects files based on defined criteria."""
    selected_files = []

    for root, _, files in os.walk(DIRECTORY_PATH):
        for filename in files:
            if not any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                continue

            file_path = os.path.join(root, filename)

            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                char_count = len(content)

            # Apply selection rules
            if char_count < 500:
                continue
            elif 500 <= char_count < 1000 and random.random() > SELECTION_PROBABILITIES["500-1000"]:
                continue
            elif 1000 <= char_count < 5000 and random.random() > SELECTION_PROBABILITIES["1000-5000"]:
                continue
            elif char_count >= 5000 and random.random() > SELECTION_PROBABILITIES["5000+"]:
                continue

            selected_files.append(file_path)

    return selected_files
