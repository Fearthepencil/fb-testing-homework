from pages.base_page import BasePage
from utils.parser_functions import parse_price, parse_length


class DestinationPage(BasePage):
    CHARTER_CARD_SELECTOR = "[data-testid='single-charter-card-container']"
    CHARTER_NAME_SELECTOR = "[data-testid='charter-card-title']"
    BOAT_LENGTH_SELECTOR = (
        "[data-testid='charter-card-boat-silhouette'] p:has-text('ft')"
    )
    MAX_PEOPLE_SELECTOR = (
        "[data-testid='charter-card-boat-silhouette'] + p:has-text('people')"
    )
    PRICE_SELECTOR = "[data-testid='charter-card-trip-from-container']"
    WISHLIST_ICON_SELECTOR = "[data-testid='add-to-wishlist']"
    SEE_AVAILABILITY_BUTTON_SELECTOR = (
        "[data-testid='charter-card-see-availability-button']"
    )

    # Sort selectors
    SORT_PRICE_LOWEST_BUTTON_SELECTOR = "[data-testid='sort-price-lowest-button']"
    SORT_PRICE_HIGHEST_BUTTON_SELECTOR = "[data-testid='sort-price-highest-button']"

    def __init__(self, page, test_config: dict):
        super().__init__(page, test_config)
        self.min_charter_cards = test_config["test_requirements"]["min_charter_cards"]
        self.expected_tooltip_text = test_config["test_requirements"][
            "expected_tooltip_text"
        ]

    def wait_for_charter_cards(self, timeout: int = 10000):
        # Wait for at least minimum number of charter cards
        self.page.wait_for_selector(
            self.CHARTER_CARD_SELECTOR, timeout=timeout, state="visible"
        )
        # Wait for at least the minimum required number of cards
        cards = self.page.locator(self.CHARTER_CARD_SELECTOR)
        cards.nth(self.min_charter_cards - 1).wait_for(state="visible", timeout=timeout)

    def wait_for_page_load(self, timeout: int = 10000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)

    def get_charter_cards(self):
        return self.page.locator(self.CHARTER_CARD_SELECTOR)

    def get_first_charter_card(self):
        cards = self.get_charter_cards()
        if cards.count() == 0:
            raise AssertionError("No charter cards found on the page")
        return cards.first

    def get_charter_name(self, card_locator):
        name_element = card_locator.locator(self.CHARTER_NAME_SELECTOR).first
        return name_element.inner_text().strip()

    def get_boat_length(self, card_locator):
        # Look for boat length inside boat-silhouette container
        boat_container = card_locator.locator(
            "[data-testid='charter-card-boat-silhouette']"
        ).first
        boat_length_element = boat_container.locator("text=/\\d+\\s*ft/")
        text = boat_length_element.inner_text()

        # Extract pattern like "24 ft" or "26ft"
        return parse_length(text)

    def get_max_people(self, card_locator):

        # Look for "up to X people" or "X people" pattern inside boat silhouette container
        boat_container = card_locator.locator(
            "[data-testid='charter-card-boat-silhouette']"
        ).first
        # The max people is in a <p> tag inside the boat container
        people_text = boat_container.locator("p:has-text('people')").first
        return people_text.inner_text().strip()

    def get_price(self, card_locator):
        price_container = card_locator.locator(self.PRICE_SELECTOR).first
        # Get the full price text including "Trips from" and the amount
        price_text = price_container.inner_text().strip()

        return parse_price(price_text)

    def hover_wishlist_icon(self, card_locator):
        wishlist_icon = card_locator.locator(self.WISHLIST_ICON_SELECTOR).first
        wishlist_icon.hover()
        # Wait for tooltip to appear - look for text "Add listing to wishlist"
        tooltip = self.page.locator("text=Add listing to wishlist").first
        tooltip.wait_for(state="visible", timeout=2000)
        return tooltip.inner_text().strip()

    def get_see_availability_button(self, card_locator):
        return card_locator.locator(self.SEE_AVAILABILITY_BUTTON_SELECTOR).first

    def click_sort_price_lowest(self):
        self.page.locator(self.SORT_PRICE_LOWEST_BUTTON_SELECTOR).click()

    def click_sort_price_highest(self):
        self.page.locator(self.SORT_PRICE_HIGHEST_BUTTON_SELECTOR).click()
