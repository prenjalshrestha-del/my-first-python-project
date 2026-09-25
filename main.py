print("===== Expense Tracker =====")
expenses = []

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")
        print(expenses)

    elif choice == "2":
        print("===== YOUR EXPENSES =====")
        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print("Name:", expense["name"])
                print("Amount:", expense["amount"])

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print("Total expenses:", total)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
