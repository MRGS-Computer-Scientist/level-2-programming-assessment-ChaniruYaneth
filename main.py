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

        self.logo_label = tk.Label(self.calendar_page, image=self.resized_logo_image, bg="#F2EEE3")
        self.logo_label.pack(pady=(10, 10))

        self.logout_button = tk.Button(self.calendar_page, text="Logout", bg="#BCA0A0", command=self.confirm_logout)
        self.logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

        self.calendar_desc_label = tk.Label(self.calendar_page, text="USE OUR CALENDAR FUNCTIONALITY TO SET IMPORTANT EVENTS BY CLICKING ON DATES. IT ALLOWS ACCOMMODATES THE FACILITIES TO ADD, REMOVE OR EDIT REMINDERS.\n\nFURTHERMORE, ALLOWING YOU TO CALCULATE THE REMAINING TIME FOR CERTAIN EVENTS ENABLING YOU TO PLAN AND MANAGE TIME EFFICIENTLY.", bg="#F2EEE3", font=("Arial", 12), wraplength=950, anchor="w", justify="left")
        self.calendar_desc_label.pack(pady=(20, 10))

        # Frame for year and month input
        self.input_frame = tk.Frame(self.calendar_page)
        self.input_frame.pack(pady=20)


        # Entry field for year
        tk.Label(self.input_frame, text="Year:").grid(row=0, column=0)
        self.year_entry = tk.Entry(self.input_frame)
        self.year_entry.insert(END, datetime.now().year)
        self.year_entry.grid(row=0, column=1)


        # Combobox for month selection
        tk.Label(self.input_frame, text="Month:").grid(row=0, column=2)
        self.month_combobox = ttk.Combobox(self.input_frame, values=list(range(1, 13)))
        self.month_combobox.grid(row=0, column=3)
        self.month_combobox.current(datetime.today().month - 1)  # Set default value to the current month


        # Button to display calendar
        self.display_button = tk.Button(self.input_frame, text="Display Calendar", command=self.display_calendar)
        self.display_button.grid(row=0, column=4, padx=10)


        # Frame for displaying calendar
        self.days_frame = tk.Frame(self.calendar_page, bg="lightblue")
        self.days_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)


        # Dictionary to store reminders
        self.reminders = {}
        self.load_reminders()  # Load reminders from file

