

'''Name : Pierre Moise D 
Project for Final
This project is an application as a vending machine called QuickVend that sells snacks and drinks
'''
import tkinter as tk    # Standard Python library for creating GUI applications
from tkinter import messagebox  #I use it to display errors!

# Initializion of the  main application window
root = tk.Tk()
root.title("QuickVend")
root.geometry("500x500")
root.configure(bg="black")

# The Products and their prices (dictionary)
products = {
    "Coca-Cola": {"price": 1.50},
    "Snack": {"price": 2.00},
    "Water": {"price": 1.00},
    "Energy Drink": {"price": 2.50}
}

# store names and amount inserted
ProductSelected = None
InsertAmount = 0.0

# Function to validate selection
def validate_selection():
    global ProductSelected
    ProductSelected = product_var.get() #retrieve the item selected from the menu dropdown
    if ProductSelected == "Choose an item":
        messagebox.showerror("Error", "Please select an item.")
    else:
        open_payment_window(ProductSelected)  # Open payment window if a valid item is selected

# Function to open payment window
def open_payment_window(product):
    WindowPayment = tk.Toplevel(root)
    WindowPayment.title("Payment")
    WindowPayment.geometry("350x250")

    price = products[product]["price"]  # Get price of selected product

    tk.Label(WindowPayment, text=f"Selected Item: {product} (${price:.2f})").pack(pady=10) 
    tk.Label(WindowPayment, text="Enter Amount (Numbers Only):").pack(pady=5)

    amount_entry = tk.Entry(WindowPayment) #generate a text entry for the user to input amount.
    amount_entry.pack(pady=5) #vertical padding

    # Process payment
    def process_payment():
        global InsertAmount # Allow function to modify variable InsertAmount
        amount = amount_entry.get().strip() #Takes user input and removes leading spaces.

        try:
            # Check if the input is empty
            if not amount:
                return ValueError("Please enter an amount.")

            # Check if the input is a valid number (allows decimal points)
            if not amount.replace(".", "", 1).isdigit():  # Remove one decimal point
                return ValueError("Invalid input: letters or symbols are not allowed.")

            InsertAmount = float(amount)
            if InsertAmount <= 0:
                return ValueError("Amount must be greater than zero.")
            elif InsertAmount < price:
                return ValueError("The amount entered is not enough.")
            else:
                change = InsertAmount - price
                open_receipt_window(product, price, InsertAmount, change)
                WindowPayment.destroy()  # Close payment window
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            amount_entry.delete(0, tk.END) # Clears the entry field

    tk.Button(WindowPayment, text="Confirm Payment", command=process_payment).pack(pady=5)  # Confirm Payment
    tk.Button(WindowPayment, text="Cancel", command=WindowPayment.destroy).pack(pady=5)  # Cancel Payment

# Function to open receipt window
def open_receipt_window(product, price, inserted_amount, change):
    ReceiptWindow = tk.Toplevel(root)
    ReceiptWindow.title("Receipt")
    ReceiptWindow.geometry("400x400")  # Increased height to accommodate the image
    ReceiptWindow.configure(bg="black")

    # Transaction details
    tk.Label(ReceiptWindow, text="This is your receipt", font=("Arial", 14, "bold"), bg="black", fg="white").pack(pady=10)
    tk.Label(ReceiptWindow, text=f"Item: {product}", bg="black", fg="white").pack(pady=5)
    tk.Label(ReceiptWindow, text=f"Price: ${price:.2f}", bg="black", fg="white").pack(pady=5)
    tk.Label(ReceiptWindow, text=f"Amount Inserted: ${inserted_amount:.2f}", bg="black", fg="white").pack(pady=5)
    tk.Label(ReceiptWindow, text=f"Change: ${change:.2f}", bg="black", fg="white").pack(pady=5)

    # Buttons
    def PurchaseAnotherItem():
        ReceiptWindow.destroy()
        product_var.set("Choose an item")  # Reset dropdown

    tk.Button(ReceiptWindow, text="Purchase another Item", bg="brown", fg="white", command=PurchaseAnotherItem).pack(pady=10)
    tk.Button(ReceiptWindow, text="Exit", bg="red", fg="white", command=root.destroy).pack(pady=5)

        # Load image for receipt window
    try:
        receipt_image = tk.PhotoImage(file=r"C:/Users/moise/OneDrive/Bureau/Spring 2025/Coding/FinalProject/money.png")
        receipt_image = receipt_image.subsample(2, 2)  # Resize the image
        receipt_image_label = tk.Label(ReceiptWindow, image=receipt_image, bg="black")
        receipt_image_label.pack(pady=10)
        receipt_image_label.image = receipt_image  # Keep a reference to avoid garbage collection
    except tk.TclError:
        tk.Label(ReceiptWindow, text="[Image Not Found]", bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# Dropdown menu for product selection
product_var = tk.StringVar(root)
product_var.set("Choose an item")  # Default value
dropdown = tk.OptionMenu(root, product_var, *products.keys())
dropdown.pack(pady=5)

# Button to validate selection
tk.Button(root, text="Select Item", command=validate_selection).pack(pady=10)

# Button to exit the application
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

# Load image for main window
try:
    quickVendImage = tk.PhotoImage(file=r"C:/Users/moise/OneDrive/Bureau/Spring 2025/Coding/FinalProject/vending.png")
    quickVendImage = quickVendImage.subsample(2, 2)  # Resize the image
    quickvendLabel = tk.Label(root, image=quickVendImage, bg="black")
    quickvendLabel.pack(pady=5)
    quickvendLabel.image = quickVendImage  # remains displayed in the Tkinter window.








except tk.TclError:  # Handles missing images
    tk.Label(root, text="[Image Not Found]", bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

# Start the main event loop
root.mainloop()