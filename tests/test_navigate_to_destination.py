from pages.sitemap_page import SitemapPage
from pages.destination_page import DestinationPage


def test_navigate_to_destination(page, test_config: dict):
    sitemap_page = SitemapPage(page, test_config)
    sitemap_page.navigate_to_sitemap()
    assert page.url.endswith(
        test_config["urls"]["sitemap_url"]
    ), "Sitemap page did not load"

    assert page.locator(
        sitemap_page.TOP_DESTINATIONS_SECTION_SELECTOR
    ).is_visible(), "Top Fishing Destinations section is not visible"

    first_destination = page.locator(sitemap_page.FIRST_DESTINATION_LINK_SELECTOR).first

    assert first_destination.is_visible(), "First destination link is not visible"
    assert first_destination.is_enabled(), "First destination link is not clickable"

    sitemap_page.click_first_destination()

    destination_page = DestinationPage(page, test_config)
    destination_page.wait_for_page_load()

    assert (
        test_config["urls"]["destination_url"] in page.url
    ), "Destination page did not load"
