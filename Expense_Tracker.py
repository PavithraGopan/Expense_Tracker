import csv
import datetime
from collections import defaultdict

def load_expenses(file_name="expenses.csv"):
    expenses = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    'Amount': float(row['Amount']),
                    'Category': row['Category'],
                    'Date': row['Date']
                })
    except FileNotFoundError:
        print("No previous expense records found. Starting fresh.")
    return expenses

def save_expenses(expenses, file_name="expenses.csv"):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['Amount', 'Category', 'Date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def add_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Invalid amount entered. Please enter a numeric value.")
        return

    category = input("Enter the expense category (e.g., Food, Transport, etc.): ")
    
    use_today = input("Use today's date? (y/n): ").lower()
    if use_today == 'y':
        date = str(datetime.date.today())
    else:
        date = input("Enter the date (YYYY-MM-DD): ")

    expense = {
        'Amount': amount,
        'Category': category,
        'Date': date
    }
    expenses.append(expense)
    print("Expense added successfully.")

def view_summary(expenses):
    if not expenses:
        print("No expenses to show.")
        return

    print("Choose an option to view summary:")
    print("1. Total spending by category")
    print("2. Total overall spending")
    print("3. Spending over time (daily, weekly, monthly)")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        category_totals = defaultdict(float)
        for expense in expenses:
            category_totals[expense['Category']] += expense['Amount']
        for category, total in category_totals.items():
            print(f"Category: {category} | Total spent: ${total:.2f}")
    
    elif choice == '2':
        total_spending = sum(expense['Amount'] for expense in expenses)
        print(f"Total overall spending: ${total_spending:.2f}")
    
    elif choice == '3':
        time_choice = input("View spending by (d)aily, (w)eekly, or (m)onthly? ")
        date_totals = defaultdict(float)

        for expense in expenses:
            date_key = None
            date_obj = datetime.datetime.strptime(expense['Date'], "%Y-%m-%d").date()
            
            if time_choice == 'd':
                date_key = date_obj
            elif time_choice == 'w':
                date_key = date_obj - datetime.timedelta(days=date_obj.weekday())
            elif time_choice == 'm':
                date_key = date_obj.strftime('%Y-%m')
            else:
                print("Invalid choice.")
                return
            
            date_totals[date_key] += expense['Amount']
        
        for date, total in date_totals.items():
            print(f"Date: {date} | Total spent: ${total:.2f}")
    
    else:
        print("Invalid choice. Please try again.")

def main():
    expenses = load_expenses() 
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add an expense")
        print("2. View summaries")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            save_expenses(expenses)
            print("Exiting the program. All data saved.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
if __name__ == "__main__":
    main()
