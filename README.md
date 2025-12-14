# FishingBooker QA Homework

## Overview
Automated and manual test suite for FishingBooker's fish page and destination page functionality, completed as part of a QA Engineer take-home assignment.

**Author:** Pavle Stefanovic  
**Date:** January 2025

---

## 📋 Project Structure

```
fb-testing-homework/
├── docs/                      # HTML documentation deliverables
│   ├── index.html            # Main landing page
│   ├── test-plan.html        # Test strategy and approach (ISTQB)
│   ├── test-cases.html       # 13 test cases (BDD format)
│   ├── bug-report.html       # 8 defects with screenshots
│   ├── test-execution-report.html  # Test results summary
│   ├── bug_data/             # Bug evidence screenshots
│   └── style.css             # Documentation styles
├── tests/                     # Automated test suite
│   ├── conftest.py           # Pytest fixtures
│   └── test_Basic.py         # Basic navigation test
├── pages/                     # Page Object Model
│   ├── __init__.py
│   └── base_page.py
├── test_data/                 # Test data files
│   └── test_config.json
├── screenshots/               # Test screenshots
├── requirements.txt           # Python dependencies
├── pytest.ini                # Pytest configuration
└── README.md                 # This file
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Installation

1. **Navigate to project directory**
   ```bash
   cd fb-testing-homework
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

---

## 🧪 Running Tests

### Run All Automated Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_Basic.py -v
```

### Run with Screenshots
```bash
pytest tests/ -v -s
```

### Generate HTML Report
```bash
pytest tests/ -v --html=test-report.html --self-contained-html
```

---

## 📚 Documentation

Open `docs/index.html` in your browser to access all deliverables:
- Test Plan (ISTQB format)
- Test Cases (BDD Given-When-Then)
- Bug Reports (with screenshots)
- Test Execution Report

---

## 🏗️ Architecture

### Page Object Model (POM)
- **BasePage:** Common functionality (navigation, screenshots)

### Test Organization
- **Fixtures:** Browser and page setup in `conftest.py`
- **Test Data:** Centralized in `test_data/test_config.json`

---

## 🔧 Troubleshooting

### Playwright browser not found
```bash
playwright install chromium
```

### Tests timeout
- Check internet connection
- FishingBooker may have rate limiting - tests include waits
- Increase timeout values in page objects if needed

### Locator issues
- FishingBooker's HTML structure may change
- Update selectors in `pages/` directory
- Use browser DevTools to inspect elements

### Login issues
- Verify credentials are correct: `fishingbooker` / `QAFBTest`
- Check if login page structure has changed
- Update selectors in `pages/login_page.py` if needed

---

## 📝 Notes

- Tests run against live FishingBooker testing environment
- Some tests may be flaky due to dynamic content
- Screenshots saved to `screenshots/` directory
- Selectors use multiple fallback options for resilience

---

## 📄 License

Created for educational and assessment purposes only.
