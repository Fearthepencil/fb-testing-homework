import os
import json
import pytest
from playwright.sync_api import sync_playwright, Browser, Page


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def test_config():
    # Load test configuration (URLs, credentials, timeouts).
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "test_data",
        "test_config.json",
    )
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def page(browser: Browser, test_config) -> Page:
    # Basic Auth is handled at context level so that as soon as the page loads,
    # credentials are automatically sent and the Basic Auth prompt is bypassed.
    context = browser.new_context(
        http_credentials={
            "username": test_config["login"]["username"],
            "password": test_config["login"]["password"],
        },
    )
    page = context.new_page()

    yield page

    context.close()
