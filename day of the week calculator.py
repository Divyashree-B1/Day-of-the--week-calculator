import tkinter as tk
from tkinter import messagebox
import datetime
def find_day():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        date = datetime.date(year, month, day)
        day_name = date.strftime("%A")
        messagebox.showinfo("Day of Week", f"The day is: {day_name}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid date!")
root = tk.Tk()
root.title("Day of Week Finder")
root.geometry("300x300")
tk.Label(root, text="Enter Day:").pack()
day_entry = tk.Entry(root)
day_entry.pack()
tk.Label(root, text="Enter Month:").pack()
month_entry = tk.Entry(root)
month_entry.pack()
tk.Label(root, text="Enter Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()
tk.Button(root, text="Find Day", command=find_day).pack(pady=10)
root.mainloop()
