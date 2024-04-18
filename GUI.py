import mysql.connector
import tkinter as tk

# Connection to MySQL Workbench
connection = mysql.connector.connect(
    host='localhost',
    database='elite_102',
    user='root',
    password='Alice@060306'
)

cursor =connection.cursor()
user = ("SELECT name FROM new_table")

#Create the root window that will hold the entire GUI application
root = tk.Tk()
root.title("Bank of America Online Banking System")

#Create labels for username and password
username_label = tk.Label(root, text= "Username: ")
password_label = tk.Label(root, text= "Password: ")

#Entry fields for username and password
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

account_window = tk.Toplevel(root)

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Query to check if username and password match
    query = f"SELECT * FROM new_table WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        # Successful login, open account window
        open_account_window(result)
    else:
        # Incorrect username or password
        error_label.config(text="Incorrect username or password", fg="red")

# Function to open account window
def open_account_window(user):
    account_window = tk.Toplevel(root)
    account_window.title("Account Details")
    
    # Display account details
    account_label = tk.Label(account_window, text=f"Welcome, {user}")
    account_label.pack()

# Function to handle deposit
def deposit(user):
    amount = float(deposit_entry.get())
    balance = user + amount
    update_balance(balance)

# Function to handle withdrawal
def withdraw(user):
    amount = float(withdraw_entry.get())
    if amount <= user:
        balance = user - amount
        update_balance(balance)
    else:
        error_label.config(text="Insufficient funds", fg="red")

# Function to update balance in database
def update_balance(balance, user):
    query = f"UPDATE new_table SET balance = {balance} WHERE username = '{user}'"
    cursor.execute(query)
    connection.commit()
    user = balance  # Update balance in user variable
    balance_label.config(text=f"Balance: ${balance}")

# Deposit Section
deposit_label = tk.Label(account_window, text="Deposit Amount:")
deposit_label.pack()
deposit_entry = tk.Entry(account_window)
deposit_entry.pack()
deposit_button = tk.Button(account_window, text="Deposit", command=deposit)
deposit_button.pack()

# Withdraw Section
withdraw_label = tk.Label(account_window, text="Withdraw Amount:")
withdraw_label.pack()
withdraw_entry = tk.Entry(account_window)
withdraw_entry.pack()
withdraw_button = tk.Button(account_window, text="Withdraw", command=withdraw)
withdraw_button.pack()

# Display balance
balance_label = tk.Label(account_window, text=f"Balance: ${user}")
balance_label.pack()

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, sticky="W")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, sticky="W")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Error Label
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=2, columnspan=2)



root.mainloop()