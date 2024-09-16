import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the number input fields
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create and place the operation selection dropdown
operation_var = tk.StringVar(root)
operation_var.set("Add")  # default value

tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=10)
operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Create and place the result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
