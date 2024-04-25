import mysql.connector

#Connection to MySQl WorkBench
connection = mysql.connector.connect(
    host='localhost',
    database='elite_102',
    user='root',
    password='Alice@060306'
)

cursor =connection.cursor()
test_query = ("SELECT * FROM new_table")
cursor.execute(test_query)

#Print the table in the MySQL workbench for testing
# for item in cursor:
#     print(item)

#Function to create new account
def new_user(username, name, age, gender, balance, password):
    user_query = "INSERT INTO new_table (username, name, age, gender, balance, password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (username, name, age, gender, balance, password)
    cursor.execute(user_query, values)
    return ("Successful created new user")

#Function to modify the users information
def name_update(name, id):
    name_query = (f"UPDATE new_table SET name = {name} WHERE account_number = {id}")
    cursor.execute(name_query)
    return cursor.fetchall("Name succesfully changed")

def username_update(username, id):
    username = (f"UPDATE new_table SET username = {username} WHERE account_number = {id}")
    cursor.execute(username)
    return cursor.fetchall("Username successfully changed")

def password_update(password, id):
    password = (f"UPDATE new_table SET password = {password} WHERE account_number {id}")
    cursor.execute(password)
    return cursor.fetchall("Password successfully changed")

#Function to delete the account
def close_account(username):
    user_delete = (f"DELETE FROM new_table WHERE username = {username}")
    cursor.execute(user_delete)
    return cursor.fetchall("Username succesfully changed")

#Function to check the account balance
def check_account(account):
    balance_query = (f"SELECT balance FROM new_table WHERE account_number = {account}")
    cursor.execute(balance_query)
    return(float(cursor.fetchall()[0][0]))

#Function to deposit money into account balance
def deposit_money(amount, account):
    balance = check_account(account)
    deposit_amount = (f"UPDATE new_table SET balance = {amount + balance}  WHERE account_number = {account}")
    cursor.execute(deposit_amount)

#Function to withdraw money from the designate account
def withdraw_money(amount, account): 
    balance = check_account(account)
    if balance >= amount:
        withdraw_amount = (f"UPDATE new_table SET balance = {balance - amount} WHERE account_number = {account}")
        cursor.execute(withdraw_amount)
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
        new_user(input("username, name, age, gender, balance, password: "))

user_input()
# print(check_account(1234))
# deposit_money(100, 1234)
# print(check_account(1234))
# withdraw_money(100,1345)
# print(check_account(1345))
name_update("Chandler", 6093)

cursor.close()
connection.close()