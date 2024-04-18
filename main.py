import mysql.connector
import random
#import GUI

#Connection to MySQl WorkBench
connection = mysql.connector.connect(
    host='localhost',
    database='elite_102',
    user='root',
    password='Alice@060306'
)

cursor =connection.cursor()
test_query = ("SELECT * FROM new_table" )
cursor.execute(test_query)

#Print the table in the MySQL workbench for testing
for item in cursor:
    print(item)


#Function to automatic assign ID
#def assign_id():
#    cursor.execute("ALTER TABLE new_table MODIFY COLUMN account_number INT AUTO_INCREMENT PRIMARY KEY")
#    connection.commit()
#    print("ID assigned successfully.")

#Function to create new account
def new_user(username, name, age, gender, balance, password):
    user_query = "INSERT INTO new_table (username, name, age, gender, balance, password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (username, name, age, gender, balance, password)
    cursor.execute(user_query, values)
    return ("Successful created new user")


#Function to delete the account
def close_account(username):
    user_delete = (f"DELETE FROM new_table WHERE username = {username}")
    cursor.execute(user_delete)
    return cursor.fetchall()

def check_account(account):
    balance_query = (f"SELECT balance FROM new_table WHERE account_number = {account}")
    cursor.execute(balance_query)
    return(float(cursor.fetchall()[0][0]))


def deposit_money(amount, account):
    balance = check_account(account)
    deposit_amount = (f"UPDATE new_table SET balance = {amount + balance}  WHERE account_number = {account}")
    cursor.execute(deposit_amount)


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


print(check_account(1234))
deposit_money(100, 1234)
print(check_account(1234))
withdraw_money(100,1345)
print(check_account(1345))
print(new_user("An2006", "An", 18, "Female", 2500.50, "HookEm4Life"))

cursor.close()
connection.close()