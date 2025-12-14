# FishingBooker QA Homework - Automated Testing

## Overview
Automated UI test suite for FishingBooker destination page functionality, completed as part of a QA Engineer take-home assignment.

**Author:** [Your Name]  
**Date:** January 2025

---

## 📋 Project Structure

```
fishingbooker-testing/
├── pages/                     # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── sitemap_page.py
│   └── destination_page.py
├── tests/                     # Automated test suite
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures
│   └── test_destination_page.py
├── utils/                     # Utilities
│   ├── __init__.py
│   └── price_parser.py       # Price parsing and validation
├── test_data/                 # Test data files
│   └── test_config.json
├── screenshots/               # Test execution screenshots
├── requirements.txt           # Python dependencies
├── pytest.ini                # Pytest configuration
└── README.md                  # This file
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Installation

1. **Navigate to project directory**
   ```bash
   cd fishingbooker-testing
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
pytest tests/test_destination_page.py -v
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

## 📊 Test Coverage

### Automated Test
- ✅ **TC-DEST-001:** Destination page functionality test
  - Charter card elements validation
  - Price sorting (Lowest to Highest)
  - Price sorting (Highest to Lowest)

---

## 🏗️ Architecture

### Page Object Model (POM)
- **BasePage:** Common functionality (navigation, screenshots)
- **LoginPage:** Login functionality
- **SitemapPage:** Sitemap navigation and destination selection
- **DestinationPage:** Charter listing page interactions

### Test Organization
- **Fixtures:** Browser and page setup in `conftest.py`
- **Test Data:** Centralized in `test_data/test_config.json`
- **Utilities:** Price parsing and validation logic

---

## 🔧 Test Details

### Test Flow
1. Navigate to FishingBooker sitemap page
2. Select a destination from "Top Fishing Destinations"
3. Validate first charter card elements:
   - Charter name (link/text)
   - Boat length
   - Max number of people
   - Price ("Trips from ...")
   - Wishlist tooltip info
   - "See availability" button
4. Sort by Price (Lowest) and validate ascending order
5. Sort by Price (Highest) and validate descending order

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

- Tests run against live FishingBooker.com
- Some tests may be flaky due to dynamic content
- Screenshots saved to `screenshots/` directory
- Selectors use multiple fallback options for resilience

---

## 📄 License

Created for educational and assessment purposes only.

