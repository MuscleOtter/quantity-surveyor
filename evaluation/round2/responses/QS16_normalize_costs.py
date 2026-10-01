"""Supplied cost framework; pure calculation with no persistence or network I/O."""
from decimal import Decimal
from math import isfinite
from numbers import Real

FRAMEWORK = {
    "B01": {"label": "Site and substructure", "allowed_units": {"m3", "m2", "item"}},
    "B02": {"label": "Structure and envelope", "allowed_units": {"m2", "kg", "item"}},
    "B03": {"label": "Interior and display", "allowed_units": {"m2", "m", "item"}},
}


def normalize_costs(rows):
    """Return normalized USD costs; raise ValueError on invalid row data."""
    def number(value, field):
        if isinstance(value, bool) or not isinstance(value, (Real, Decimal)):
            raise ValueError(f"{field} must be numeric, excluding booleans")
        if value < 0:
            raise ValueError(f"{field} must be finite and nonnegative")
        try:
            converted = float(value)
        except (OverflowError, ValueError, TypeError) as exc:
            raise ValueError(f"{field} must be finite and nonnegative") from exc
        if not isfinite(converted) or converted < 0:
            raise ValueError(f"{field} must be finite and nonnegative")
        return converted

    seen = set()
    normalized = []
    totals = {code: Decimal(0) for code in FRAMEWORK}
    try:
        iterator = iter(rows)
    except TypeError as exc:
        raise ValueError("rows must be iterable") from exc
    for row in iterator:
        if not isinstance(row, dict):
            raise ValueError("each row must be a dictionary")
        if not {"id", "code", "qty", "unit", "rate_USD"} <= row.keys():
            raise ValueError("row missing a required field")
        row_id, code, unit = row["id"], row["code"], row["unit"]
        if not isinstance(row_id, str) or not row_id:
            raise ValueError("row id must be a nonempty string")
        if row_id in seen:
            raise ValueError(f"duplicate row id: {row_id}")
        if not isinstance(code, str) or code not in FRAMEWORK:
            raise ValueError(f"unknown framework code: {code}")
        if not isinstance(unit, str) or unit not in FRAMEWORK[code]["allowed_units"]:
            raise ValueError(f"unit mismatch for {code}: {unit}")
        qty = number(row["qty"], "qty")
        rate = number(row["rate_USD"], "rate_USD")
        amount = Decimal(str(qty)) * Decimal(str(rate))
        if not isfinite(float(amount)):
            raise ValueError("amount_USD exceeds finite output range")
        totals[code] += amount
        seen.add(row_id)
        normalized.append({
            "id": row_id, "code": code, "label": FRAMEWORK[code]["label"],
            "qty": qty, "unit": unit, "rate_USD": rate, "amount_USD": float(amount),
        })
    grand = sum(totals.values(), Decimal(0))
    if not isfinite(float(grand)):
        raise ValueError("grand_total_USD exceeds finite output range")
    return {
        "rows": normalized,
        "element_totals_USD": {code: float(total) for code, total in totals.items()},
        "grand_total_USD": float(grand),
    }


if __name__ == "__main__":
    supplied_rows = [
        {"id": "r1", "code": "B01", "qty": 30, "unit": "m3", "rate_USD": 110},
        {"id": "r2", "code": "B02", "qty": 250, "unit": "m2", "rate_USD": 420},
        {"id": "r3", "code": "B03", "qty": 80, "unit": "m", "rate_USD": 250},
    ]
    print(normalize_costs(supplied_rows))
