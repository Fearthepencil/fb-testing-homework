import re


def parse_length(length_text: str) -> int:
    match = re.search(r'(\d+)\s*ft', length_text, re.IGNORECASE)
    if not match:
        raise ValueError(f"Could not parse boat length from: '{length_text}'")
    return int(match.group(1))

def parse_price(price_text: str) -> float:
    cleaned = price_text.lower()
    cleaned = re.sub(r'trips?\s*from\s*', '', cleaned)
    cleaned = re.sub(r'from\s*', '', cleaned)
    cleaned = re.sub(r'[€$£,]', '', cleaned)

    match = re.search(r'(\d+(?:\.\d+)?)', cleaned)
    if not match:
        raise ValueError(f"Could not parse price from: '{price_text}'")

    return float(match.group(1))
    