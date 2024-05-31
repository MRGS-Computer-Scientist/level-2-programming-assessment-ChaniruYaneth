from tkinter import *
from tkinter import ttk
import time
import csv

# Funtion to load stored credentials
def load_credentials():
    try:
        with open('credentials.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                username, password = row
                users[username] = password
        print("Credentials loaded successfully.")
        print("Loaded users:", users)  # Print loaded users for debugging
    except FileNotFoundError:
        print("Credentials file not found.")
        # Create an empty file if it doesn't exist
        with open('credentials.csv', mode='w', newline=''):
            pass
    except Exception as e:
        print("Error loading credentials:", e)

# File will be created when the first user signs up

# Funtion to save new credntials
def save_credentials(username, password):
    print("test", username, password)
    try:
        with open('credentials.csv', mode='a', newline='') as file:
            writer  = csv.writer(file)
            writer.writerow([username, password])
        print("Credentials saved successfully.")
    except Exception as e:
        print("Error saving credentials:", e)


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
                message_label. config(text="Signing you up...")
                create_account_window.after(1000, create_account_window.destroy)

        else:
            message_label.config(text="Passwords do not match. Please try again.")

        print("Test..")
        save_credentials(username_entry.get(), password_entry.get())

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
             message_label.config(text="You have successfully signed in. Enjoy Right Way!")
        else:
            message_label.config(text="Username or Password is invalid. Please enter again.")

# Function to exit the application
def exit_app():
    root.destroy()



# Create the main window
root = Tk()
root.title("Login Page")
root.geometry("800x550")
root.config(bg="#F2EEE3")

# Define users list to store credentials
users = {}

# Load stored credentials
load_credentials()
print("Loaded users:", users)  # Print loaded users for debugging

# Load logo image
logo_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\logo.png")

# Resize the logo image
resized_logo_image = logo_image.subsample(2, 2)

# Logo label
logo_label = Label(root, image=resized_logo_image, bg="#F2EEE3")
logo_label.pack(pady=(20, 20))

# Do not have an account label
no_account_label = Label(root, text="Do not have an account?", bg="#F2EEE3", font=("Arial", 14))
no_account_label.pack()

# Sign up button
sign_up_button = Button(root, text="SIGN UP", bg="#BCA0A0", font=("Arial", 14), command=create_account)
sign_up_button.pack(pady=20)

# Username label and entry
username_frame = Frame(root, bg="#F2EEE3")
username_frame.pack(pady=(20, 5))
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

# Exit button
exit_button = Button(root, text="Exit", bg="#BCA0A0", command=exit_app)
exit_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)  # Top-right corner


# Center and align elements
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

load_credentials()
print("Loaded users:", users)  # Print loaded users for debugging




# Function to show loading overlay
def show_loading(message):
    loading_overlay = Toplevel(main_interface)
    loading_overlay.geometry("800x550")
    loading_overlay.attributes('-alpha', 0.8)
    loading_overlay.config(bg="gray")
    loading_overlay.overrideredirect(1)

    loading_label = Label(loading_overlay, text=message, font=("Arial", 24), bg="gray", fg="white")
    loading_label.pack(pady=200)

    # Simulate a loading period
    main_interface.after(2000, loading_overlay.destroy)

# Function to open the main interface
def open_main_interface():
    global main_interface
    root.destroy()

    main_interface = Tk()
    main_interface.title("Right Way")
    main_interface.geometry("800x550")
    main_interface.config(bg="#F2EEE3")

    # Load logo image
    logo_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\logo.png")
    resized_logo_image = logo_image.subsample(2, 2)

    # Logo label
    logo_label = Label(main_interface, image=resized_logo_image, bg="#F2EEE3")
    logo_label.place(relx=0.5, y=30, anchor="n")

    # Logout button
    logout_button = Button(main_interface, text="Logout", bg="#BCA0A0", command=main_interface.destroy)
    logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)  # Top-right corner

    # Function to handle "click here" buttons
    def click_here(message):
        show_loading(f"Taking you to the {message} page")

    # Resources and Materials section
    resources_label = Label(main_interface, text="RESOURCES AND MATERIALS", bg="#F2EEE3", font=("Arial", 16, "bold"))
    resources_label.place(x=50, y=100)

    resources_desc = Label(main_interface, text="To help students further advance and excel in their studies, we offer various materials and resources to help enhance their experience.", bg="#F2EEE3", font=("Arial", 12))
    resources_desc.place(x=50, y=130)

    resources_button = Button(main_interface, text="Click here", bg="#BCA0A0", command=lambda: click_here("study resources"))
    resources_button.place(x=50, y=180)

    resources_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\resources.png")
    resources_label_img = Label(main_interface, image=resources_image, bg="#F2EEE3")
    resources_label_img.place(x=50, y=220)

    # Calendar section
    calendar_label = Label(main_interface, text="CALENDAR", bg="#F2EEE3", font=("Arial", 16, "bold"))
    calendar_label.place(x=450, y=100)

    calendar_desc = Label(main_interface, text="Organize your study schedule and never miss an important date with our calendar. Set reminders for exams, assignments, and events to stay on track and maximize productivity.", bg="#F2EEE3", font=("Arial", 12))
    calendar_desc.place(x=450, y=130)

    calendar_button = Button(main_interface, text="Click here", bg="#BCA0A0", command=lambda: click_here("calendar"))
    calendar_button.place(x=450, y=180)
    
    calendar_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\calendar.png")
    calendar_label_img = Label(main_interface, image=calendar_image, bg="#F2EEE3")
    calendar_label_img.place(x=450, y=220)




main_interface.mainloop()
root.mainloop()