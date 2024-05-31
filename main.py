from tkinter import *
from tkinter import ttk
import csv

# Function to load stored credentials
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

# Function to save new credentials
def save_credentials(username, password):
    print("test", username, password)
    try:
        with open('credentials.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print("Credentials saved successfully.")
    except Exception as e:
        print("Error saving credentials:", e)

# Function to create an account
def create_account():
    def submit():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        
        if password == confirm_password:
            if username in users:
                message_label.config(text="You already have an account. Please sign-in.")
            else:
                users[username] = password
                message_label.config(text="Signing you up...")
                create_account_window.after(1000, create_account_window.destroy)
                save_credentials(username, password)
        else:
            message_label.config(text="Passwords do not match. Please try again.")

    create_account_window = Toplevel(root)
    create_account_window.title("Create Account")
    create_account_window.geometry("500x300")
    create_account_window.config(bg="#F2EEE3")

    username_label = Label(create_account_window, text="Username:", bg="#F2EEE3", font=("Arial", 14))
    username_entry = Entry(create_account_window, font=("Arial", 14))

    password_label = Label(create_account_window, text="Password:", bg="#F2EEE3", font=("Arial", 14))
    password_entry = Entry(create_account_window, show="*", font=("Arial", 14))

    confirm_password_label = Label(create_account_window, text="Confirm Password:", bg="#F2EEE3", font=("Arial", 14))
    confirm_password_entry = Entry(create_account_window, show="*", font=("Arial", 14))

    submit_button = Button(create_account_window, text="Submit", bg="#BCA0A0", font=("Arial", 14), command=submit)

    message_label = Label(create_account_window, text="", bg="#F2EEE3", fg="red", font=("Arial", 12))

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
        message_label.config(text="You have successfully signed in. Enjoy Right Way!")
        root.after(1000, open_main_interface)
    else:
        message_label.config(text="Username or Password is invalid. Please enter again.")

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main window
root = Tk()
root.title("Login Page")
root.geometry("900x600")
root.config(bg="#F2EEE3")

users = {}

load_credentials()
print("Loaded users:", users)  # Print loaded users for debugging

logo_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\logo.png")
resized_logo_image = logo_image.subsample(2, 2)

logo_label = Label(root, image=resized_logo_image, bg="#F2EEE3")
logo_label.pack(pady=(20, 20))

no_account_label = Label(root, text="Do not have an account?", bg="#F2EEE3", font=("Arial", 14))
no_account_label.pack()

sign_up_button = Button(root, text="SIGN UP", bg="#BCA0A0", font=("Arial", 14), command=create_account)
sign_up_button.pack(pady=20)

username_frame = Frame(root, bg="#F2EEE3")
username_frame.pack(pady=(20, 5))
username_label = Label(username_frame, text="Username:", bg="#F2EEE3", font=("Arial", 14))
username_label.pack(side=LEFT)
username_entry = Entry(username_frame, font=("Arial", 14))
username_entry.pack(side=LEFT, fill=X, expand=True)

password_frame = Frame(root, bg="#F2EEE3")
password_frame.pack(pady=10)
password_label = Label(password_frame, text="Password:", bg="#F2EEE3", font=("Arial", 14))
password_label.pack(side=LEFT)
password_entry = Entry(password_frame, show="*", font=("Arial", 14))
password_entry.pack(side=LEFT, fill=X, expand=True)

sign_in_button = Button(root, text="SIGN IN", bg="#BCA0A0", font=("Arial", 14), command=sign_in)
sign_in_button.pack(pady=10)

message_label = Label(root, text="", bg="#F2EEE3", fg="red", font=("Arial", 14))
message_label.pack(pady=10)

exit_button = Button(root, text="Exit", bg="#BCA0A0", command=exit_app)
exit_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

def show_loading(message):
    loading_overlay = Toplevel(main_interface)
    loading_overlay.geometry("900x600")
    loading_overlay.attributes('-alpha', 0.8)
    loading_overlay.config(bg="gray")
    loading_overlay.overrideredirect(1)

    loading_label = Label(loading_overlay, text=message, font=("Arial", 24), bg="gray", fg="white")
    loading_label.pack(pady=200)

    main_interface.after(2000, loading_overlay.destroy)

def open_main_interface():
    global main_interface
    root.destroy()

    main_interface = Tk()
    main_interface.title("Right Way")
    main_interface.geometry("900x600")
    main_interface.config(bg="#F2EEE3")

    logo_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\logo.png")
    resized_logo_image = logo_image.subsample(2, 2)

    logo_label = Label(main_interface, image=resized_logo_image, bg="#F2EEE3")
    logo_label.place(relx=0.5, y=30, anchor="n")

    logout_button = Button(main_interface, text="Logout", bg="#BCA0A0", command=main_interface.destroy)
    logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

    def click_here(message):
        show_loading(f"Taking you to the {message} page")

    # Frame for resources and materials
    resources_frame = Frame(main_interface, bg="#F2EEE3", bd=2, relief="groove")
    resources_frame.place(x=50, y=120, width=360, height=200)

    resources_label = Label(resources_frame, text="RESOURCES AND MATERIALS", bg="#F2EEE3", font=("Arial", 11, "bold"))
    resources_label.pack(pady=(10, 0))

    resources_desc = Label(resources_frame, text="To help students further advance and excel in their studies, we offer various materials and resources to help enhance their experience.", bg="#F2EEE3", font=("Arial", 9), wraplength=350)
    resources_desc.pack(pady=10)

    resources_button = Button(resources_frame, text="Click here", bg="#BCA0A0", command=lambda: click_here("study resources"))
    resources_button.pack(pady=10)

    resources_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Pictures\PythonExercises-1\images\calendar.png")
    resources_label_img = Label(resources_frame, image=resources_image, bg="#F2EEE3")
    resources_label_img.pack(pady=10)

    # Frame for calendar
    calendar_frame = Frame(main_interface, bg="#F2EEE3", bd=2, relief="groove")
    calendar_frame.place(x=310, y=100, width=220, height=200)

    calendar_label = Label(calendar_frame, text="CALENDAR", bg="#F2EEE3", font=("Arial", 12, "bold"))
    calendar_label.pack(pady=(10, 0))

    calendar_desc = Label(calendar_frame, text="Organize your study schedule and never miss an important date with our calendar. Set reminders for exams, assignments, and events to stay on track and maximize productivity.", bg="#F2EEE3", font=("Arial", 10), wraplength=200)
    calendar_desc.pack(pady=10)

    calendar_button = Button(calendar_frame, text="Click here", bg="#BCA0A0", command=lambda: click_here("calendar"))
    calendar_button.pack(pady=10)

    calendar_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\calendar.png")
    calendar_label_img = Label(calendar_frame, image=calendar_image, bg="#F2EEE3")
    calendar_label_img.pack(pady=10)

    # Frame for career advice
    advice_frame = Frame(main_interface, bg="#F2EEE3", bd=2, relief="groove")
    advice_frame.place(x=570, y=100, width=220, height=200)

    advice_label = Label(advice_frame, text="CAREER ADVICE", bg="#F2EEE3", font=("Arial", 12, "bold"))
    advice_label.pack(pady=(10, 0))

    advice_desc = Label(advice_frame, text="Get valuable career advice to guide your study efforts effectively. Our resources help you plan and achieve your career goals.", bg="#F2EEE3", font=("Arial", 10), wraplength=200)
    advice_desc.pack(pady=10)

    advice_button = Button(advice_frame, text="Click here", bg="#BCA0A0", command=lambda: click_here("career advice"))
    advice_button.pack(pady=10)

    advice_image = PhotoImage(file=r"C:\Users\yanet\OneDrive\Desktop\Development\PythonExercises-1\images\advice.png")
    advice_label_img = Label(advice_frame, image=advice_image, bg="#F2EEE3")
    advice_label_img.pack(pady=10)

    main_interface.mainloop()

root.mainloop()
