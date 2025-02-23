from expense_db import ExpenseDB
from expense_class import Expense


new_expenseDB = ExpenseDB()

first_expense = Expense("First Expense","34.56")
second_expense = Expense("Second Expense","34.56")
third_expense = Expense("Third Expense","4.56")
fourth_expense = Expense("Fourth Expense","34.56")
fifth_expense = Expense("Fifth Expense","3.56")
new_expenseDB.add_expense(first_expense)
new_expenseDB.add_expense(second_expense)
new_expenseDB.add_expense(third_expense)
new_expenseDB.add_expense(fourth_expense)
new_expenseDB.add_expense(fifth_expense)

print(new_expenseDB.to_dict())

new_expenseDB.remove_expense(new_expense2.id)

print(new_expenseDB.to_dict())

print(new_expenseDB.get_expense_by_id(new_expense2.id))