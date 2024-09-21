import re
import tkinter as tk

def check_password_strength():
    password = password_entry.get()
    special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\t\n"

    password_strength = 0

    if 8 <= len(password) < 12:
        password_strength += 0.5
    elif len(password) >= 12:
        password_strength += 1

    if any(char.isdigit() for char in password):
        password_strength += 1
    if any(char in special_characters for char in password):
        password_strength += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        password_strength += 1
    elif any(char.isupper() or char.islower() for char in password):
        password_strength += 0.5

    if password_strength >= 3:
        strength_category = "Strong"
    elif password_strength >= 2:
        strength_category = "Moderate"
    else:
        strength_category = "Weak"

    password_strength_label.config(text="Password Strength: " + strength_category)
    password_score_label.config(text="Password Score: " + str(password_strength))

# Create a Tkinter window
window = tk.Tk()
window.title("Password Strength Checker")
window.config(background= "grey14" )
window.geometry("500x200")
# Create an input field
password_label = tk.Label(window, text="Enter your password:", bg="orange red")
password_label.pack()
password_entry = tk.Entry(window, width=60)
password_entry.pack(pady="30")

# Create a button to check the password
check_button = tk.Button(window, text="Check", command=check_password_strength)
check_button.pack()

# Create labels for password strength and password score
password_strength_label = tk.Label(window, text="Password Strength:", bg="saddle brown")
password_strength_label.pack(side= "bottom")
password_score_label = tk.Label(window, text="Password Score:", bg="saddle brown")
password_score_label.pack(side= "bottom")

# Start the Tkinter main loop
window.mainloop()
