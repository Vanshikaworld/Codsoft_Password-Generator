
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Define the characters used in the password
characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"',
    "'", '<', '>', ',', '.', '?', '/'
]


# Function to generate password
def generate_password():
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive number.", icon='warning')
            return

        password = ""
        for i in range(1, n + 1):
            a = random.choice(characters)
            while a in password:
                a = random.choice(characters)
            password += a

        password_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.", icon='warning')


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#ffffff")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="#f0f0f0")
style.configure("TButton", font=("Helvetica", 14))
style.configure("TEntry", font=("Helvetica", 14))

# Create and place the input field for password length
ttk.Label(root, text="Enter the length of Password you want:").pack(pady=10)
entry = ttk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

# Variable to store the generated password
password_var = tk.StringVar()

# Create and place the button to generate the password
ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Create and place the label to display the generated password
ttk.Label(root, text="Generated Password:").pack(pady=10)
password_entry = tk.Entry(root, textvariable=password_var, state='readonly', font=("Helvetica", 14), bg="#d3d3d3",
                          fg="#0000ff")
password_entry.pack(pady=10)

# Run the main event loop
root.mainloop()
