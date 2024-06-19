from tkinter import *
from tkinter import ttk, messagebox
import time
import csv
import os

# Function to load stored credentials
def load_credentials():
    try:
        with open('credentials.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                username, password = row
                users[username] = password
        print("Credentials loaded successfully.")
    except FileNotFoundError:
        print("Credentials file not found.")
        with open('credentials.csv', mode='w', newline=''):
            pass
    except Exception as e:
        print("Error loading credentials:", e)

# Function to save new credentials
def save_credentials(username, password):
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

    password_label = Label(create_account_window, text="Password", bg="#F2EEE3", font=("Arial", 14))
    password_entry = Entry(create_account_window, show="*", font=("Arial", 14))

    confirm_password_label = Label(create_account_window, text="Confirm Password", bg="#F2EEE3", font=("Arial", 14))
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

# Function to center a window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to confirm exit
def confirm_exit():
    center_window(root, 1100, 800)
    if messagebox.askyesno("Exit", "Are you sure you want to exit Right Way?"):
        root.destroy()

# Create the main window
root = Tk()
root.title("Login Page")
root.geometry("1100x900")
root.config(bg="#F2EEE3")

users = {}
load_credentials()

# Center the root window
center_window(root, 1100, 800)

# Updated paths to use the relative path to the images folder
logo_image_path = os.path.join(os.path.dirname(__file__), 'images', 'logo.png')
logo_image = PhotoImage(file=logo_image_path)
resized_logo_image = logo_image.subsample(2, 2)

logo_label = Label(root, image=resized_logo_image, bg="#F2EEE3")
logo_label.pack(pady=(20, 20))

no_account_label = Label(root, text="Do not have an account?", bg="#F2EEE3", font=("Arial", 14))
no_account_label.pack(pady=20)

sign_up_button = Button(root, text="SIGN UP", bg="#BCA0A0", font=("Arial", 14), command=create_account)
sign_up_button.pack(pady=15)

username_frame = Frame(root, bg="#F2EEE3")
username_frame.pack(pady=(50, 10))
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

exit_button = Button(root, text="Exit", bg="#BCA0A0", command=confirm_exit)
exit_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

def show_loading(message):
    loading_overlay = Toplevel(main_interface)
    loading_overlay.geometry("1100x900")
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
    main_interface.geometry("1100x950")
    main_interface.config(bg="#F2EEE3")

    # Center the main interface window
    center_window(main_interface, 1100, 900)

    # Store images in a dictionary to keep references
    images = {}

    logo_image_path = os.path.join(os.path.dirname(__file__), 'images', 'logo.png')
    images['logo_image'] = PhotoImage(file=logo_image_path)
    resized_logo_image = images['logo_image'].subsample(2, 2)

    logo_label = Label(main_interface, image=resized_logo_image, bg="#F2EEE3")
    logo_label.pack(pady=(10, 10))

    # Function to confirm logout
    def confirm_logout():
        center_window(main_interface, 1100, 900)
        if messagebox.askyesno("Logout", "Are you sure you want to log out from Right Way?"):
            main_interface.destroy()

    logout_button = Button(main_interface, text="Logout", bg="#BCA0A0", command=confirm_logout)
    logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

    def click_here(message):
        show_loading(f"Taking you to the {message} page")
        main_interface.after(2000, open_resources_page)

    # Frame for resources and materials
    resources_frame = Frame(main_interface, bg="#F2EEE3", bd=2, relief="groove")
    resources_frame.pack(padx=20, pady=20, fill="x")

    resources_label = Label(resources_frame, text="RESOURCES AND MATERIALS", bg="#F2EEE3", font=("Arial", 14, "bold"), anchor="w", justify="left")
    resources_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    resources_desc = Label(resources_frame, text="Our resources section offers a variety of materials to help you excel in your studies. Access textbooks, study guides, and more.", bg="#F2EEE3", font=("Arial", 12), wraplength=550, anchor="w", justify="left")
    resources_desc.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    resources_button = Button(resources_frame, text="Click here", bg="#BCA0A0", command=lambda: click_here("resources"))
    resources_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    resources_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Books.png')
    images['resources_image'] = PhotoImage(file=resources_image_path)
    resources_label_img = Label(resources_frame, image=images['resources_image'], bg="#F2EEE3")
    resources_label_img.grid(row=0, column=1, rowspan=3, padx=50, pady=10)

    # Frame for calendar
    calendar_frame = Frame(main_interface, bg="#F2EEE3", bd=2, relief="groove")
    calendar_frame.pack(padx=20, pady=10, fill="x")

    calendar_label = Label(calendar_frame, text="CALENDAR", bg="#F2EEE3", font=("Arial", 14, "bold"), anchor="w", justify="left")
    calendar_label.grid(row=0, column=1, padx=85, pady=10, sticky="w")

    calendar_desc = Label(calendar_frame, text="Keep track of important dates and events with our integrated calendar. Stay organized and never miss a deadline.", bg="#F2EEE3", font=("Arial", 12), wraplength=550, anchor="w", justify="left")
    calendar_desc.grid(row=1, column=1, padx=85, pady=10, sticky="w")

    calendar_button = Button(calendar_frame, text="Click here", bg="#BCA0A0", command=lambda: click_here("calendar"))
    calendar_button.grid(row=2, column=1, padx=85, pady=10, sticky="w")

    calendar_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Calendar.png')
    images['calendar_image'] = PhotoImage(file=calendar_image_path)
    calendar_label_img = Label(calendar_frame, image=images['calendar_image'], bg="#F2EEE3")
    calendar_label_img.grid(row=0, column=0, rowspan=3, padx=50, pady=10)

    # Frame for career advice
    career_frame = Frame(main_interface, bg="#F2EEE3", bd=2, relief="groove")
    career_frame.pack(padx=20, pady=10, fill="x")

    career_label = Label(career_frame, text="CAREER ADVICE", bg="#F2EEE3", font=("Arial", 14, "bold"), anchor="w", justify="left")
    career_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    career_desc = Label(career_frame, text="Our career advice section offers guidance to help you make informed decisions about your future career path. Get tips and advice from professionals.", bg="#F2EEE3", font=("Arial", 12), wraplength=550, anchor="w", justify="left")
    career_desc.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    career_button = Button(career_frame, text="Click here", bg="#BCA0A0", command=lambda: click_here("career advice"))
    career_button.grid(row=2, column=0, padx=10, pady=2, sticky="w")

    career_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Career Advice Girl.png')
    images['career_image'] = PhotoImage(file=career_image_path)
    career_label_img = Label(career_frame, image=images['career_image'], bg="#F2EEE3")
    career_label_img.grid(row=0, column=1, rowspan=3, padx=20, pady=10)

    main_interface.mainloop()

def open_resources_page():
    resources_page = Toplevel(main_interface)
    resources_page.title("Resources and Materials")
    resources_page.geometry("1100x900")
    resources_page.config(bg="#F2EEE3")
    center_window(resources_page, 1100, 900)

    logo_label = Label(resources_page, image=resized_logo_image, bg="#F2EEE3")
    logo_label.pack(pady=(10, 10))

    logout_button = Button(resources_page, text="Logout", bg="#BCA0A0", command=confirm_logout)
    logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

    resources_desc_label = Label(resources_page, text="Find resources and materials for your NCEA Level 2 subjects below.", bg="#F2EEE3", font=("Arial", 14), wraplength=600, anchor="w", justify="left")
    resources_desc_label.pack(pady=(20, 10))

    search_bar_frame = Frame(resources_page, bg="#F2EEE3")
    search_bar_frame.pack(pady=(10, 10))
    search_bar_label = Label(search_bar_frame, text="Search:", bg="#F2EEE3", font=("Arial", 14))
    search_bar_label.pack(side=LEFT, padx=(10, 5))
    search_bar_entry = Entry(search_bar_frame, font=("Arial", 14))
    search_bar_entry.pack(side=LEFT, fill=X, expand=True)

    resources_girl_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Resources Girl.png')
    resources_girl_image = PhotoImage(file=resources_girl_image_path)

    resources_girl_label = Label(root, image=resources_girl_image, bg="#F2EEE3")
    resources_girl_label.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

    # Function for handling search bar input
    def on_search_input(event):
        query = search_bar_entry.get().lower()
        suggestions = [subject for subject in subjects if query in subject.lower()]
        update_suggestions(suggestions)

    search_bar_entry.bind("<KeyRelease>", on_search_input)

    # Listbox to display search suggestions
    suggestions_listbox = Listbox(resources_page, font=("Arial", 14), bg="#F2EEE3")
    suggestions_listbox.pack(pady=(10, 10), padx=20, fill=X)

    # Function to update suggestion list
    def update_suggestions(suggestions):
        suggestions_listbox.delete(0, END)
        for suggestion in suggestions:
            suggestions_listbox.insert(END, suggestion)

    subjects = ["Accounting", "Economics", "English", "Maths", "Chemistry", "Physics", "Biology"]

    # Function to open a new window with exam links
    def open_exam_links(subject):
        exam_links_page = Toplevel(resources_page)
        exam_links_page.title(f"{subject} Exams")
        exam_links_page.geometry("600x400")
        exam_links_page.config(bg="#F2EEE3")
        center_window(exam_links_page, 600, 400)

        internal_label = Label(exam_links_page, text=f"Internal Exams - {subject}", bg="#F2EEE3", font=("Arial", 14))
        internal_label.pack(pady=(20, 10))
        internal_link = Label(exam_links_page, text="Click here for Internal Exams", bg="#F2EEE3", font=("Arial", 12), fg="blue", cursor="hand2")
        internal_link.pack(pady=(5, 5))
        internal_link.bind("<Button-1>", lambda e: open_web_link(internal_links[subject]))

        external_label = Label(exam_links_page, text=f"External Exams - {subject}", bg="#F2EEE3", font=("Arial", 14))
        external_label.pack(pady=(20, 10))
        external_link = Label(exam_links_page, text="Click here for External Exams", bg="#F2EEE3", font=("Arial", 12), fg="blue", cursor="hand2")
        external_link.pack(pady=(5, 5))
        external_link.bind("<Button-1>", lambda e: open_web_link(external_links[subject]))

    # Function to open web link in browser
    def open_web_link(url):
        import webbrowser
        webbrowser.open(url)

    # Dictionaries to store exam links (to be provided)
    internal_links = {
        "Accounting": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=accounting&view=exams&level=02",
        "Economics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=economics&view=files&level=02",
        "English": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=english&view=exams&level=02",
        "Maths": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=math&view=exams&level=02",
        "Chemistry": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=chemistry&view=exams&level=02",
        "Physics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=physics&view=exams&level=02",
        "Biology": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=biology&view=exams&level=02"
    }

    external_links = {
        "Accounting": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=accounting&view=exams&level=02",
        "Economics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=economics&view=files&level=02",
        "English": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=english&view=exams&level=02",
        "Maths": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=math&view=exams&level=02",
        "Chemistry": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=chemistry&view=exams&level=02",
        "Physics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=physics&view=exams&level=02",
        "Biology": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=biology&view=exams&level=02"
    }

    # Function to handle suggestion selection
    def on_suggestion_select(event):
        selected_subject = suggestions_listbox.get(suggestions_listbox.curselection())
        open_exam_links(selected_subject)

    suggestions_listbox.bind("<<ListboxSelect>>", on_suggestion_select)

root.mainloop()
