import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime
import json
import os

# Function to save reminders to a JSON file
def save_reminders():
    with open("reminders.json", "w") as file:
        json.dump(reminders, file)

# Function to load reminders from a JSON file
def load_reminders():
    global reminders
    if os.path.exists("reminders.json"):
        with open("reminders.json", "r") as file:
            reminders = json.load(file)
    else:
        reminders = {}

def display_calendar(year=None, month=None):
    global calendar_window, days_frame

    # Get the current year and month if not provided
    if year is None or month is None:
        year = int(year_entry.get())
        month = int(month_combobox.get())

    # Create a calendar object
    cal = calendar.monthcalendar(year, month)

    # Create or update the calendar window
    if 'calendar_window' in globals() and calendar_window.winfo_exists():
        calendar_window.destroy()

    calendar_window = tk.Toplevel(root)
    calendar_window.title(f"Calendar - {calendar.month_name[month]} {year}")
    calendar_window.geometry("800x600")

    # Create a frame for the navigation and calendar
    main_frame = tk.Frame(calendar_window, bg="lightblue")
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Create navigation buttons
    nav_frame = tk.Frame(main_frame, bg="lightblue")
    nav_frame.pack(pady=10)

    prev_month_button = tk.Button(nav_frame, text="<", command=lambda: navigate_month(year, month, -1))
    prev_month_button.grid(row=0, column=0, padx=10)

    next_month_button = tk.Button(nav_frame, text=">", command=lambda: navigate_month(year, month, 1))
    next_month_button.grid(row=0, column=2, padx=10)

    current_label = tk.Label(nav_frame, text=f"{calendar.month_name[month]} {year}", font=('Arial', 14, 'bold'), bg="lightblue")
    current_label.grid(row=0, column=1)

    # Create a frame for the calendar days
    days_frame = tk.Frame(main_frame, bg="lightblue")
    days_frame.pack()

    # Create labels to display the days of the week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i, day in enumerate(days):
        tk.Label(days_frame, text=day, width=12, font=('Arial', 10, 'bold'), bg="white", relief="solid").grid(row=0, column=i, padx=1, pady=1)

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
                reminder_text = "\n".join(reminders.get(date_key, []))

                # Create a label for the date
                date_label = tk.Label(days_frame, text=f"{day}\n{reminder_text}", width=12, height=6, font=('Arial', 10), fg=label_color, bg=label_bg, relief="ridge", bd=1)
                date_label.grid(row=week_num, column=day_num, padx=1, pady=1)

                # Bind click event to each date label
                date_label.bind("<Button-1>", lambda event, d=day, m=month, y=year: open_reminder_window(event, d, m, y))

def navigate_month(year, month, delta):
    new_month = month + delta
    new_year = year

    if new_month < 1:
        new_month = 12
        new_year -= 1
    elif new_month > 12:
        new_month = 1
        new_year += 1

    display_calendar(new_year, new_month)

def open_reminder_window(event, day, month, year):
    # Check if there are existing reminders for the selected date
    date_key = f"{year}-{month}-{day}"
    existing_reminders = reminders.get(date_key, [])

    # Open a window to display existing reminders
    reminder_window = tk.Toplevel(root)
    reminder_window.title(f"Reminders - {day}/{month}/{year}")

    def remove_reminder(reminder):
        existing_reminders.remove(reminder)
        if not existing_reminders:
            del reminders[date_key]
        save_reminders()
        reminder_window.destroy()
        display_calendar(year, month)  # Refresh calendar to update reminder display

    for reminder in existing_reminders:
        frame = tk.Frame(reminder_window)
        frame.pack(fill='x', pady=5)
        tk.Label(frame, text=reminder, font=('Arial', 12)).pack(side='left')
        remove_button = tk.Button(frame, text="Remove", command=lambda r=reminder: remove_reminder(r))
        remove_button.pack(side='right')

    # Button to add a new reminder
    def add_reminder():
        set_reminder_window(day, month, year)

    add_button = tk.Button(reminder_window, text="Add Reminder", command=add_reminder)
    add_button.pack(pady=10)

    # Button to close the reminder window
    close_button = tk.Button(reminder_window, text="Back", command=reminder_window.destroy)
    close_button.pack(pady=10)

def set_reminder_window(day, month, year, reminder_text=""):
    # Create a new Tkinter window for setting reminders
    reminder_window = tk.Toplevel(root)
    reminder_window.title(f"Set Reminder - {day}/{month}/{year}")

    # Label for selected date
    tk.Label(reminder_window, text=f"Set Reminder for {day}/{month}/{year}", font=('Arial', 12)).pack()

    # Entry field for setting reminder
    reminder_entry = tk.Entry(reminder_window, width=30)
    reminder_entry.insert(0, reminder_text)
    reminder_entry.pack()

    # Function to set reminder
    def set_reminder():
        reminder_text = reminder_entry.get()
        date_key = f"{year}-{month}-{day}"
        if date_key in reminders:
            reminders[date_key].append(reminder_text)
        else:
            reminders[date_key] = [reminder_text]
        save_reminders()
        # Close the reminder window
        reminder_window.destroy()
        display_calendar(year, month)  # Refresh calendar to update reminder display

    # Button to set reminder
    set_button = tk.Button(reminder_window, text="Set Reminder", command=set_reminder)
    set_button.pack()

# Create the main Tkinter window
root = tk.Tk()
root.title("Advanced Calendar")
root.geometry("300x150")

# Entry field for year
tk.Label(root, text="Year:").grid(row=0, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1)

# Combobox for month selection
tk.Label(root, text="Month:").grid(row=1, column=0)
month_combobox = ttk.Combobox(root, values=list(range(1, 13)))
month_combobox.grid(row=1, column=1)
month_combobox.current(datetime.today().month - 1)  # Set default value to the current month

# Button to display calendar
display_button = tk.Button(root, text="Display Calendar", command=display_calendar)
display_button.grid(row=2, columnspan=2)

# Dictionary to store reminders
reminders = {}
load_reminders()  # Load reminders from file

root.mainloop()

