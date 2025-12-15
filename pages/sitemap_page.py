from pages.base_page import BasePage


class SitemapPage(BasePage):

    TOP_DESTINATIONS_SECTION_SELECTOR = (
        "h1[class*='list-title']:has-text('Top Fishing Destinations')"
    )
    FIRST_DESTINATION_LINK_SELECTOR = "a:has-text('Fishing Charters in')"

    def __init__(self, page, test_config: dict):
        super().__init__(page, test_config)
        self.sitemap_url = test_config["urls"]["sitemap_url"]

    def navigate_to_sitemap(self):
        self.goto(self.sitemap_url)

    def wait_for_top_destinations_section(self, timeout: int = 5000):
        self.page.wait_for_selector(
            self.TOP_DESTINATIONS_SECTION_SELECTOR, timeout=timeout, state="visible"
        )
        self.page.wait_for_selector(
            self.FIRST_DESTINATION_LINK_SELECTOR, timeout=timeout, state="visible"
        )

    def click_first_destination(self):
        self.wait_for_top_destinations_section()

        first_link = self.page.locator(self.FIRST_DESTINATION_LINK_SELECTOR).first

        destination_url = first_link.get_attribute("href")

        first_link.click()

        self.page.wait_for_url(f"{destination_url}", timeout=10000)
