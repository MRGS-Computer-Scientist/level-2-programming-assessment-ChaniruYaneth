from tkinter import *
import time

# Function to create an account
def create_account():
    # Function to handle submission of create account form
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
                # Add username and password to users list
                users[username] = password
                message_label. config(text="You have successfully signed-up.")
                create_account_window.after(3000, create_account_window.destroy)

        else:
            message_label.config(text="Passwords do not match. Please try again.")
    # Create small window for creating an account
    create_account_window = Toplevel(root)
    create_account_window.title("Create Account")
    create_account_window.geometry("500x300")
    create_account_window.config(bg="#F2EEE3")

    # Username label and entry
    username_label = Label(create_account_window, text="Username:", bg="#F2EEE3", font=("Arial", 14))
    username_entry = Entry(create_account_window, font=("Arial", 14))

    # Password label and entry
    password_label = Label(create_account_window, text="Password", bg="#F2EEE3", font=("Arial", 14))
    password_entry = Entry(create_account_window, show="*", font=("Arial", 14))

    # Confirm password label and entry
    confirm_password_label = Label(create_account_window, text="Confirm Password", bg="#F2EEE3", font=("Arial", 14))
    confirm_password_entry = Entry(create_account_window, show="*", font=("Arial", 14))

    # Submit button
    submit_button = Button(create_account_window, text="Submit", bg="#BCA0A0", font=("Arial", 14), command=submit)

    # Message label
    message_label = Label(create_account_window, text="", bg="#F2EEE3", fg="red", font=("Arial", 12))

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
        # Retrieve inputs
        username = username_entry.get()
        password = password_entry.get()
        
        # Check if username and password match
        if username in users and users[username] == password:
             message_label.config(text="You have successfully signed in. Enjoy RIGHTWAY!!!")
        else:
            message_label.config(text="Username and Password are invalid. Please try again.")

# Create the main window
root = Tk()
root.title("Login Page")
root.geometry("700x500")
root.config(bg="#F2EEE3")

# Define users list to store credentials
users = {}

# Load logo image
logo_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\logo.png")

# Resize the logo image
resized_logo_image = logo_image.subsample(2, 2)

# Logo label
logo_label = Label(root, image=resized_logo_image, bg="#F2EEE3")
logo_label.pack(pady=(20, 10))

# Do not have an account label
no_account_label = Label(root, text="Do not have an account?", bg="#F2EEE3", font=("Arial", 14))
no_account_label.pack()

# Sign up button
sign_up_button = Button(root, text="SIGN UP", bg="#BCA0A0", font=("Arial", 14), command=create_account)
sign_up_button.pack(pady=10)

# Username label and entry
username_frame = Frame(root, bg="#F2EEE3")
username_frame.pack(pady=(0, 10))
username_label = Label(username_frame, text="Username:", bg="#F2EEE3", font=("Arial", 14))
username_label.pack(side=LEFT)
username_entry = Entry(username_frame, font=("Arial", 14))
username_entry.pack(side=LEFT, fill=X, expand=True)

# Password label and entry
password_frame = Frame(root, bg="#F2EEE3")
password_frame.pack(pady=10)
password_label = Label(password_frame, text="Password:", bg="#F2EEE3", font=("Arial", 14))
password_label.pack(side=LEFT)
password_entry = Entry(password_frame, show="*", font=("Arial", 14))
password_entry.pack(side=LEFT, fill=X, expand=True)

# Sign in button
sign_in_button = Button(root, text="SIGN IN", bg="#BCA0A0", font=("Arial", 14), command=sign_in)
sign_in_button.pack(pady=10)

# Message label
message_label = Label(root, text="", bg="#F2EEE3", fg="red", font=("Arial", 14))
message_label.pack(pady=10)

# Center and align elements
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Run the application
root.mainloop()