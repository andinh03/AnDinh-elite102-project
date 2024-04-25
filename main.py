import mysql.connector

#Connection to MySQl WorkBench
connection = mysql.connector.connect(
    host='localhost',
    database='elite_102',
    user='root',
    password='Alice@060306'
)

cursor =connection.cursor()

#Function to create new account
def new_user(username, name, age, gender, balance, password):
    user_query = "INSERT INTO new_table (username, name, age, gender, balance, password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (username, name, age, gender, balance, password)
    cursor.execute(user_query, values)
    connection.commit()
    return "Successful created new user"

#Function to modify the users information
def name_update(name, id):
    name_query = f"UPDATE new_table SET name = '{name}' WHERE account_number = {id}"
    cursor.execute(name_query)
    connection.commit()
    return "Succesfully changed name"

def password_update(password, id):
    password_query = f"UPDATE new_table SET password = '{password}' WHERE account_number {id}"
    cursor.execute(password_query)
    connection.commit()
    return "Password successfully changed"

#Function to delete the account
def close_account(username):
    user_delete = f"DELETE FROM new_table WHERE username = '{username}'"
    cursor.execute(user_delete)
    connection.commit()
    return "Username succesfully changed"

#Function to check the account balance
def check_account(account):
    balance_query = "SELECT balance FROM new_table WHERE account_number = %s "
    cursor.execute(balance_query, (account, ))
    return float(cursor.fetchone()[0])

#Function to deposit money into account balance
def deposit_money(amount, account):
    balance = check_account(account)
    deposit_amount = balance + amount
    deposit_query = f"UPDATE new_table SET balance = {deposit_amount}  WHERE account_number = {account}"
    cursor.execute(deposit_query)
    connection.commit()

#Function to withdraw money from the designate account
def withdraw_money(amount, account): 
    balance = check_account(account)
    if balance >= amount:
        withdraw_amount = balance - amount
        withdraw_query = f"UPDATE new_table SET balance = {withdraw_amount} WHERE account_number = {account}"
        cursor.execute(withdraw_query)
        connection.commit()
    else:
        print("Insufficient funds")

#Welcome Statement
print("Welcome to Bank of America Online Banking System")

#User Input
def user_input():
    print("Please choose from the following service: ")
    print("1. Create a New Account")
    print("2. Modify Account")
    print("3. Close Current Account")
    print("4. Check Account Balance")
    print("5. Deposit Money")
    print("6. Withdraw Money")
    print("7. Back to Main Menu")

    number = int(input("Enter the number of your choice: "))
    if number == 1:
        new_user(
            input("Enter username: "),
            input("Enter name: "),
            int(input("Enter age: ")),
            input("Enter gender: "),
            float(input("Enter balance: ")),
            input("Enter password: ")
        )
    elif number == 2:
        print("Choose what you want to modify: ")
        print("1. Update Name")
        print("2. Update Password")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name_update(input("Enter new name: "), input("Enter account number: "))
        elif choice == 2:
            password_update(input("Enter new password: "), input("Enter account number: "))
    elif number == 3:
        close_account(input("Enter username: "))
    elif number == 4:
        print("Account balance: $", check_account(input("Enter account number: ")))
    elif number == 5:
        deposit_money(float(input("Enter deposit amount: ")), input("Enter account number: "))
    elif number == 6:
        withdraw_money(float(input("Enter withdrawal amount: ")), input("Enter account number: "))
    elif number == 7:
        print("Returning to Main Menu...")
    else:
        print("Invalid choice")

user_input()


cursor.close()
connection.close()