expenses = []


def add_expense():
    amount = input("Amount (or 'done' to finish): ")

    if amount == "done":
        return False

    amount = float(amount)
    category = input("Category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    return True

def show_expenses():
    print("\nYour expenses:")

    for expense in expenses:
        print(f"- {expense['amount']:.2f} € | {expense['category']}")


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total:", total)


def main():
    while True:
        print("\n1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            show_total()
        elif choice == "4":
            break

main()