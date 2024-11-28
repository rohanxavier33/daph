import tkinter as tk
from tkinter import messagebox
import time
import threading


def love_calculation():
    def calculate_love():
        try:
            love_amount = int(love_input.get())
            output_label["text"] = ""
            for i in range(love_amount + 1):
                if i > 0:
                    output_label["text"] = f"You love {true_love.get()} x {i}"
                    time.sleep(3 / i)
                else:
                    output_label["text"] = "Guess what"
                    time.sleep(2.5)
        except ValueError:
            output_label["text"] = f"You love {true_love.get()} {love_input.get()}"
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Use threading to prevent the GUI from freezing during the loop
    threading.Thread(target=calculate_love).start()


# Initialize the tkinter window
root = tk.Tk()
root.title("Love Calculator")

# Define input fields and labels
tk.Label(root, text="Who is your true love?").pack(pady=5)
true_love = tk.Entry(root, width=30)
true_love.pack(pady=5)

tk.Label(root, text="How much do you love them?").pack(pady=5)
love_input = tk.Entry(root, width=30)
love_input.pack(pady=5)

# Output label
output_label = tk.Label(root, text="", fg="blue", font=("Arial", 14))
output_label.pack(pady=10)

# Button to calculate
calculate_button = tk.Button(root, text="Show Love", command=love_calculation)
calculate_button.pack(pady=10)

# Run the tkinter loop
root.mainloop()
