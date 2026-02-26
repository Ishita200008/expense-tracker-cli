import json
import datetime
import os


if not os.path.exists("expense.json"):
     with open ("expense.json","w") as f:
          json.dump([],f)

#loading exisitng
with open("expense.json","r") as f:
     expenses = json.load(f)

while True:
    print("Here is th menu: 1. Add expense , 2. View All, 3. Filter by category, 4. category summary , 5. exit")
    
    try :
        user_input  =int(input("Please enter your choice:"))
    except ValueError:
         print("invalid input. enter the valid number between 1 to 4")
         continue

    if user_input ==1:
        print("Adding new expense\n")
        # categorys = input ("Enter the category of the expense i.e.,  Amount, categroy, date : ")
        amount = 0
        category = ""
        date = ""
        val= {
                "amount":float(input("enter amount: ")),
                "category": input("enter category: "),
                "date": input("enter date in DD/MM/YYYY format: ")
            }
        expenses.append(val)
        with open ("expense.json","w") as f:
            json.dump(expenses,f,indent=4)
        print("expense added successfully\n")

    elif user_input ==2:
         total = 0
         Month_wise_expenses = {}
         print("Viewing all expenses\n")
         with open("expense.json","r") as f:
              expense = json.load(f)
              for exp in expense:
                   #print(f"{exp['amount']} | {exp['category']} | {exp['date']} ")
                   total += exp['amount']

                   date_obj = datetime.datetime.strptime(exp["date"],"%d/%m/%Y")
                   month = date_obj.month

                   if month  not in  Month_wise_expenses:
                        Month_wise_expenses[month]= 0
                   Month_wise_expenses[month]+= exp["amount"]

              for month, amount in Month_wise_expenses.items():
                   print(f"Month: {month} | Total expenses: {amount}")

              print(f"Total expenses: {total}")

    elif user_input ==3:
         print ("Filtering by category\n")
         category_input = input ("Enter the categoy you want to filter by: ")
         with open ("expense.json","r") as f:
            expense = json.load(f)
            found = False
            for exp in expense:
                if exp["category"].lower()== category_input.lower():
                    print(f"{exp['amount']} | {exp['date']}")
                    found = True
            if not found:
                print(f"No expenses found for category: {category_input}\n")

    elif user_input == 4:
        category_list ={}
        with open ("expense.json","r")as f:
            expense = json.load(f)
            for exp in expense:
                if exp["category"] not in category_list:
                    category_list[exp["category"]] = 0
                category_list[exp["category"]] += exp["amount"]

        for category, amount in category_list.items():
            print(f"{category}: {amount}")
    

    elif user_input ==5:
         print("exsiting thee application")
         break
    else:
         print("invalid input. enter the valid number between 1 to 4\n")

   