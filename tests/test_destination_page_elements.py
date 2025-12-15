from pages.destination_page import DestinationPage
from pages.sitemap_page import SitemapPage

def test_destination_page_elements(page, test_config: dict):
    
    sitemap_page = SitemapPage(page, test_config)
    sitemap_page.navigate_to_sitemap()
    sitemap_page.click_first_destination()

    destination_page = DestinationPage(page, test_config)
    destination_page.wait_for_charter_cards()
    destination_page.wait_for_page_load()

    cards_count = destination_page.get_charter_cards().count()
    assert cards_count >= destination_page.min_charter_cards, (
        f"Expected at least {destination_page.min_charter_cards} "
        f"charter cards, but found {cards_count}"
    )

    first_charter_card = destination_page.get_first_charter_card()
    charter_name = destination_page.get_charter_name(first_charter_card)
    assert charter_name, "Charter name is not present"
    
    boat_length = destination_page.get_boat_length(first_charter_card)
    assert boat_length > 0, "Boat length is not valid"
    
    max_people = destination_page.get_max_people(first_charter_card)
    assert max_people.lower().endswith("people"), "Max people text format is invalid"

    price = destination_page.get_price(first_charter_card)
    assert isinstance(price, (int, float)), "Price is not a number"
    assert price > 0, "Price is not valid"

    tooltip_text = destination_page.hover_wishlist_icon(first_charter_card)
    assert destination_page.expected_tooltip_text in tooltip_text, "Wishlist tooltip is not valid"

    see_availability_button = destination_page.get_see_availability_button(first_charter_card)
    assert see_availability_button.is_visible(), "See availability button is not visible"
    assert see_availability_button.is_enabled(), "See availability button is not clickable"
