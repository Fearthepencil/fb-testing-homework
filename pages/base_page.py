class BasePage:

    def __init__(self, page, test_config: dict):
        self.page = page
        self.test_config = test_config
        self.base_url = test_config["urls"]["base_url"]

    def goto(self, url: str):
        self.page.goto(f"{self.base_url}{url}", wait_until="networkidle")

    def take_screenshot(self, filename: str):
        self.page.screenshot(path=f"screenshots/{filename}.png", full_page=True)

    def wait_for_page_load(self, timeout: int = 5000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)
