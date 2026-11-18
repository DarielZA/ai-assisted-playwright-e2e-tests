# AI-Assisted Playwright E2E Tests

Architecture-focused QA automation using local LLM augmentation.

End-to-end test automation built with **Playwright + Python**, enhanced with a local LLM workflow (**Ollama + DeepSeek**) to support test development and maintainability.

This project demonstrates a clean QA automation setup focused on:

- Maintainable test structure
- Reusable helpers
- Evidence-driven execution (videos & screenshots)
- Local AI-assisted testing workflows

---

## Tech Stack

- **Playwright (Python)**
- **Python**
- **Ollama** (local LLM runtime)
- **DeepSeek Coder**
- Video & screenshot evidence
- Modular test helpers

---

## Project Structure

```
opencart-tests/
├── tests/
│   ├── helpers.py
│   ├── test_opencart.py
│   ├── test_search.py
│   ├── test_add_user.py
│   └── test_logout.py
├── test-results/
└── README.md
```

---

## Setup

1. Clone the repository
```bash
git clone https://github.com/DarielZA/ai-assisted-playwright-e2e-tests.git
cd ai-assisted-playwright-e2e-tests
```

2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install playwright pytest
playwright install chromium
```

---

## Run Tests

```bash
python -m pytest tests/ -v
```

Execution generates:

- Video recordings
- Screenshots
- Console logs

All stored inside `test-results/`.

---

## Local AI Workflow (Ollama + DeepSeek)

This project integrates a local coding model to assist with test generation and refactoring.

Run locally:

```bash
ollama run deepseek-coder:6.7b
```

Example usage:

```
optimize this playwright python test for maintainability
```

---

## Purpose

This repository showcases how QA automation can evolve with local AI assistance, combining:

- Traditional test automation practices
- Reusable architecture
- Offline LLM-powered development workflows

---

## Author

**Dariel Aguilar** - QA Engineer
