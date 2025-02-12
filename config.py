import os

# Define AI models
MODELS = {
    "fast": "qwen2.5-coder:1.5b",
    "balanced": "qwen2.5-coder:3b",
    "medium": "qwen2.5-coder:7b",
    "slow": "qwen2.5-coder:14b",
    "slowest": "deepseek-coder-v2:16b"
}

# Selected model
SELECTED_MODEL = MODELS["medium"]

# Allowed file extensions
ALLOWED_EXTENSIONS = [".cpp", ".h"]

# Sampling probabilities
SELECTION_PROBABILITIES = {
    "500-1000": 0.1,
    "1000-5000": 0.2,
    "5000+": 0.5
}

# Cutoff for file length
CUTOFF = 8000

# Define the working directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DIRECTORY_PATH = r"C:\Projects\test"

# ✅ Fix: Make sure NUM_WORKERS is properly assigned
NUM_WORKERS = min(4, os.cpu_count() or 1)  # Ensure at least 1 core is used
