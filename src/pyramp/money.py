from decimal import Decimal, InvalidOperation


def parse_amount(raw: str) -> tuple[Decimal, str]:
    """Parse '1,250,000.50 EUR' into (Decimal('1250000.50'), 'EUR')."""
    parts = raw.strip().split()

    if len(parts) != 2:
        raise ValueError("Invalid amount format")

    currency = parts[1].upper()
    if len(currency) != 3:
        raise ValueError("Invalid currency code")

    amount_text = parts[0].replace(",", "")
    try:
        amount = Decimal(amount_text)
    except InvalidOperation as e:
        raise ValueError("Invalid amount") from e

    return amount, currency
