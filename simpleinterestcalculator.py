import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest
def calculate_si():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())
        si = (p * r * t) / 100
        result_label.config(text=f"Simple Interest = {si:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("350x300")
root.config(bg="#f0f0f0")

# Title Label
tk.Label(root, text="Simple Interest Calculator", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="blue").pack(pady=10)

# Principal input
tk.Label(root, text="Principal (P):", font=("Arial", 12), bg="#f0f0f0").pack()
principal_entry = tk.Entry(root, width=25)
principal_entry.pack(pady=5)

# Rate input
tk.Label(root, text="Rate of Interest (R):", font=("Arial", 12), bg="#f0f0f0").pack()
rate_entry = tk.Entry(root, width=25)
rate_entry.pack(pady=5)

# Time input
tk.Label(root, text="Time (T in years):", font=("Arial", 12), bg="#f0f0f0").pack()
time_entry = tk.Entry(root, width=25)
time_entry.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), bg="green", fg="white", command=calculate_si).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="red")
result_label.pack(pady=10)

# Run the application
root.mainloop()
