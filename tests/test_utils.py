import sys
import os
import pytest
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import clean_json_response

def test_clean_json_valid():
    """Test that a valid JSON response remains unchanged."""
    json_input = '{"Duplication": {"summary": "No duplication", "advice": "Good job", "score": 5}}'
    assert clean_json_response(json_input) == json.dumps(json.loads(json_input), indent=4)

def test_clean_json_markdown():
    """Test that JSON wrapped in markdown is correctly cleaned."""
    json_input = """```json
    {
        "Duplication": {"summary": "No duplication", "advice": "Good job", "score": 5}
    }
    ```"""
    expected_output = json.dumps({"Duplication": {"summary": "No duplication", "advice": "Good job", "score": 5}}, indent=4)
    assert clean_json_response(json_input) == expected_output

def test_clean_json_invalid():
    """Test that an invalid JSON returns an empty JSON string."""
    json_input = '{"Duplication": {"summary": "No duplication", "advice": "Good job", "score": 5'  # Missing closing brace
    assert clean_json_response(json_input) == "{}"

def test_clean_json_extra_text():
    """Test that extra text before or after JSON is removed."""
    json_input = "Some random text before {\"Duplication\": {\"summary\": \"No duplication\", \"advice\": \"Good job\", \"score\": 5}} and some text after"
    expected_output = json.dumps({"Duplication": {"summary": "No duplication", "advice": "Good job", "score": 5}}, indent=4)
    assert clean_json_response(json_input) == expected_output

if __name__ == "__main__":
    pytest.main()
