
Expense = {}
Income = {}

def sum(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum


def expense_tracker(Num_of_expenses):
    for i in range(Num_of_expenses):
        Expense_name = input(f"Enter the name of expense #{i+1}:")
        Cost = float(input(f"Enter the amount of expense #{i+1}:"))
        Expense[Expense_name] = Cost



print("-------------WELCOME TO MY BUDGET SHEET CALCULATOR---------------------")
Monthly_income = int(input("Enter your monthly net income:"))
Income["Monthly_Income"] = Monthly_income
Expense_num_prompt = int(input("How many expenses do you have?:"))
expense_tracker(Expense_num_prompt)
Total_Expenses = sum(list(Expense.values()))
print(f"Total expenses:${Total_Expenses}")
print(f"Remaining monthly income:{Income['Monthly_Income'] - Total_Expenses }")

