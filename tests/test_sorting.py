from pages.destination_page import DestinationPage
from pages.sitemap_page import SitemapPage
import pytest

@pytest.mark.parametrize(
    "sort_method, comparison_operator",
    [
        ("click_sort_price_lowest", lambda x, y: x <= y),
        ("click_sort_price_highest", lambda x, y: x >= y)
    ]
)
def test_sorting_price(page, test_config: dict, sort_method: str, comparison_operator: callable):
    sitemap_page = SitemapPage(page, test_config)
    sitemap_page.navigate_to_sitemap()
    sitemap_page.click_first_destination()

    destination_page = DestinationPage(page, test_config)
    destination_page.wait_for_charter_cards()

    getattr(destination_page, sort_method)()
    destination_page.wait_for_charter_cards()

    charter_cards = destination_page.get_charter_cards()
    prices = [
        destination_page.get_price(charter_cards.nth(i))
        for i in range(charter_cards.count())
    ]
    prices = [p for p in prices if p is not None and p > 0]
    for i in range(len(prices) - 1):
        assert comparison_operator(prices[i], prices[i + 1]), (
            f"Sorting failed for {sort_method} | Full list: {prices}"
        )
