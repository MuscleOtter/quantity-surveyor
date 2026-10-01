"""In-memory cost normalization for the supplied B01/B02/B03 framework."""

from decimal import Decimal
from math import isfinite, fsum
from numbers import Real

FRAMEWORK = {
    "B01": {"label": "Site and substructure", "allowed_units": {"m3", "m2", "item"}},
    "B02": {"label": "Structure and envelope", "allowed_units": {"m2", "kg", "item"}},
    "B03": {"label": "Interior and display", "allowed_units": {"m2", "m", "item"}},
}


def normalize_costs(rows):
    """Return new rows and USD totals; reject invalid data without recoding it."""
    def numeric(value, field):
        if isinstance(value, bool) or not isinstance(value, (Real, Decimal)):
            raise ValueError(f"{field} must be a finite, nonnegative real number")
        try:
            number = float(value)
        except (OverflowError, ValueError, TypeError) as exc:
            raise ValueError(f"Invalid {field}") from exc
        if not isfinite(number) or number < 0:
            raise ValueError(f"{field} must be finite and nonnegative")
        return number

    normalized, seen = [], set()
    amounts = {code: [] for code in FRAMEWORK}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"Row {index} must be a dictionary")
        if not all(key in row for key in ("id", "code", "qty", "unit", "rate_USD")):
            raise ValueError(f"Row {index} is missing a required field")
        row_id, code, unit = row["id"], row["code"], row["unit"]
        if not isinstance(row_id, str) or not row_id:
            raise ValueError("Row id must be a nonempty string")
        if row_id in seen:
            raise ValueError(f"Duplicate row id: {row_id}")
        seen.add(row_id)
        if not isinstance(code, str) or code not in FRAMEWORK:
            raise ValueError(f"Unknown framework code: {code!r}")
        definition = FRAMEWORK[code]
        if not isinstance(unit, str) or unit not in definition["allowed_units"]:
            raise ValueError(f"Unit {unit!r} is not allowed for {code}")
        qty, rate = numeric(row["qty"], "qty"), numeric(row["rate_USD"], "rate_USD")
        amount = qty * rate
        if not isfinite(amount):
            raise ValueError(f"Amount overflows for row {row_id}")
        normalized.append({"id": row_id, "code": code, "label": definition["label"],
                           "qty": qty, "unit": unit, "rate_USD": rate, "amount_USD": amount})
        amounts[code].append(amount)
    try:
        totals = {code: fsum(values) for code, values in amounts.items()}
        grand_total = fsum(totals.values())
    except OverflowError as exc:
        raise ValueError("Cost totals overflow") from exc
    if not all(isfinite(x) for x in (*totals.values(), grand_total)):
        raise ValueError("Cost totals must be finite")
    return {"rows": normalized, "element_totals_USD": totals, "grand_total_USD": grand_total}


SUPPLIED_ROWS = [
    {"id": "r1", "code": "B01", "qty": 30, "unit": "m3", "rate_USD": 110},
    {"id": "r2", "code": "B02", "qty": 250, "unit": "m2", "rate_USD": 420},
    {"id": "r3", "code": "B03", "qty": 80, "unit": "m", "rate_USD": 250},
]

if __name__ == "__main__":
    print(normalize_costs(SUPPLIED_ROWS))
