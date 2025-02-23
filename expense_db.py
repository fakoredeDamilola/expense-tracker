
class ExpenseDB:
    def __init__(self):
        self.expenses_list = list()

    def add_expense(self,expense):
        self.expenses_list.append(expense)

    def remove_expense(self,expense_id):
        self.expenses_list = [expense for expense in self.expenses_list if str(expense.id) != str(expense_id)]

    def get_expense_by_id(self,expense_id):
        for expense in self.expenses_list:
            if expense.id == expense_id:
                return expense
        return "expense not found"

    def get_expense_by_title(self,expense_title):
        for expense in self.expenses_list:
            if expense.title == expense_title:
                return expense
        return "expense not found"

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses_list]
        


