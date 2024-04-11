from tkinter import *
from datetime import date

root = Tk()
root.title('Codemy.com - Date')
root.geometry("500x350")

panic = Label(root, text="Don't panic!", font=("Helvetica", 42), bg="black", fg="green")
panic.pack(pady=20, ipadx=10, ipady=10)

today = date.today()

today_label = Label(root, text=today)
today_label.pack(pady=20)
