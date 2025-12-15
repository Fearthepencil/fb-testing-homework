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
│   ├── test-cases.html       # 17 test cases (13 manual + 4 automated, BDD format)
│   ├── bug-report.html       # 8 defects with screenshots
│   ├── test-execution-report.html  # Test results summary
│   ├── bug_data/             # Bug evidence screenshots
│   └── style.css             # Documentation styles
├── tests/                     # Automated test suite
│   ├── conftest.py           # Pytest fixtures (browser, page, destination_page)
│   ├── test_navigate_to_destination.py  # Navigation test (TC-014)
│   ├── test_destination_page_elements.py  # Element validation (TC-015)
│   └── test_sorting.py       # Price sorting tests (TC-016, TC-017)
├── pages/                     # Page Object Model
│   ├── __init__.py
│   ├── base_page.py          # Base page class
│   ├── sitemap_page.py       # Sitemap page object
│   └── destination_page.py   # Destination page object
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── parser_functions.py   # Price and length parsing utilities
├── test_data/                 # Test data files
│   └── test_config.json      # Configuration (URLs, credentials, timeouts)
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
pytest tests/test_navigate_to_destination.py -v
pytest tests/test_destination_page_elements.py -v
pytest tests/test_sorting.py -v
```

### Run with Screenshots
```bash
pytest tests/ -v -s
```

### Generate HTML Report
```bash
pytest tests/ -v --html=test-report.html --self-contained-html
```

### Run with Pylint
```bash
pylint tests/ --max-line-length=120 --disable=C0114,C0115,C0116,W0621
```

---

## 📚 Documentation

Open `docs/index.html` in your browser to access all deliverables:
- **Test Plan** - Test strategy, scope, and approach (ISTQB format)
- **Test Cases** - 17 test cases in BDD format (13 manual + 4 automated)
- **Bug Reports** - 8 documented defects with screenshots
- **Test Execution Report** - Test results summary with pass/fail rates

---

## 🏗️ Architecture

### Page Object Model (POM)
- **BasePage:** Common functionality (navigation, screenshots, page load waits)
- **SitemapPage:** Sitemap page interactions (navigation, destination selection)
- **DestinationPage:** Destination page interactions (charter cards, sorting, validation)

### Test Organization
- **Fixtures:** 
  - `browser` - Session-scoped browser instance
  - `test_config` - Session-scoped configuration loader
  - `page` - Function-scoped Playwright page with HTTP Basic Auth
  - `destination_page` - Function-scoped fixture that navigates to destination page
- **Test Data:** Centralized in `test_data/test_config.json`
- **Utilities:** Price and length parsing functions in `utils/parser_functions.py`

### Design Patterns
- **Page Object Model** - Encapsulates page interactions
- **Fixture-based Setup** - Reusable test fixtures for common setup
- **DRY Principle** - Shared navigation logic in `destination_page` fixture

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

### Authentication issues
- HTTP Basic Auth is handled automatically via `conftest.py`
- Verify credentials in `test_data/test_config.json`: `fishingbooker` / `QAFBTest`
- If authentication fails, check if the test environment URL or credentials have changed

---

## 📝 Notes

- Tests run against live FishingBooker testing environment: `https://nextjs15.dev.fishingbooker.com`
- HTTP Basic Auth is automatically handled via Playwright context
- Tests include explicit waits for network idle and DOM stability
- Screenshots saved to `screenshots/` directory (if configured)
- Selectors use `data-testid` attributes for reliability
- All automated tests (TC-014 to TC-017) are passing with 100% pass rate

---

## 📄 License

Created for educational and assessment purposes only.
