expenses = []

try:
    file = open("expenses.txt", "r")

    for line in file:
        data = line.strip().split(",")

        category = data[0]
        name = data[1]
        amount = float(data[2])

        expenses.append([category, name, amount])
    file.close()

except FileNotFoundError:
    pass

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([category, name, amount])

        file = open("expenses.txt", "a")
        file.write(category + "," + name + "," + str(amount) + "\n")
        file.close()

        print("Expense added successfully!")

    elif choice == "2":
        print("\nExpenses List")

        for expense in expenses:
            print(expense[0], "-", expense[1], "- ₹", expense[2])
    
    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[2]

        print("Total Spending = ₹", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")