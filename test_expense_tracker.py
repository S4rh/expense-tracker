from expense_tracker import expenses


def test_expenses_list():
    assert isinstance(expenses, list)


def test_add_expense_data():
    expense = {
        "amount": 20.0,
        "category": "courses"
    }

    assert expense["amount"] == 20.0
    assert expense["category"] == "courses"


def test_category_totals():
    test_expenses = [
        {"amount": 20.0, "category": "courses"},
        {"amount": 10.0, "category": "courses"},
        {"amount": 15.0, "category": "transport"}
    ]

    totals = {}

    for expense in test_expenses:
        category = expense["category"]

        if category not in totals:
            totals[category] = 0

        totals[category] += expense["amount"]

    assert totals["courses"] == 30.0
    assert totals["transport"] == 15.0