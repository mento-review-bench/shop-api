from app.billing import invoice_total, paginate
from decimal import Decimal

def test_total():
    assert invoice_total([(10, 2), (1.5, 1)]) == Decimal("25.80")

def test_paginate():
    assert paginate(list(range(25)), 3) == list(range(20, 25))
