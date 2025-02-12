# 🚀 Code Quality AI Analyzer

**Code Quality AI Analyzer** is an automated tool that uses AI to analyze C++ and header files for **duplication, complexity, coupling, and coding standards**. The tool scans, evaluates, and provides actionable insights into code quality.

---

## 📌 Features
✅ **AI-Powered Code Analysis** – Uses LLMs like DeepSeek-Coder and Qwen to evaluate code quality.  
✅ **Automatic File Selection** – Smart sampling based on file size and probability rules.  
✅ **Parallel Processing** – Multi-threaded analysis for performance optimization.  
✅ **JSON Cleanup & Validation** – Ensures AI responses are structured correctly.  
✅ **Excel Export** – Saves the results in an easy-to-use Excel file.  
✅ **Modular & Extensible** – Clean architecture with separate modules for maintainability.  
✅ **Unit-Tested** – Comprehensive tests for robustness.  

---

## 📁 Project Structure
```plaintext
/code-analysis/
│── main.py                 # Entry point for execution
│── config.py               # Configuration settings
│── utils.py                # Utility functions (JSON cleanup, validation)
│── analyzer.py             # AI-based code analysis
│── file_selector.py        # Handles file selection based on criteria
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│── tests/                  # Unit tests
│   ├── test_utils.py       # Tests for utils.py
│   ├── test_analyzer.py    # Tests for analyzer.py
│── .gitignore              # Git ignored files
│── code_analysis.xlsx      # (Generated) Analysis results file
```

---

## 🔧 Installation & Setup

### **1️⃣ Prerequisites**
- **Python 3.8+**
- **pip (Python package manager)**
- **Ollama** (For LLM-based code analysis)

## 📊 How It Works

- The script scans the workspace master directory for .cpp and .h files.
- It filters files based on size and selection probability.
- It sends the code to an LLM for analysis.
- The AI returns structured feedback (JSON format).
- The cleaned and formatted data is saved in an Excel report.

## 🔗 License

EUPL License – Feel free to use and modify.

## 🌟 Contributing

Want to improve this tool? Fork the repo and submit a pull request! 🚀