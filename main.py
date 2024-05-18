from tkinter import *
import time

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
                message_label. config(text="You have succesfully signed-up.")
                create_account_window.after(3000, create_account_window.destroy)

        else:
            message_label.config(text="Passwords do not match. Please try again.")


    create_account_window = Toplevel(root)
    create_account_window.title("Sign-Up")
    create_account_window.geometry("500x300")
    create_account_window.config(bg="#F2EEE3")