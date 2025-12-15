import re


def parse_length(length_text: str) -> int:
    match = re.search(r'(\d+)\s*ft', length_text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return int(length_text.strip())

def parse_price(price_text: str) -> float:
    #Remove currency symbols, "trips from", "from", commas, spaces
    cleaned = re.sub(r'[€$£, ]', '', price_text, flags=re.IGNORECASE)
    cleaned = re.sub(r'trips?\s*from\s*', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'from\s*', '', cleaned, flags=re.IGNORECASE)
    match = re.search(r'(\d+(?:\.\d+)?)', cleaned)
    if match:
        return float(match.group(1))
    return float(cleaned)