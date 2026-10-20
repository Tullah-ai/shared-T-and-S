
import tkinter as tk
from tkinter import ttk
import sqlite3

def check_database():
    try:
        connection = sqlite3.connect("asaq_farm.db")
        connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
        connection.close()
        return "Database connected successfully"
    except sqlite3.Error:
        return "Database connection failed"

root = tk.Tk()
root.title("Asaq Poultry Farm Management System")
root.geometry("900x600")
root.minsize(750, 500)

ttk.Label(
    root,
    text="ASAQ POULTRY FARM",
    font=("Arial", 22, "bold")
).pack(pady=(25, 5))

ttk.Label(
    root,
    text="Farm Management Dashboard",
    font=("Arial", 12)
).pack(pady=5)

status = ttk.Label(root, text=check_database())
status.pack(pady=10)

menu = ttk.Frame(root, padding=20)
menu.pack(fill="both", expand=True)

buttons = [
    "Flock Management",
    "Egg Production",
    "Sales",
    "Expenses",
    "Stock Management",
    "Employees",
    "Reports",
]

for i, name in enumerate(buttons):
    ttk.Button(
        menu,
        text=name,
        width=25
    ).grid(
        row=i // 2,
        column=i % 2,
        padx=15,
        pady=12,
        ipadx=10,
        ipady=10,
        sticky="ew"
    )

menu.columnconfigure(0, weight=1)
menu.columnconfigure(1, weight=1)

root.mainloop()