# Function to save reminders to a JSON file
    def save_reminders(self):
        with open("reminders.json", "w") as file:
            json.dump(self.reminders, file)


    # Function to load reminders from a JSON file
    def load_reminders(self):
        global reminders
        if os.path.exists("reminders.json"):
            with open("reminders.json", "r") as file:
                self.reminders = json.load(file)
                # Convert any single reminder strings to lists
                self.reminders = {k: [v] if isinstance(v, str) else v for k, v in self.reminders.items()}
        else:
            self.reminders = {}


    def display_calendar(self):
        year = self.year_entry.get().strip()
        month = self.month_combobox.get().strip()


        # Check if year and month are provided
        if not year or not month:
            tk.messagebox.showerror("Error", "Please enter both year and select month.")
            return


        try:
            year = int(year)
            month = int(month)
        except ValueError:
            tk.messagebox.showerror("Error", "Year and month must be integers.")
            return


        # Clear any existing calendar display
        for widget in self.days_frame.winfo_children():
            widget.destroy()


        # Create a calendar object
        cal = calendar.monthcalendar(year, month)


        # Create labels to display the days of the week
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(days):
            tk.Label(self.days_frame, text=day, width=12, font=('Arial', 10, 'bold'), bg="lightblue", relief="solid").grid(row=0, column=i, padx=10, pady=1)


        # Display the calendar data
        today = datetime.today()
        for week_num, week in enumerate(cal, start=1):
            for day_num, day in enumerate(week):
                if day != 0:
                    # Determine the color of the label based on the day
                    if day_num in (5, 6):  # Weekend (Saturday and Sunday)
                        label_color = 'red'
                    else:
                        label_color = 'black'


                    # Highlight current day
                    if year == today.year and month == today.month and day == today.day:
                        label_bg = 'yellow'
                    else:
                        label_bg = 'white'


                    # Check for reminders
                    date_key = f"{year}-{month}-{day}"
                    reminder_texts = self.reminders.get(date_key, [])


                    # Create a label for the date
                    date_label = tk.Label(self.days_frame, text=f"{day}\n{', '.join(reminder_texts)}", width=12, height=5, font=('Arial', 10), fg=label_color, bg=label_bg, relief="ridge", bd=1, justify=tk.LEFT)
                    date_label.grid(row=week_num, column=day_num, padx=1, pady=1)


                    # Bind click event to each date label (left-click for touch, right-click for context menu)
                    date_label.bind("<Button-1>", lambda event, d=day, m=month, y=year, r=reminder_texts: self.open_reminder_menu(event, d, m, y, r))
                    date_label.bind("<Button-3>", lambda event, d=day, m=month, y=year, r=reminder_texts: self.open_reminder_menu(event, d, m, y, r))


    def open_reminder_menu(self, event, day, month, year, reminders):
        self.menu = tk.Menu(self.calendar_page, tearoff=0)


        if not self.reminders:
            self.menu.add_command(label="Set Reminder", command=lambda: self.set_reminder_window(day, month, year))
        else:
            for reminder in self.reminders:
                self.menu.add_command(label=reminder, command=lambda r=reminder: self.confirm_remove_reminder(day, month, year, r))


            self.menu.add_separator()
            self.menu.add_command(label="Add Reminder", command=lambda: self.set_reminder_window(day, month, year))
            self.menu.add_command(label="Cancel")


        try:
            self.menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.menu.grab_release()


    def confirm_remove_reminder(self, day, month, year, reminder_text):
        confirm = messagebox.askyesno("Confirm Remove", "Remove existing reminder?")
        if confirm:
            remove_reminder(day, month, year, reminder_text)


    def remove_reminder(self, day, month, year, reminder_text):
        date_key = f"{year}-{month}-{day}"
        if date_key in self.reminders:
            reminders[date_key].remove(reminder_text)
            if not reminders[date_key]:
                del reminders[date_key]
            self.save_reminders()
            self.display_calendar()  # Refresh calendar to update reminder display


    def set_reminder_window(self, day, month, year, reminder_text=""):
        # Create a new Tkinter window for setting reminders
        self.reminder_window = tk.Toplevel(self.calendar_page)
        self.reminder_window.title(f"Set Reminder - {day}/{month}/{year}")


        # Label for selected date
        tk.Label(self.reminder_window, text=f"Set Reminder for {day}/{month}/{year}", font=('Arial', 12)).pack()


        # Entry field for setting reminder
        self.reminder_entry = tk.Entry(self.reminder_window, width=30)
        self.reminder_entry.insert(0, reminder_text)
        self.reminder_entry.pack()

        # Button to set reminder
        self.set_button = tk.Button(self.reminder_window, text="Set Reminder", command=lambda: self.set_reminder(year, month, day))
        self.set_button.pack()

        # Button to close the reminder window
        self.close_button = tk.Button(self.reminder_window, text="Back", command=self.reminder_window.destroy)
        self.close_button.pack()


    # Function to set reminder
    def set_reminder(self, year, month, day):

        reminder_text = self.reminder_entry.get().strip()
        if reminder_text:
            date_key = f"{year}-{month}-{day}"
            if date_key in self.reminders:
                self.reminders[date_key].append(reminder_text)
            else:
                self.reminders[date_key] = [reminder_text]
            self.save_reminders()
            # Close the reminder window
            self.reminder_window.destroy()
            self.display_calendar()  # Refresh calendar to update reminder display
        else:
            tk.messagebox.showerror("Error", "Reminder cannot be empty.")


        

if __name__ == "__main__":
    app = App()
    