import json
import datetime
import os

"""
Expense Tracker Application

This module provides functionality to track personal expenses. It allows users to:
- Add new expenses with amount, category, and date
- View all expenses with monthly totals
- Filter expenses by category
- Get summary of expenses by category

Data is stored in a JSON file named 'expense.json'.
"""

# create json path if not present 
if not os.path.exists("expense.json"):
     with open ("expense.json","w") as f:
          json.dump([],f)

# read the json file by opening
def load_data():
    """
    Load expense data from the JSON file.

    Returns:
        list: A list of expense dictionaries loaded from 'expense.json'.
    """
    with open ("expense.json","r") as f:
        data = json.load(f)
    return data

#append the input 
def save_data(data):
    """
    Save expense data to the JSON file.

    Args:
        data (list): A list of expense dictionaries to save to 'expense.json'.
    """
    with open ("expense.json","w") as f:
          json.dump(data,f,indent=4)


def Adding_Expense():
    """
    Add a new expense to the expense tracker.

    Prompts the user for amount, category, and date, then appends the new expense
    to the data and saves it to the JSON file.
    """
    expenses = load_data()
    print("Adding New Expenses\n")

    # Create a dictionary for the new expense
    val= {
                    "amount":float(input("enter amount: ")),
                    "category": input("enter category: "),
                    "date": input("enter date in DD/MM/YYYY format: ")
                }
        
    expenses.append(val)
    save_data(expenses)
#----------------------------------------------------------------------------------------
def view_expense():
    """
    View all expenses and display monthly totals and overall total.

    Loads all expenses, calculates total expenses and monthly breakdowns,
    then prints the results.
    """
    print("View All Expenses \n")
    total = 0
    Month_wise_expenses = {}
    ViewExp = load_data()
    # Calculate total expenses and group by month
    for exp in ViewExp:
        total += exp['amount']
        try :
            date_obj = datetime.datetime.strptime(exp['date'], "%d/%m/%y")
        except ValueError:
            print(f"Invalid date format {exp['date']}.")

        month = date_obj.month

        

        if month  not in  Month_wise_expenses:
            Month_wise_expenses[month]= 0
        Month_wise_expenses[month]+= exp["amount"]

    for month, amount in Month_wise_expenses.items():
        print(f"Month: {month} | Total expenses: {amount}")
    print(f"Total expenses: {total}")

#--------------------------------------------------------------------------------------------
def filter_by_category():
    """
    Filter and display expenses by a specific category.

    Prompts the user for a category, then displays all expenses matching that category
    (case-insensitive). If no expenses are found, prints a message.
    """
    print ("Filtering by category\n")
    category_input = input ("Enter the categoy you want to filter by: ")
    expense = load_data()
    found = False
    for exp in expense:
        if exp["category"].lower()== category_input.lower():
            print(f"{exp['amount']} | {exp['date']}")
            found = True
    if not found:
        print(f"No expenses found for category: {category_input}\n")

#----------------------------------------------------------------------------------------------
def category_summary():
    """
    Display a summary of total expenses by category.

    Loads all expenses, groups them by category, and prints the total amount
    for each category.
    """
    category_list ={}
    expense = load_data()
    for exp in expense:
        if exp["category"] not in category_list:
            category_list[exp["category"]] = 0
        category_list[exp["category"]] += exp["amount"]

    for category, amount in category_list.items():
        print(f"{category}: {amount}")
    print()



if __name__ == "__main__":
    # Main menu loop for the expense tracker application
    while True:
        try :
            user_input  =int(input("Here is th menu: 1. Add expense , 2. View All, 3. Filter by category, 4. category summary , 5. exit : "))
        except ValueError:
            print("invalid input. enter the valid number between 1 to 5")
            continue
        # Handle user menu selection
        match user_input:
            case 1:
                Adding_Expense()
            case 2:
                view_expense()
            case 3:
                filter_by_category()
            case 4:
                category_summary()
            case 5:
                print("Exiting from the application")
                break




