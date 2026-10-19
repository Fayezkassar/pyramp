from decimal import Decimal

import pytest

from pyramp.money import parse_amount


def test_parses_thousand_separators() -> None:
    assert parse_amount("1,250,000.50 EUR") == (Decimal("1250000.50"), "EUR")


def test_parses_stripped_amount() -> None:
    assert parse_amount("  42 usd  ") == (Decimal("42"), "USD")


def test_rejects_empty_string() -> None:
    with pytest.raises(ValueError):
        parse_amount("")


def test_rejects_invalid_amount() -> None:
    with pytest.raises(ValueError):
        parse_amount("abc EUR")
