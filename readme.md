# Expense Tracker

This is a simple Expense Tracker project built with Python. It allows users to create, update, list, and delete expenses using an in-memory database (a list in Python). Each expense has a unique ID, title, amount, and timestamps for creation and updates.

## Features

- Create a new expense with a title and amount.
- Update an existing expense.
- Convert an expense object to a dictionary.
- Store expenses in an in-memory list.
- Remove an expense by its unique ID.
- Find an expense by it title or ID

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x

## Installation

To get started with this project, follow these steps:

### 1. Clone the Repository

```sh
git clone https://github.com/fakoredeDamilola/expense-tracker.git
cd expense-tracker
```

### 2. Install Dependencies

This project does not have external dependencies, but ensure you have Python installed.

## Usage

### Running the Project

1. Open a terminal and navigate to the project directory.
2. Run the Python script:
   ```sh
   python main.py
   ```

### Example Usage in Python

```python
from expense_class import Expense
from expense_db import ExpenseDB

# Create an expense database
expense_db = ExpenseDB()

# Add an expense
expense = Expense("Groceries", 50.75)
expense_db.add_expense(expense)

# Print all expenses
print(expense_db.to_dict())

# Remove an expense
expense_db.remove_expense(expense.id)
print(expense_db.to_dict())
```

## Project Structure

```
expense-tracker/
│── expense_class.py  # Defines the Expense class
│── expense_db.py     # Manages the list of expenses
│── main.py           # Main script to run the project
│── readme.md         # Project documentation
```
