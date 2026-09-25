expenses = []

while True:
    print("\n===== MY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Wise Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        note = input("Enter note: ")

        expense = {
            "category": category,
            "amount": amount,
            "note": note
        }

        expenses.append(expense)

        print("Expense added successfully!")

    # View Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\n----- My Expenses -----")

            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['category']} | "
                    f"Rs.{expense['amount']} | "
                    f"{expense['note']}"
                )

    # Total Expense
    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print(f"Total Expense = Rs.{total:.2f}")

    # Category Wise Expense
    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            category_total = {}

            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]

                if category in category_total:
                    category_total[category] = category_total[category] + amount
                else:
                    category_total[category] = amount

            print("\n----- Category Wise Expense -----")

            for category, amount in category_total.items():
                print(f"{category} = Rs.{amount:.2f}")

    # Exit
    elif choice == "5":
        print("Thank you for using My Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
