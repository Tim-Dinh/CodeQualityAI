import pytest
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch
from analyzer import analyze_file

# Sample JSON response for testing
MOCK_JSON_RESPONSE = {
    "Duplication": {"summary": "No duplication detected", "advice": "Keep it up", "score": 5},
    "Unit Size": {"summary": "Small functions", "advice": "Maintainable", "score": 4},
    "Complexity": {"summary": "Low complexity", "advice": "Good structure", "score": 5},
    "Unit Interfacing": {"summary": "Well interfaced", "advice": "Minimal coupling", "score": 4},
    "Coupling": {"summary": "Loose coupling", "advice": "Excellent design", "score": 5},
    "Coding Standards": {"summary": "Follows standards", "advice": "Keep it up", "score": 5}
}

MOCK_JSON_TEXT = json.dumps(MOCK_JSON_RESPONSE, indent=4)

@pytest.fixture
def mock_file(tmp_path):
    """Create a temporary C++ file for testing."""
    file_path = tmp_path / "test.cpp"
    file_path.write_text("int main() { return 0; }")  # Minimal valid C++ code
    return str(file_path)

@patch("ollama.chat")
def test_analyze_file(mock_ollama, mock_file):
    """Test analyzing a file with a mocked AI response."""
    mock_ollama.return_value = {"message": {"content": MOCK_JSON_TEXT}}

    result = analyze_file(mock_file)

    assert result[0] == mock_file  # Ensure filename is correctly stored
    assert result[1] == "No duplication detected"
    assert result[2] == "Keep it up"
    assert result[3] == 5  # Duplication score
    assert len(result) == 19  # Ensure full category coverage

@patch("ollama.chat")
def test_analyze_file_invalid_json(mock_ollama, mock_file):
    """Test behavior when AI returns invalid JSON."""
    mock_ollama.return_value = {"message": {"content": "invalid response"}}

    result = analyze_file(mock_file)

    assert result[0] == mock_file  # Ensure filename is correctly stored
    assert "Error" in result[1:]  # Ensure all fields return "Error"

if __name__ == "__main__":
    pytest.main()
