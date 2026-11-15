import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Form")
root.geometry("400x430")

canvas = tk.Canvas(root, width=400, height=430, highlightthickness=0)
canvas.pack(fill="both", expand=True)

bg_photo = tk.PhotoImage(file="ok.png")
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

card = tk.Frame(root, bg="pink", padx=4, pady=5, highlightbackground="yellow", highlightthickness=3)
card.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(card, text="USER LOGIN", font=("Times New Roman", 20, "bold"), bg="pink")
title_label.pack(pady=5)

subtitle = tk.Label(card, text="Welcome back, cutie! ✿'ed", font=("Comfortaa", 9),
                    bg="pink", fg="black")
subtitle.pack(pady=(0, 8))

username_label = tk.Label(card, text="Username", font=("Arial", 11), bg="pink", fg="black")
username_label.pack(anchor="w", pady=5)

username_entry = tk.Entry(card, font=("Courier New", 12), width=25)
username_entry.pack(pady=5)

password_label = tk.Label(card, text="Password", font=("Arial", 12), bg="pink", fg="black")
password_label.pack(anchor="w", pady=5)

password_entry = tk.Entry(card, font=("Courier New", 12), width=25, show="*")
password_entry.pack(pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Sevi" and password == "is cute":
        messagebox.showinfo("LOGIN SUCCESSFULLY!", "Welcome Sevi!")
    else:
        messagebox.showerror("LOGIN FAILED!", "Invalid Username and Password!")

login_button = tk.Button(card, text="LOG IN", font=("Times New Roman", 12, "bold"), bg="sky blue", fg="white", width=20, command=login)
login_button.pack(pady=10)

root.mainloop()