# Playwright Pytest Automation Framework

A scalable UI automation framework built using:

- Python
- Pytest
- Playwright
- Allure Reporting

---

# Framework Features

- Playwright browser automation
- Pytest execution framework
- Page Object Model (POM)
- Allure reporting
- CSV driven test data
- Parallel execution support
- Cross-browser execution
- Reusable BasePage methods
- Chained page methods

---

# Project Structure

```text
project/
│
├── pages/
├── tests/
├── utils/
├── data/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <your_repo_url>
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Playwright Browsers

```bash
playwright install
```

---

# Run Tests

## Chromium

```bash
pytest --browser chromium
```

## Firefox

```bash
pytest --browser firefox
```

## Webkit (Safari)

```bash
pytest --browser webkit
```

## Headed Mode

```bash
pytest --browser chromium --headed
```

---

# Run Allure Report

## Generate Results

```bash
pytest --alluredir=allure-results
```

## Open Report

```bash
allure serve allure-results
```

---

# Parallel Execution

```bash
pytest -n 4
```

---

# Tech Stack

- Python
- Pytest
- Playwright
- Allure
- Pandas
- Faker

---

# Future Enhancements

- API automation integration
- Docker support
- GitHub Actions CI/CD
- Playwright tracing
- Automatic screenshot capture
- Environment management using .env

---

# Author

Akshay