import tkinter as tk
from tkinter import ttk, messagebox
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
            # Convert any single reminder strings to lists
            reminders = {k: [v] if isinstance(v, str) else v for k, v in reminders.items()}
    else:
        reminders = {}


def display_calendar():
    year = year_entry.get().strip()
    month = month_combobox.get().strip()


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
    for widget in days_frame.winfo_children():
        widget.destroy()


    # Create a calendar object
    cal = calendar.monthcalendar(year, month)


    # Create labels to display the days of the week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i, day in enumerate(days):
        tk.Label(days_frame, text=day, width=12, font=('Arial', 10, 'bold'), bg="lightblue", relief="solid").grid(row=0, column=i, padx=5, pady=1)


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
                reminder_texts = reminders.get(date_key, [])


                # Create a label for the date
                date_label = tk.Label(days_frame, text=f"{day}\n{', '.join(reminder_texts)}", width=12, height=6, font=('Arial', 10), fg=label_color, bg=label_bg, relief="ridge", bd=1, justify=tk.LEFT)
                date_label.grid(row=week_num, column=day_num, padx=1, pady=1)


                # Bind click event to each date label (left-click for touch, right-click for context menu)
                date_label.bind("<Button-1>", lambda event, d=day, m=month, y=year, r=reminder_texts: open_reminder_menu(event, d, m, y, r))
                date_label.bind("<Button-3>", lambda event, d=day, m=month, y=year, r=reminder_texts: open_reminder_menu(event, d, m, y, r))


def open_reminder_menu(event, day, month, year, reminders):
    menu = tk.Menu(root, tearoff=0)


    if not reminders:
        menu.add_command(label="Set Reminder", command=lambda: set_reminder_window(day, month, year))
    else:
        for reminder in reminders:
            menu.add_command(label=reminder, command=lambda r=reminder: confirm_remove_reminder(day, month, year, r))


        menu.add_separator()
        menu.add_command(label="Add Reminder", command=lambda: set_reminder_window(day, month, year))
        menu.add_command(label="Cancel")


    try:
        menu.tk_popup(event.x_root, event.y_root, 0)
    finally:
        menu.grab_release()


def confirm_remove_reminder(day, month, year, reminder_text):
    confirm = messagebox.askyesno("Confirm Remove", "Remove existing reminder?")
    if confirm:
        remove_reminder(day, month, year, reminder_text)


def remove_reminder(day, month, year, reminder_text):
    date_key = f"{year}-{month}-{day}"
    if date_key in reminders:
        reminders[date_key].remove(reminder_text)
        if not reminders[date_key]:
            del reminders[date_key]
        save_reminders()
        display_calendar()  # Refresh calendar to update reminder display


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
        reminder_text = reminder_entry.get().strip()
        if reminder_text:
            date_key = f"{year}-{month}-{day}"
            if date_key in reminders:
                reminders[date_key].append(reminder_text)
            else:
                reminders[date_key] = [reminder_text]
            save_reminders()
            # Close the reminder window
            reminder_window.destroy()
            display_calendar()  # Refresh calendar to update reminder display
        else:
            tk.messagebox.showerror("Error", "Reminder cannot be empty.")


    # Button to set reminder
    set_button = tk.Button(reminder_window, text="Set Reminder", command=set_reminder)
    set_button.pack()


    # Button to close the reminder window
    close_button = tk.Button(reminder_window, text="Back", command=reminder_window.destroy)
    close_button.pack()


# Create the main Tkinter window
root = tk.Tk()
root.title("Advanced Calendar")
root.geometry("1000x800")


# Frame for year and month input
input_frame = tk.Frame(root)
input_frame.pack(pady=20)


# Entry field for year
tk.Label(input_frame, text="Year:").grid(row=0, column=0)
year_entry = tk.Entry(input_frame)
year_entry.grid(row=0, column=1)


# Combobox for month selection
tk.Label(input_frame, text="Month:").grid(row=0, column=2)
month_combobox = ttk.Combobox(input_frame, values=list(range(1, 13)))
month_combobox.grid(row=0, column=3)
month_combobox.current(datetime.today().month - 1)  # Set default value to the current month


# Button to display calendar
display_button = tk.Button(input_frame, text="Display Calendar", command=display_calendar)
display_button.grid(row=0, column=4, padx=10)


# Frame for displaying calendar
days_frame = tk.Frame(root, bg="lightblue")
days_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)


# Dictionary to store reminders
reminders = {}
load_reminders()  # Load reminders from file


root.mainloop()
