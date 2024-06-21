import tkinter as tk
from tkinter import ttk
import calendar


def display_calendar():
    # Get the year and month from entry fields
    year = int(year_entry.get())
    month = int(month_combobox.get())


    # Create a calendar object
    cal = calendar.monthcalendar(year, month)


    # Create a new Tkinter window for the calendar
    calendar_window = tk.Toplevel(root)
    calendar_window.title(f"Calendar - {calendar.month_name[month]} {year}")


    # Create labels to display the days of the week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i, day in enumerate(days):
        tk.Label(calendar_window, text=day, width=5, font=('Arial', 10, 'bold')).grid(row=0, column=i)


    # Display the calendar data
    for week_num, week in enumerate(cal, start=1):
        for day_num, day in enumerate(week):
            if day != 0:
                # Determine the color of the label based on the day
                if day_num in (5, 6):  # Weekend (Saturday and Sunday)
                    label_color = 'red'
                else:
                    label_color = 'black'


                # Create a label for the date
                date_label = tk.Label(calendar_window, text=day, width=5, font=('Arial', 10), fg=label_color)
                date_label.grid(row=week_num, column=day_num)


                # Bind click event to each date label
                date_label.bind("<Button-1>", lambda event, d=day, m=month: open_reminder_window(event, d, m))


def open_reminder_window(event, day, month):
    # Check if there is an existing reminder for the selected date
    if (day, month) in reminders:
        existing_reminder = reminders[(day, month)]
        # Open a window to display existing reminder
        reminder_window = tk.Toplevel(root)
        reminder_window.title(f"Existing Reminder - {day}/{month}")


        # Label to display existing reminder
        tk.Label(reminder_window, text=f"Existing Reminder: {existing_reminder}", font=('Arial', 12)).pack()


        # Button to remove existing reminder
        def remove_reminder():
            del reminders[(day, month)]
            reminder_window.destroy()


        remove_button = tk.Button(reminder_window, text="Remove Existing Reminder", command=remove_reminder)
        remove_button.pack()


        # Button to add reminder
        def add_reminder():
            # Open window to add new reminder
            add_reminder_window = tk.Toplevel(root)
            add_reminder_window.title(f"Add Reminder - {day}/{month}")


            # Entry field for new reminder
            reminder_entry = tk.Entry(add_reminder_window, width=30)
            reminder_entry.pack()


            # Function to set new reminder
            def set_reminder():
                reminder_text = reminder_entry.get()
                reminders[(day, month)] = reminder_text
                add_reminder_window.destroy()


            # Button to set new reminder
            set_button = tk.Button(add_reminder_window, text="Add Reminder", command=set_reminder)
            set_button.pack()


        add_button = tk.Button(reminder_window, text="Add Reminder", command=add_reminder)
        add_button.pack()


        # Button to close the reminder window
        close_button = tk.Button(reminder_window, text="Back", command=reminder_window.destroy)
        close_button.pack()


    else:
        # If no existing reminder, proceed with setting a new reminder
        set_reminder_window(day, month)


def set_reminder_window(day, month):
    # Create a new Tkinter window for setting reminders
    reminder_window = tk.Toplevel(root)
    reminder_window.title(f"Set Reminder - {day}/{month}")


    # Label for selected date
    tk.Label(reminder_window, text=f"Set Reminder for {day}/{month}", font=('Arial', 12)).pack()


    # Entry field for setting reminder
    reminder_entry = tk.Entry(reminder_window, width=30)
    reminder_entry.pack()


    # Function to set reminder
    def set_reminder():
        reminder_text = reminder_entry.get()
        # Store the reminder with the corresponding date
        reminders[(day, month)] = reminder_text
        # Close the reminder window
        reminder_window.destroy()


    # Button to set reminder
    set_button = tk.Button(reminder_window, text="Set Reminder", command=set_reminder)
    set_button.pack()


# Create the main Tkinter window
root = tk.Tk()
root.title("Visual Calendar")


# Entry field for year
tk.Label(root, text="Year:").grid(row=0, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1)


# Combobox for month selection
tk.Label(root, text="Month:").grid(row=1, column=0)
month_combobox = ttk.Combobox(root, values=list(range(1, 13)))
month_combobox.grid(row=1, column=1)
month_combobox.current(0)  # Set default value to January (index 0)


# Button to display calendar
display_button = tk.Button(root, text="Display Calendar", command=display_calendar)
display_button.grid(row=2, columnspan=2)


# Dictionary to store reminders
reminders = {}


root.mainloop()



