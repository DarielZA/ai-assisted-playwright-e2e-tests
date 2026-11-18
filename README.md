# AI-Assisted Playwright E2E Tests

End-to-end UI tests in Python with Playwright, written with help from a local LLM (Ollama + DeepSeek Coder). The tests run against the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/).

## What's included

- Login, user search, add user and logout tests in `tests/`
- A shared helper (`tests/helpers.py`) that opens the browser and saves a video recording and a screenshot of each run in `test-results/`

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

## Run the tests

```bash
python -m pytest tests/ -v
```

## Local AI workflow

The local model runs with:

```bash
ollama run deepseek-coder:6.7b
```

Example prompt: `optimize this playwright python test for maintainability`

---

## Author

**Dariel Aguilar** - QA Engineer
