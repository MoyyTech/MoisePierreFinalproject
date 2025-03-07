import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Required for image resizing

# Initialize main application window
root = tk.Tk()
root.title("QuickVend")
root.geometry("500x500")
root.configure(bg="black")

# Products and their prices (dictionary)
products = {
    "Coca-Cola": {"price": 1.50},
    "Snack": {"price": 2.00},
    "Water": {"price": 1.00},
    "Energy Drink": {"price": 2.50}
}

# Function to validate selection and open the payment window
def validate_selection():
    product_selected = product_var.get()
    if product_selected == "Choose an item":
        messagebox.showerror("Error", "Please select an item.")
    else:
        open_payment_window(product_selected)

# Function to open payment window
def open_payment_window(product):
    window_payment = tk.Toplevel(root)
    window_payment.title("Payment")
    window_payment.geometry("350x250")

    price = products[product]["price"]  # Get price of selected product

    # Labels for payment window
    tk.Label(window_payment, text=f"Selected Item: {product} (${price:.2f})").pack(pady=10)
    tk.Label(window_payment, text="Enter Amount (Numbers Only):").pack(pady=5)

    # Entry for payment amount
    amount_entry = tk.Entry(window_payment)
    amount_entry.pack(pady=5)

    # Function to process payment
    def process_payment():
        try:
            insert_amount = float(amount_entry.get().strip())

            if insert_amount <= 0:
                messagebox.showerror("Invalid Input", "Amount must be greater than zero.")
                amount_entry.delete(0, tk.END)  # Clear entry box
            elif insert_amount < price:
                messagebox.showerror("Insufficient Amount", "The amount entered is not enough.")
                amount_entry.delete(0, tk.END)
            else:
                change = insert_amount - price
                open_receipt_window(product, price, insert_amount, change)
                window_payment.destroy()  # Close payment window

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            amount_entry.delete(0, tk.END)

    # Buttons for payment window
    tk.Button(window_payment, text="Confirm Payment", command=process_payment).pack(pady=5)
    tk.Button(window_payment, text="Cancel", command=window_payment.destroy).pack(pady=5)

# Function to open receipt window
def open_receipt_window(product, price, inserted_amount, change):
    receipt_window = tk.Toplevel(root)
    receipt_window.title("Receipt")
    receipt_window.geometry("400x300")
    receipt_window.configure(bg="black")

    # Labels for receipt window
    tk.Label(receipt_window, text="Transaction Details", font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=10)
    tk.Label(receipt_window, text=f"Item: {product}", fg="white", bg="black").pack(pady=5)
    tk.Label(receipt_window, text=f"Price: ${price:.2f}", fg="white", bg="black").pack(pady=5)
    tk.Label(receipt_window, text=f"Amount Inserted: ${inserted_amount:.2f}", fg="white", bg="black").pack(pady=5)
    tk.Label(receipt_window, text=f"Change: ${change:.2f}", fg="white", bg="black").pack(pady=5)

    # Function to purchase another item
    def purchase_another_item():
        receipt_window.destroy()
        product_var.set("Choose an item")  # Reset dropdown

    # Buttons for receipt window
    tk.Button(receipt_window, text="Purchase another Item", command=purchase_another_item).pack(pady=10)
    tk.Button(receipt_window, text="Exit", command=root.destroy).pack(pady=5)

# Dropdown menu for product selection
product_var = tk.StringVar(root)
product_var.set("Choose an item")  # Default value
dropdown = tk.OptionMenu(root, product_var, *products.keys())
dropdown.pack(pady=10)

# Load and display the image
try:
    image_path = r"C:/Users/moise/OneDrive/Bureau/Spring 2025/Coding/FinalProject/vending.png"
    image = Image.open(image_path)
    image = image.resize((200, 200))  # Resize to fit the GUI properly
    quickVendImage = ImageTk.PhotoImage(image)
    quickvendLabel = tk.Label(root, image=quickVendImage, bg="yellow")
    quickvendLabel.pack(pady=5)
except Exception:  # Handles missing images
    tk.Label(root, text="[Image Not Found]", bg="Yellow", font=("Arial", 12, "bold")).pack(pady=5)

# Button to validate selection
tk.Button(root, text="Select Item", command=validate_selection).pack(pady=10)

# Button to exit the application
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

# Start the main event loop
root.mainloop()
