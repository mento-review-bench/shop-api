from app.billing import invoice_total, paginate
from decimal import Decimal

def test_total():
    assert invoice_total([(10, 2), (1.5, 1)]) == Decimal("25.80")

def test_paginate():
    assert paginate(list(range(25)), 3) == list(range(20, 25))

def test_count_orders():
    import sqlite3
    from app.db import count_orders
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE orders (id INTEGER, user_id INTEGER, total TEXT)")
    c.executemany("INSERT INTO orders VALUES (?,?,?)", [(1, 7, "1"), (2, 7, "2"), (3, 8, "3")])
    assert count_orders(c, 7) == 2
