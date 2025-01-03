import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def update_timer():
    """
    Update the countdown timer displayed on the GUI.
    """
    try:
        deadline = datetime.strptime(deadline_entry.get(), "%Y-%m-%d %H:%M:%S")
        current_time = datetime.now()
        remaining_time = deadline - current_time

        if remaining_time.total_seconds() <= 0:
            timer_label.config(text="Time is up!", fg="red")
            messagebox.showinfo("Countdown Timer", "Deadline reached!")
            return

        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        timer_label.config(text=f"{days}d {hours}h {minutes}m {seconds}s", fg="white")

        # Schedule the next update after 1 second
        root.after(1000, update_timer)
    except ValueError:
        timer_label.config(text="Invalid format. Use YYYY-MM-DD HH:MM:SS", fg="yellow")

def start_countdown():
    """
    Start the countdown timer.
    """
    update_timer()

# Create the GUI application
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x300")
root.config(bg="#1e1e2f")

# Header label
header_label = tk.Label(root, text="Countdown Timer", font=("Helvetica", 20, "bold"), bg="#1e1e2f", fg="#4caf50")
header_label.pack(pady=10)

# Deadline entry label and field
entry_label = tk.Label(root, text="Enter deadline (YYYY-MM-DD HH:MM:SS):", font=("Helvetica", 12), bg="#1e1e2f", fg="white")
entry_label.pack(pady=5)

deadline_entry = tk.Entry(root, font=("Helvetica", 12), width=30, justify="center")
deadline_entry.pack(pady=5)

# Start button
start_button = tk.Button(root, text="Start Countdown", font=("Helvetica", 12, "bold"), bg="#4caf50", fg="white", command=start_countdown)
start_button.pack(pady=10)

# Timer display label
timer_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#1e1e2f", fg="white")
timer_label.pack(pady=20)

# Run the application
root.mainloop()
