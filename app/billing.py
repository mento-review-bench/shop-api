from decimal import Decimal, ROUND_HALF_UP

TAX_RATE = Decimal("0.20")

def line_total(price, qty):
    return (Decimal(str(price)) * qty).quantize(Decimal("0.01"), ROUND_HALF_UP)

def invoice_total(lines):
    subtotal = sum((line_total(p, q) for p, q in lines), Decimal("0"))
    return (subtotal * (1 + TAX_RATE)).quantize(Decimal("0.01"), ROUND_HALF_UP)

def paginate(items, page, per_page=10):
    start = (page - 1) * per_page
    return items[start:start + per_page]
