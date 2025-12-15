import pytest


@pytest.mark.parametrize(
    "sort_method, comparison_operator",
    [
        ("click_sort_price_lowest", lambda x, y: x <= y),
        ("click_sort_price_highest", lambda x, y: x >= y),
    ],
)
def test_sorting_price(
    destination_page, sort_method: str, comparison_operator: callable
):

    getattr(destination_page, sort_method)()
    destination_page.wait_for_charter_cards()

    # Check that there are still at least the minimum number of charter cards
    cards_count_after = destination_page.get_charter_cards().count()
    assert cards_count_after >= destination_page.min_charter_cards, (
        f"Expected at least {destination_page.min_charter_cards} "
        f"charter cards, but found {cards_count_after}"
    )

    charter_cards = destination_page.get_charter_cards()
    prices = [
        destination_page.get_price(charter_cards.nth(i))
        for i in range(charter_cards.count())
    ]
    prices = [p for p in prices if p is not None and p > 0]
    assert len(prices) >= 2, "Need at least 2 prices to verify sorting"

    for i in range(len(prices) - 1):
        assert comparison_operator(
            prices[i], prices[i + 1]
        ), f"Sorting failed for {sort_method} | Full list: {prices}"
