import pytest
from playwright.sync_api import sync_playwright, BrowserContext, Page
import json
import os
import tempfile


@pytest.fixture(scope="session")
def browser_context():
    """Use persistent browser context with your Chrome profile"""
    with sync_playwright() as playwright:
        # Create a persistent context directory (stores cookies, session, etc.)
        user_data_dir = tempfile.mkdtemp()
        
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            viewport={"width": 1920, "height": 1080},
        )
        
        yield context
        
        context.close()


@pytest.fixture(scope="function")
def page(browser_context: BrowserContext) -> Page:
    # Get a new page from the persistent context
    page = browser_context.new_page()
    
    yield page
    
    # Don't close the page, just close it at the end
    page.close()


@pytest.fixture(scope="session")
def test_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_data", "test_config.json")
    with open(config_path, "r") as f:
        return json.load(f)
