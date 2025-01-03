import time
from datetime import datetime

def countdown_timer(deadline):
    """
    Countdown timer to calculate time remaining until the given deadline.

    Parameters:
    deadline (str): The deadline in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    try:
        deadline_time = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")
        print(f"Deadline set to: {deadline_time}")

        while True:
            current_time = datetime.now()
            remaining_time = deadline_time - current_time

            if remaining_time.total_seconds() <= 0:
                print("\nDeadline reached! Time is up.")
                break

            days = remaining_time.days
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"Time remaining: {days}d {hours}h {minutes}m {seconds}s", end="\r")
            time.sleep(1)

    except ValueError:
        print("Invalid deadline format. Please use 'YYYY-MM-DD HH:MM:SS'.")

if __name__ == "__main__":
    print("Welcome to the Countdown Timer!")
    user_deadline = input("Enter the deadline (YYYY-MM-DD HH:MM:SS): ")
    countdown_timer(user_deadline)
