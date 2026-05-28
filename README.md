Architecture-focused QA automation using local LLM augmentation.

End-to-end test automation built with Playwright + Python, enhanced with a local LLM workflow (Ollama + DeepSeek) to support test development and maintainability.

This project demonstrates a clean QA automation setup focused on:

Maintainable test structure

Reusable helpers

Evidence-driven execution (videos & screenshots)

Local AI-assisted testing workflows

🧠 Tech Stack

🧪 Playwright (Python)

🐍 Python

🤖 Ollama (Local LLM Runtime)

💡 DeepSeek Coder

🎥 Video & Screenshot Evidence

🧱 Modular Test Helpers

📂 Project Structure
opencart-tests/
├── tests/
│   ├── helpers.py
│   ├── test_opencart.py
│   ├── test_search.py
│   ├── test_add_user.py
│   └── test_logout.py
├── test-results/
└── README.md
⚙️ Setup
1️⃣ Clone repository
git clone https://github.com/DarielZA/ai-assisted-playwright-e2e-tests.git
cd ai-assisted-playwright-e2e-tests
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install playwright pytest
playwright install chromium
▶️ Run Tests
python -m pytest tests/ -v

Execution generates:

🎥 Video recordings

🖼 Screenshots

Console logs

All stored inside:

test-results/
🤖 Local AI Workflow (Ollama + DeepSeek)

This project integrates a local coding model to assist with test generation and refactoring.

Run locally:

ollama run deepseek-coder:6.7b

Example usage:

optimize this playwright python test for maintainability
🎯 Purpose

This repository showcases how QA automation can evolve with local AI assistance, combining:

Traditional test automation practices

Reusable architecture

Offline LLM-powered development workflows

👨‍💻 Author

Dariel Aguilar
QA Automation Engineer
