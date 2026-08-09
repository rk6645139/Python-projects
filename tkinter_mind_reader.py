import tkinter as tk
import time

def read_mind():
    """Simulates mind reading with a delay and reveals the same number."""
    user_number = entry.get()
    
    if not user_number.isdigit():
        result_label.config(text="Please enter a valid number!", fg="red")
        return

    result_label.config(text="Reading your mind... 🧠", fg="black")
    root.update()
    time.sleep(2)
    
    result_label.config(text="Processing... 🔮", fg="black")
    root.update()
    time.sleep(2)

    result_label.config(text=f"I got it! You were thinking of... {user_number}! 😲", fg="blue")

# Create main window
root = tk.Tk()
root.title("Mind Reader")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="I Can Read Your Mind!", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Entry field for user input
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Button to start mind reading
start_button = tk.Button(root, text="Read My Mind", font=("Arial", 12), command=read_mind)
start_button.pack(pady=20)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the Tkinter loop
root.mainloop()
