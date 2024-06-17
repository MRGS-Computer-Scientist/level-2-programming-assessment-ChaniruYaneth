from tkinter import *
from tkinter import ttk, messagebox
import os

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
root.title("Resources and Materials")
root.geometry("1100x900")
root.config(bg="#F2EEE3")

# Load and resize the logo image
logo_image_path = os.path.join(os.path.dirname(__file__), 'images', 'logo.png')
logo_image = PhotoImage(file=logo_image_path)
resized_logo_image = logo_image.subsample(2, 2)

# Display the logo
logo_label = Label(root, image=resized_logo_image, bg="#F2EEE3")
logo_label.pack(pady=(20, 20))

# Add the logout button
logout_button = Button(root, text="Logout", bg="#BCA0A0", command=confirm_exit)
logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

# Add the resources and materials text
resources_text = "RESOURCES AND MATERIALS CLICK ON THE SEARCH BAR VISIBLE, AND SELECT THE SUBJECT YOU REQUIRE ASSISTANCE. HELP YOURSELVES BY GOING THROUGH WHAT THE SUBJECT OFFERS YOU FOR LEVEL TWO AND WE WISH YOU GOOD LUCK WITH YOUR STUDIES..."
resources_label = Label(root, text=resources_text, bg="#F2EEE3", font=("Arial", 14), wraplength=500, justify="left")
resources_label.pack(pady=(20, 20))

# Add the search bar
search_bar_frame = Frame(root, bg="#F2EEE3")
search_bar_frame.pack(pady=(10, 10))

search_label = Label(search_bar_frame, text="Search:", bg="#F2EEE3", font=("Arial", 14))
search_label.pack(side=LEFT, padx=(10, 5))

search_entry = Entry(search_bar_frame, font=("Arial", 14))
search_entry.pack(side=LEFT, fill=X, expand=True)

# Add the image of the girl pointing to the search bar
resources_girl_image_path = os.path.join(os.path.dirname(__file__), 'images', 'Resources Girl.png')
resources_girl_image = PhotoImage(file=resources_girl_image_path)

resources_girl_label = Label(root, image=resources_girl_image, bg="#F2EEE3")
resources_girl_label.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

root.mainloop()
