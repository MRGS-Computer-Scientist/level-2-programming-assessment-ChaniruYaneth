from tkinter import *
import time

# Funtion to create an account
def create_account():
    # Funtion to handle the submission of create account form
    def submit():
        # Getting/retrieving user inputs
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        # Check if passwords match
        if password == confirm_password:
            # Check if username already exists
            if username in users:
                message_label.config(text="You already have an account. Please sign-in.")
            else:
                # Add username andd password to users list
                users[username] = password
                message_label. config(text="You have succesfully signed-up.")
                create_account_window.after(3000, create_account_window.destroy)

        else:
            message_label.config(text="Passwords do not match. Please try again.")
    # Create small window for creating an account
    create_account_window = Toplevel(root)
    create_account_window.title("Sign-Up")
    create_account_window.geometry("500x300")
    create_account_window.config(bg="#F2EEE3")

    # Username label and entry
    username_label = Label(create_account_window, text="Username:", bg="#F2EEE3", font=("Arial", 14))
    username_entry = Entry(create_account_window, font=("Arial", 14))

    # Password label and entry
    password_label = Label(create_account_window, text="Password", bg="F2EEE3", font=("Arial", 14))
    password_entry = Entry(create_account_window, show="*", font=("Arial", 14))

    # Confirm password label and entry
    confirm_password_label = Label(create_account_window, text="Confirm Password", bg="F2EEE3", font=("Arial", 14))
    confirm_password_entry = Entry(create_account_window, show="*", font=("Arial", 14))

    # Submit button
    submit_button = Button(create_account_window, text="Submit", bg="#BCA0A0", font=("Arial", 14), command=submit)

    # Message label
    message_label = Label(create_account_window, text="", bg="F2EEE3", fg="red", font=("Arial", 12))

    # Arrange elements in grid
    username_label.grid(row=0, column=0, padx=10, pady=10)
    username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    password_label.grid(row=1, column=0, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    confirm_password_label.grid(row=2, column=0, padx=10, pady=10)
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)
    message_label.grid(row=4, column=0, columnspan=2, pady=10)

# Function to sign in
def sign_in():
        username = username_entry.get()
        password = password_entry.get()

        if username in users and users[username] == password:
             message_label.config(text="You have successfully signed in. Enjoy RIGHTWAY!!!")
        else:
            message_label.config(text="Username and Password are invalid. Please try again.")