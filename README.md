# Python Expense Tracker

This is a Python program that acts as a Personal Expense Tracker to help users log, manage, and track their daily spending. It allows users to categorize their expenses, view summaries, and keep a persistent record of their spending across sessions using file handling.

## Features
- Add an Expense: Users can log new expenses by specifying the amount, category (e.g., Food, Transport, Entertainment), and date.
- View Summary:
- Total spending by category.
- Overall total spending.
- Spending summary over time (daily, weekly, monthly).
- Data Persistence: All expense data is saved to a CSV file, allowing the user to access their previous records even after restarting the program.
- Simple User Interface: A menu-based system that allows users to add expenses, view summaries, or exit the program.

## How It Works
1. The user is presented with a menu with three options:
- Add an expense.
- View summaries of expenses.
- Exit the program.
2. Based on the user's choice:
- Add Expense: The user inputs the amount, selects the category, and specifies the date (or uses the current date).
- View Summary: The user can view a summary by category, overall spending, or spending over specific time periods.
3. Expense data is stored in a CSV file to ensure persistence between program runs.
