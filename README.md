# My Expense Tracker

A simple Python-based Expense Tracker that allows users to add, view, and manage their daily expenses through a menu-driven program.

## Features

* Add new expenses
* Enter expense category, amount, and note
* View all saved expenses
* Calculate total expenses
* View expenses category-wise
* Display expenses with serial numbers
* Simple menu-driven interface
* Exit the program when finished

## Technologies Used

* Python
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Functions such as `input()`, `float()`, `len()`, and `enumerate()`

## How It Works

When the program starts, it displays a menu with five options:

1. Add Expense
2. View Expenses
3. Total Expense
4. Category Wise Expense
5. Exit

### 1. Add Expense

The user enters:

* Category
* Amount
* Note

The expense is stored in a dictionary and then added to the expenses list.

Example:

```text
Category: Food
Amount: 500
Note: Lunch
```

### 2. View Expenses

This option displays all the expenses saved by the user.

Example:

```text
----- My Expenses -----
1. Food | Rs.500.0 | Lunch
2. Travel | Rs.1000.0 | Bus
```

### 3. Total Expense

This option calculates the total amount of all saved expenses.

Example:

```text
Total Expense = Rs.1500.00
```

### 4. Category Wise Expense

This option calculates how much money was spent in each category.

Example:

```text
----- Category Wise Expense -----
Food = Rs.800.00
Travel = Rs.1000.00
Shopping = Rs.500.00
```

### 5. Exit

This option closes the program.

## Concepts Practiced

This project helped me practice the following Python concepts:

* Variables
* Lists
* Dictionaries
* User Input
* Type Conversion
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* `append()`
* `len()`
* `enumerate()`
* Dictionary `.items()`
* String formatting
* `break`
## Clone Repository

To get a copy of this project on your computer, run:

```bash
git clone https://github.com/hamnanadeem04/Python_Expense_Tracker.git
```

## How to Run
Make sure Python is installed on your computer.
Download or clone this repository.
Open the project folder in VS Code or a terminal.
Run the Python file.

Example:

```bash
python expense_tracker.py
```

## Example

```text
===== MY EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Total Expense
4. Category Wise Expense
5. Exit

Enter your choice: 1
Enter category: Food
Enter amount: 500
Enter note: Lunch

Expense added successfully!
```

## Project Purpose

The purpose of this project is to practice Python programming by building a simple real-world application for tracking personal expenses.

## Author

Hamna Khan
Computer Science Student | Aspiring AI/ML Develope
