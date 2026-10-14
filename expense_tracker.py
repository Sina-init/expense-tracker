from time import sleep
from database import cursor, connection


    

def showExpenses():
    cursor.execute("SELECT * FROM expenses")
    rows=cursor.fetchall()
    if rows:
        for row in rows:
            print(f"{row[0]}.{row[1]} - {row[2]} - {row[3]}")
        return True
    else:
        print("No expenses found!")
        return False

while True:
    print()
    print("="*5,"Expense Tracker","="*5)
    text="1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Delete Expense\n5.Show Category Totals\n6.Search Expense\n7.Edit Expense\n8. Exit"
    for word in text.split():
        if word[0].isdigit():
            print()
            print(word,end="")
        else:
            print(word,end="")
        sleep(0.2)
    sleep(0.5)
    number=input("\n\nChoose an option: ")
    while not number.isdigit() or not 1<=int(number)<=8:    
        number=input("Choose a valid option: ")
    print()
    if int(number)==1:
        print("1.Add Expense\n")
        while True:
            expense=input("Enter the amount:")
            try:
                if float(expense)>0:
                    break
                else:
                    print("Amount must be greater than zero!")
            except ValueError:
                print("Enter a valid number!")
        while True:
            category=input("Enter the category:").strip()
            if category:
                break
            else:
                print("The category is not valid!")
        while True:
            description=input("Enter the description:").strip()
            if description:
                break
            else:
                print("The description is not valid!")
        cursor.execute(
            "INSERT INTO expenses(category,description,amount) VALUES(?,?,?)",
            category,
            description,
            expense
        )
        connection.commit()
        sleep(0.2)
        print("\nExpense added successfully!")
    elif int(number)==2:
        print("2. Show Expenses\n")
        showExpenses()
    elif int(number)==3:
        cursor.execute("select sum(amount) from expenses")
        row=cursor.fetchone() 
        print("3. Show Total\n\n")
        if row[0] is None:
            print("Total expenses: 0")
        else:   
            print(f"Total expenses: {row[0]}")
    elif int(number)==4:
        print("4. Delete Expense\n")
        showExpenses()
        print()
        delete=input("Choose an expense to delete: ")
        while not delete.isdigit():
            delete=input("Choose a valid option to delete: ")
        print()
        cursor.execute("DELETE FROM expenses WHERE id=?",delete)
        if cursor.rowcount>0:
            connection.commit()
            print("The expense's been deleted successfully.")
        else:
            print("The expense was not found!")
    elif int(number)==5:
        print("5.Show Category Totals")
        cursor.execute("SELECT category,SUM(amount) FROM expenses GROUP BY category")
        rows=cursor.fetchall()
        if rows:
            for row in rows:
                print(f"{row[0]} ==> {row[1]}")
        else:
            print("There are no expenses")
    elif int(number)==6:
        print("6.Search Expense\n")
        search=input("Enter a category or description to search:").strip()
        while not search:
            search=input("Enter a category or description to search:").strip()
        print()
        cursor.execute("SELECT * FROM expenses WHERE category LIKE ? OR description LIKE ?",f"%{search}%",f"%{search}%")
        rows=cursor.fetchall()
        if rows:
            for row in rows:
                print(f"{row[0]}.{row[1]} - {row[2]} - {row[3]}")
        else:
            print("No expenses found!")
    elif int(number)==7:
        print("7.Edit Expense\n")
        if showExpenses():
            edit=input("Choose an expense to edit:").strip()
            while not edit.isdigit():
                edit=input("Choose an expense to edit:").strip()
            print()
            print("What do you want to edit:\n1.Category\n2.Description\n3.Amount\n")
            editingPart=input("Choose an option:")
            while not editingPart.isdigit() or not 1 <= int(editingPart) <= 3:
                editingPart=input("Choose an option:")
            if editingPart=="3":
                while True:
                    newData=input(f"Enter the new Amount:").strip()
                    try:
                        if float(newData)>0:
                            break
                        else:
                            print("Amount must be greater than zero!")   
                    except ValueError:
                        print("Enter a valid number!")   
                cursor.execute("UPDATE expenses SET amount=? WHERE id=?",newData,edit)
            elif editingPart=="1":
                newData=input(f"Enter the new Category:").strip()
                while not newData:
                    newData=input(f"Enter the new Category:").strip()
                cursor.execute("UPDATE expenses SET category=? WHERE id = ? ",newData,edit)
            else:
                newData=input(f"Enter the new description:").strip()
                while not newData:
                    newData=input(f"Enter the new description:").strip()
                cursor.execute("UPDATE expenses SET description=? WHERE id =?",newData,edit)
            print()
            if cursor.rowcount>0:
                connection.commit()
                print("The value has changed successfully.")    
            else:
                print("The expense was not found!")
    elif int(number)==8:
        break