from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import tkinter as tk
import time
import csv
import calendar
import json
import os

class App():

    users = {}

    def __init__(self):
        self.root = Tk()
        self.root.title("Login Page")
        self.root.geometry("1100x900")
        self.root.config(bg="#F2EEE3")

        self.load_credentials()

        # Center the root window
        self.center_window(self.root, 1100, 800)

        # Updated paths to use the relative path to the images folder
        logo_image_path = os.path.join(os.path.dirname(__file__), 'images', 'logo.png')
        logo_image = PhotoImage(file=logo_image_path)
        resized_logo_image = logo_image.subsample(2, 2)

        self.logo_label = Label(self.root, image=resized_logo_image, bg="#F2EEE3")
        self.logo_label.pack(pady=(20, 20))

        self.no_account_label = Label(self.root, text="Do not have an account?", bg="#F2EEE3", font=("Arial", 14))
        self.no_account_label.pack(pady=20)

        self.sign_up_button = Button(self.root, text="SIGN UP", bg="#BCA0A0", font=("Arial", 14), command=self.create_account)
        self.sign_up_button.pack(pady=15)

        self.username_frame = Frame(self.root, bg="#F2EEE3")
        self.username_frame.pack(pady=(50, 10))
        self.username_label = Label(self.username_frame, text="Username:", bg="#F2EEE3", font=("Arial", 14))
        self.username_label.pack(side=LEFT)
        self.username_entry = Entry(self.username_frame, font=("Arial", 14))
        self.username_entry.pack(side=LEFT, fill=X, expand=True)

        self.password_frame = Frame(self.root, bg="#F2EEE3")
        self.password_frame.pack(pady=10)
        self.password_label = Label(self.password_frame, text="Password:", bg="#F2EEE3", font=("Arial", 14))
        self.password_label.pack(side=LEFT)
        self.password_entry = Entry(self.password_frame, show="*", font=("Arial", 14))
        self.password_entry.pack(side=LEFT, fill=X, expand=True)

        self.sign_in_button = Button(self.root, text="SIGN IN", bg="#BCA0A0", font=("Arial", 14), command=self.sign_in)
        self.sign_in_button.pack(pady=10)

        self.message_label = Label(self.root, text="", bg="#F2EEE3", fg="red", font=("Arial", 14))
        self.message_label.pack(pady=10)

        self.exit_button = Button(self.root, text="Exit", bg="#BCA0A0", command=self.confirm_exit)
        self.exit_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.root.mainloop()

    # Function to load stored credentials
    def load_credentials(self):
        try:
            with open('credentials.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, password = row
                    self.users[username] = password
            print("Credentials loaded successfully.")
        except FileNotFoundError:
            print("Credentials file not found.")
            with open('credentials.csv', mode='w', newline=''):
                pass
        except Exception as e:
            print("Error loading credentials:", e)

    # Function to save new credentials
    def save_credentials(self, username, password):
        try:
            with open('credentials.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password])
            print("Credentials saved successfully.")
        except Exception as e:
            print("Error saving credentials:", e)

    # Function to create an account
    def create_account(self):
        def submit():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            
            if password == confirm_password:
                if username in self.users:
                    message_label.config(text="You already have an account. Please sign-in.")
                else:
                    self.users[username] = password
                    message_label.config(text="Signing you up...")
                    create_account_window.after(1000, create_account_window.destroy)
                    self.save_credentials(username, password)
            else:
                message_label.config(text="Passwords do not match. Please try again.")

        create_account_window = Toplevel(self.root)
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
    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        #TODO: Add a check for the length of the username

        if username in self.users and self.users[username] == password:
            self.message_label.config(text="You have successfully signed in. Enjoy Right Way!")
            self.root.after(1000, self.open_main_interface)
        else:
            self.message_label.config(text="Username or Password is invalid. Please enter again.")

    # Function to center a window
    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        window.geometry(f'{width}x{height}+{x}+{y}')

    # Function to confirm exit
    def confirm_exit(self):
        self.center_window(self.root, 1100, 800)
        if messagebox.askyesno("Exit", "Are you sure you want to exit Right Way?"):
            self.root.destroy()



    #### MAIN INTERFACE ####

    # Function to confirm logout
    def confirm_logout(self):
        self.center_window(self.main_interface, 1100, 900)
        if messagebox.askyesno("Logout", "Are you sure you want to log out from Right Way?"):
            self.main_interface.destroy()

    def click_here(self,message):
        self.show_loading(f"Taking you to the {message} page", 1000)

        if message == "resource":
            self.main_interface.after(2000, self.open_resources_page)
            #time.sleep(2)
            #self.open_resources_page()
        elif message == "calendar":
            self.main_interface.after(2000, self.open_calendar_page)
            #time.sleep(2)
            #self.open_resources_page()


    # Function to show a loading message
    def show_loading(self, message, delay):
        loading_window = Toplevel(self.main_interface)
        loading_window.title("Loading")
        loading_window.geometry("300x100")
        loading_window.config(bg="white")

        self.center_window(loading_window, 300, 100)

        message_label = Label(loading_window, text=message, bg="white", font=("Arial", 10))
        message_label.pack(pady=20)

        self.main_interface.after(delay, loading_window.destroy)
        

    def open_main_interface(self):
        self.root.destroy()

        self.main_interface = Tk()
        self.main_interface.title("Right Way")
        self.main_interface.geometry("1100x950")
        self.main_interface.config(bg="#F2EEE3")

        # Center the main interface window
        self.center_window(self.main_interface, 1100, 900)

        # Store images in a dictionary to keep references
        self.images = {}

        self.logo_image_path = os.path.join(os.path.dirname(__file__), 'images', 'logo.png')
        self.images['logo_image'] = PhotoImage(file=self.logo_image_path)
        self.resized_logo_image = self.images['logo_image'].subsample(2, 2)

        self.logo_label = Label(self.main_interface, image=self.resized_logo_image, bg="#F2EEE3")
        self.logo_label.pack(pady=(10, 10))

        self.logout_button = Button(self.main_interface, text="Logout", bg="#BCA0A0", command=self.confirm_logout)
        self.logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

        # Frame for resources and materials
        self.resources_frame = Frame(self.main_interface, bg="#F2EEE3", bd=2, relief="groove")
        self.resources_frame.pack(padx=20, pady=20, fill="x")


        self.resources_label = Label(self.resources_frame, text="RESOURCES AND MATERIALS", bg="#F2EEE3", font=("Arial", 14, "bold"), anchor="w", justify="left")
        self.resources_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")


        self.resources_desc = Label(self.resources_frame, text="Our resources section offers a variety of materials to help you excel in your studies. Access textbooks, study guides, and more.", bg="#F2EEE3", font=("Arial", 12), wraplength=550, anchor="w", justify="left")
        self.resources_desc.grid(row=1, column=0, padx=10, pady=10, sticky="w")


        self.resources_button = Button(self.resources_frame, text="Click here", bg="#BCA0A0", command=lambda: self.click_here("resource"))
        self.resources_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.resources_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Books.png')
        self.images['resources_image'] = PhotoImage(file=self.resources_image_path)
        self.resources_label_img = Label(self.resources_frame, image=self.images['resources_image'], bg="#F2EEE3")
        self.resources_label_img.grid(row=0, column=1, rowspan=3, padx=50, pady=10)


        # Frame for calendar
        self.calendar_frame = Frame(self.main_interface, bg="#F2EEE3", bd=2, relief="groove")
        self.calendar_frame.pack(padx=20, pady=10, fill="x")


        self.calendar_label = Label(self.calendar_frame, text="CALENDAR", bg="#F2EEE3", font=("Arial", 14, "bold"), anchor="w", justify="left")
        self.calendar_label.grid(row=0, column=1, padx=85, pady=10, sticky="w")


        self.calendar_desc = Label(self.calendar_frame, text="Keep track of important dates and events with our integrated calendar. Stay organized and never miss a deadline.", bg="#F2EEE3", font=("Arial", 12), wraplength=550, anchor="w", justify="left")
        self.calendar_desc.grid(row=1, column=1, padx=85, pady=10, sticky="w")


        self.calendar_button = Button(self.calendar_frame, text="Click here", bg="#BCA0A0", command=lambda: self.click_here("calendar"))
        self.calendar_button.grid(row=2, column=1, padx=85, pady=10, sticky="w")


        self.calendar_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Calendar.png')
        self.images['calendar_image'] = PhotoImage(file=self.calendar_image_path)
        self.calendar_label_img = Label(self.calendar_frame, image=self.images['calendar_image'], bg="#F2EEE3")
        self.calendar_label_img.grid(row=0, column=0, rowspan=3, padx=50, pady=10)

        # Frame for career adviceself.
        self.career_frame = Frame(self.main_interface, bg="#F2EEE3", bd=2, relief="groove")
        self.career_frame.pack(padx=20, pady=10, fill="x")


        self.career_label = Label(self.career_frame, text="CAREER ADVICE", bg="#F2EEE3", font=("Arial", 14, "bold"), anchor="w", justify="left")
        self.career_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")


        self.career_desc = Label(self.career_frame, text="Our career advice section offers guidance to help you make informed decisions about your future career path. Get tips and advice from professionals.", bg="#F2EEE3", font=("Arial", 12), wraplength=550, anchor="w", justify="left")
        self.career_desc.grid(row=1, column=0, padx=10, pady=10, sticky="w")


        self.career_button = Button(self.career_frame, text="Click here", bg="#BCA0A0", command=lambda: self.click_here("career advice"))
        self.career_button.grid(row=2, column=0, padx=10, pady=2, sticky="w")


        self.career_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Career Advice Girl.png')
        self.images['career_image'] = PhotoImage(file=self.career_image_path)
        self.career_label_img = Label(self.career_frame, image=self.images['career_image'], bg="#F2EEE3")
        self.career_label_img.grid(row=0, column=1, rowspan=3, padx=20, pady=10)

        self.main_interface.mainloop()


    #### RESOURCES AND MATERIALS ####

    def open_resources_page(self):
        print("Opening resource page")
        self.resources_page = Toplevel(self.main_interface)
        self.resources_page.title("Resources and Materials")
        self.resources_page.geometry("1100x900")
        self.resources_page.config(bg="#F2EEE3")
        self.center_window(self.resources_page, 1100, 900)

        logo_label = Label(self.resources_page, image=self.resized_logo_image, bg="#F2EEE3")
        logo_label.pack(pady=(10, 10))

        logout_button = Button(self.resources_page, text="Logout", bg="#BCA0A0", command=self.confirm_logout)
        logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

        resources_desc_label = Label(self.resources_page, text="CLICK ON THE SEARCH BAR VISIBLE, AND SELECT THE SUBJECT YOU REQUIRE ASSISTANCE.\n\nHELP YOURSELVES BY GOING THROUGH WHAT THE SUBJECT OFFERS YOU FOR LEVEL TWO AND WE WISH YOU GOOD LUCK WITH YOUR STUDIES...", bg="#F2EEE3", font=("Arial", 12), wraplength=950, anchor="w", justify="left")
        resources_desc_label.pack(pady=(20, 10))

        search_bar_frame = Frame(self.resources_page, bg="#F2EEE3")
        search_bar_frame.pack(pady=(10, 10))
        search_bar_label = Label(search_bar_frame, text="Search:", bg="#F2EEE3", font=("Arial", 14))
        search_bar_label.pack(side=LEFT, padx=(10, 5))
        search_bar_entry = Entry(search_bar_frame, font=("Arial", 14))
        search_bar_entry.pack(side=LEFT, fill=X, expand=True)

        # Function for handling search bar input
        def on_search_input(event):
            query = search_bar_entry.get().lower()
            suggestions = [subject for subject in self.subjects if query in subject.lower()]
            update_suggestions(suggestions)

        search_bar_entry.bind("<KeyRelease>", on_search_input)

        # Listbox to display search suggestions
        suggestions_listbox = Listbox(self.resources_page, font=("Arial", 14), bg="#F2EEE3", width=50)  # Reduced width to 50
        suggestions_listbox.pack(pady=(10, 10), padx=20, fill=X)

        # Function to update suggestion list
        def update_suggestions(suggestions):
            suggestions_listbox.delete(0, END)
            for suggestion in suggestions:
                suggestions_listbox.insert(END, suggestion)

        # Function to handle suggestion selection
        def on_suggestion_select(event):
            selected_subject = suggestions_listbox.get(suggestions_listbox.curselection())
            self.open_exam_links(selected_subject)

        suggestions_listbox.bind("<<ListboxSelect>>", on_suggestion_select)

        # Add subject list
        self.subjects = ["Accounting", "Economics", "English", "Maths", "Chemistry", "Physics", "Biology"]

        self.internal_links = {
            "Accounting": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=accounting&view=exams&level=02",
            "Economics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=economics&view=files&level=02",
            "English": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=english&view=exams&level=02",
            "Maths": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=math&view=exams&level=02",
            "Chemistry": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=chemistry&view=exams&level=02",
            "Physics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=physics&view=exams&level=02",
            "Biology": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=biology&view=exams&level=02"
        }

        self.external_links = {
            "Accounting": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=accounting&view=exams&level=02",
            "Economics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=economics&view=files&level=02",
            "English": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=english&view=exams&level=02",
            "Maths": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=math&view=exams&level=02",
            "Chemistry": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=chemistry&view=exams&level=02",
            "Physics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=physics&view=exams&level=02",
            "Biology": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=biology&view=exams&level=02"
        }

        # Load and display the image on the right side
        self.image_path = "images/Resources Girl.png"
        self.resource_image = PhotoImage(file=self.image_path)
        image_label = Label(self.resources_page, image=self.resource_image, bg="#F2EEE3")
        image_label.pack(side=RIGHT, padx=(10, 20), pady=(10, 20))

        

        # Function to open exam links
    def open_exam_links(self, subject):
            if subject in self.internal_links:
                link = self.internal_links[subject]
                # open the link in a browser
                import webbrowser
                webbrowser.open(link)
            else:
                messagebox.showerror("Error", "No links available for the selected subject.")



### Calendar Page ###

    def open_calendar_page(self):
        print("Opening calendar page")
        self.calendar_page = tk.Toplevel(self.main_interface)
        self.calendar_page.title("Calendar")
        self.calendar_page.geometry("1100x900")
        self.calendar_page.config(bg="#F2EEE3")
        self.center_window(self.calendar_page, 1100, 900)

        logo_label = tk.Label(self.calendar_page, image=self.resized_logo_image, bg="#F2EEE3")
        logo_label.pack(pady=(10, 10))

        logout_button = tk.Button(self.calendar_page, text="Logout", bg="#BCA0A0", command=self.confirm_logout)
        logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

        calendar_desc_label = tk.Label(self.calendar_page, text="USE OUR CALENDAR FUNCTIONALITY TO SET IMPORTANT EVENTS BY CLICKING ON DATES. IT ALLOWS ACCOMMODATES THE FACILITIES TO ADD, REMOVE OR EDIT REMINDERS.\n\nFURTHERMORE, ALLOWING YOU TO CALCULATE THE REMAINING TIME FOR CERTAIN EVENTS ENABLING YOU TO PLAN AND MANAGE TIME EFFICIENTLY.", bg="#F2EEE3", font=("Arial", 12), wraplength=950, anchor="w", justify="left")
        calendar_desc_label.pack(pady=(20, 10))



if __name__ == "__main__":
    app = App()
    