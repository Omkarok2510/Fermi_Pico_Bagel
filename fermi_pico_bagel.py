import tkinter as tk
import random

# Generate a random 3-digit number with unique digits
def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:3])

original_number = generate_number()  # Store generated number

# Function to process user guess
def check_guess():
    global original_number

    guess_number = entry.get()
    
    # Validate input length
    if len(guess_number) != 3 or not guess_number.isdigit():
        result_label.config(text="❌ Invalid Input! Enter a 3-digit number.", fg="red")
        return
    
    # Validate uniqueness
    if len(set(guess_number)) != 3:
        result_label.config(text="❌ Duplicate digits! Try again.", fg="red")
        return

    output = []

    # Check conditions for "Fermi", "Pico", "Bagel"
    for i in range(3):
        if guess_number[i] == original_number[i]:
            output.append("Fermi ✅")
        elif guess_number[i] in original_number:
            output.append("Pico 🔄")

    if not output:
        output.append("Bagel ❌")

    # Check if user wins
    if output == ["Fermi ✅", "Fermi ✅", "Fermi ✅"]:
        result_label.config(text=f"🎉 You Win! The number was {original_number}!", fg="green")
        restart_button.pack()  # Show Restart Button
    else:
        result_label.config(text=" | ".join(output), fg="blue")

# Restart the game
def restart_game():
    global original_number
    original_number = generate_number()
    result_label.config(text="🆕 New Game Started! Enter a 3-digit number.", fg="black")
    entry.delete(0, tk.END)
    restart_button.pack_forget()  # Hide Restart Button

# Setup UI
root = tk.Tk()
root.title("Fermi, Pico, Bagel Game")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="🎲 Fermi, Pico, Bagel!", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Entry Box
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Check", font=("Arial", 12), command=check_guess)
submit_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Enter a 3-digit number.", font=("Arial", 12))
result_label.pack(pady=5)

# Restart Button (Initially Hidden)
restart_button = tk.Button(root, text="Restart Game", font=("Arial", 12), command=restart_game)
restart_button.pack_forget()

# Start Game
root.mainloop()
