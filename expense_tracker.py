import json


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


expenses = load_expenses()


def add_expense():
    amount = input("Amount (or 'done' to finish): ")

    if amount == "done":
        return False

    try:
        amount = float(amount)

        if amount < 0:
            print("Amount cannot be negative.")
            return True

    except ValueError:
        print("Invalid amount.")
        return True

    category = input("Category: ")

    if category.strip() == "":
        print("Category cannot be empty.")
        return True

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return True

def delete_expense():
    show_expenses()

    if not expenses:
        return

    choice = input("Enter the number of the expense to delete: ")

    try:
        index = int(choice) - 1

        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return

        deleted_expense = expenses.pop(index)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print(
            f"Deleted: {deleted_expense['amount']:.2f} € | "
            f"{deleted_expense['category']}"
        )

    except ValueError:
        print("Invalid number.")

def edit_expense():
    show_expenses()

    if not expenses:
        return

    choice = input("Enter the number of the expense to edit: ")

    try:
        index = int(choice) - 1

        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return

        amount = input("New amount: ")

        try:
            amount = float(amount)

            if amount < 0:
                print("Amount cannot be negative.")
                return

        except ValueError:
            print("Invalid amount.")
            return

        category = input("New category: ")

        if category.strip() == "":
            print("Category cannot be empty.")
            return

        expenses[index] = {
            "amount": amount,
            "category": category
        }

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense updated.")

    except ValueError:
        print("Invalid number.")

def show_expenses():
    print("\nYour expenses:")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['amount']:.2f} € | {expense['category']}")


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total: {total:.2f} €")

def show_category_totals():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    print("\nTotals by category:")

    for category, total in category_totals.items():
        print(f"- {category}: {total:.2f} €")


def main():
    while True:
        print("\n1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Delete expense")
        print("5. Edit expense")
        print("6. Totals by category")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            edit_expense()

        elif choice == "6":
            show_category_totals()

        elif choice == "7":
            break


if __name__ == "__main__":
    main()