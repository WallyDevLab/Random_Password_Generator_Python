import random
import string
import tkinter as tk

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
length_label = tk.Label(root, text="Enter Password Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
result_label = tk.Label(root, text="")

# Grid layout
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
