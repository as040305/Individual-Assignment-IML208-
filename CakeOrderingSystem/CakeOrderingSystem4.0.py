import tkinter as tk

def make_gui_big(root):
    """Resize the GUI window to a larger size."""
    root.geometry("800x600")

def welcome_gui():
    def proceed():
        root.destroy()

    root = tk.Tk()
    root.title("Welcome")
    make_gui_big(root)

    tk.Label(root, text="Welcome to ふくも Cake Ordering Service!", font=("Arial", 20)).pack(pady=20)
    tk.Button(root, text="Proceed", font=("Arial", 14), command=proceed).pack(pady=20)

    root.mainloop()

def thank_you_gui():
    def close():
        root.destroy()

    root = tk.Tk()
    root.title("Thank You")
    make_gui_big(root)

    tk.Label(root, text="Thank you for your order!", font=("Arial", 20)).pack(pady=20)
    tk.Button(root, text="Close", font=("Arial", 14), command=close).pack(pady=20)

    root.mainloop()

def get_customer_details():
    def submit_details():
        customer_details["name"] = name_entry.get()
        customer_details["phone"] = phone_entry.get()
        customer_details["address"] = address_entry.get()
        root.destroy()

    customer_details = {"name": "", "phone": "", "address": ""}
    root = tk.Tk()
    root.title("Customer Details")
    make_gui_big(root)

    tk.Label(root, text="Enter your name:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root, font=("Arial", 14))
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Enter your phone number:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(root, font=("Arial", 14))
    phone_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Enter your address:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5)
    address_entry = tk.Entry(root, font=("Arial", 14))
    address_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(root, text="Submit", font=("Arial", 14), command=submit_details).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()
    return customer_details

def choose_size():
    def submit_size():
        selected["size"] = size_var.get()
        root.destroy()

    selected = {"size": ""}
    root = tk.Tk()
    root.title("Choose Cake Size")
    make_gui_big(root)

    size_var = tk.StringVar(value="1")
    tk.Label(root, text="Select a cake size:", font=("Arial", 14)).pack(pady=10)
    tk.Radiobutton(root, text="Small (15cm) - RM45", variable=size_var, value="1", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Medium (20cm) - RM65", variable=size_var, value="2", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Large (25cm) - RM95", variable=size_var, value="3", font=("Arial", 12)).pack(anchor="w")

    tk.Button(root, text="Submit", font=("Arial", 14), command=submit_size).pack(pady=10)

    root.mainloop()

    size = {"1": ("Small", 45), "2": ("Medium", 65), "3": ("Large", 95)}
    return size.get(selected["size"], ("Invalid", 0))

def choose_flavour():
    def submit_flavour():
        selected["flavour"] = flavour_var.get()
        root.destroy()

    selected = {"flavour": ""}
    root = tk.Tk()
    root.title("Choose Cake Flavour")
    make_gui_big(root)

    flavour_var = tk.StringVar(value="1")
    tk.Label(root, text="Select a cake flavour:", font=("Arial", 14)).pack(pady=10)
    tk.Radiobutton(root, text="Vanilla", variable=flavour_var, value="1", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Chocolate", variable=flavour_var, value="2", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Strawberry", variable=flavour_var, value="3", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Ube", variable=flavour_var, value="4", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Coffee", variable=flavour_var, value="5", font=("Arial", 12)).pack(anchor="w")

    tk.Button(root, text="Submit", font=("Arial", 14), command=submit_flavour).pack(pady=10)

    root.mainloop()

    flavour = {"1": "Vanilla", "2": "Chocolate", "3": "Strawberry", "4": "Ube", "5": "Coffee"}
    return flavour.get(selected["flavour"], "Invalid")

def choose_toppings():
    def submit_toppings():
        selected["toppings"] = toppings_var.get()
        root.destroy()

    selected = {"toppings": ""}
    root = tk.Tk()
    root.title("Choose Cake Toppings")
    make_gui_big(root)

    toppings_var = tk.StringVar(value="1")
    tk.Label(root, text="Select cake toppings:", font=("Arial", 14)).pack(pady=10)
    tk.Radiobutton(root, text="Fruits", variable=toppings_var, value="1", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Chocolate Shavings", variable=toppings_var, value="2", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Almonds and Cashews", variable=toppings_var, value="3", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Coconut Shavings", variable=toppings_var, value="4", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="No toppings", variable=toppings_var, value="5", font=("Arial", 12)).pack(anchor="w")

    tk.Button(root, text="Submit", font=("Arial", 14), command=submit_toppings).pack(pady=10)

    root.mainloop()

    toppings = {"1": "Fruits", "2": "Chocolate Shavings", "3": "Almonds and Cashews", "4": "Coconut Shavings", "5": "No toppings"}
    return toppings.get(selected["toppings"], "Invalid")

def check_allergens():
    def submit_allergens():
        has_allergens["value"] = has_allergens_var.get() == "yes"
        allergen_list["value"] = allergens_entry.get().split(",") if has_allergens["value"] else []
        root.destroy()

    has_allergens = {"value": False}
    allergen_list = {"value": []}
    root = tk.Tk()
    root.title("Allergens Information")
    make_gui_big(root)

    has_allergens_var = tk.StringVar(value="no")
    tk.Label(root, text="Do you have any allergens?", font=("Arial", 14)).pack(pady=10)
    tk.Radiobutton(root, text="Yes", variable=has_allergens_var, value="yes", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="No", variable=has_allergens_var, value="no", font=("Arial", 12)).pack(anchor="w")

    tk.Label(root, text="List your allergens (comma-separated):", font=("Arial", 14)).pack(pady=5)
    allergens_entry = tk.Entry(root, font=("Arial", 12))
    allergens_entry.pack(pady=5)

    tk.Button(root, text="Submit", font=("Arial", 14), command=submit_allergens).pack(pady=10)

    root.mainloop()
    return has_allergens["value"], allergen_list["value"]

def display_order(customer, size, flavour, toppings, allergens):
    print("\n-- Booking Order --")
    print(f"Customer Name: {customer['name']}")
    print(f"Phone Number: {customer['phone']}")
    print(f"Customer Address: {customer['address']}")
    print(f"Cake Size: {size[0]} - RM {size[1]}")
    print(f"Cake Flavour: {flavour}")
    print(f"Cake Toppings: {toppings}")
    if allergens[0]:
        print(f"Allergens: {', '.join(allergens[1])}")
    else:
        print("Allergens: None")
    print(f"Total Price: RM {size[1]}")

def main():
    welcome_gui()
    customer = get_customer_details()
    size = choose_size()
    flavour = choose_flavour()
    toppings = choose_toppings()
    allergens = check_allergens()
    display_order(customer, size, flavour, toppings, allergens)
    thank_you_gui()

if __name__ == "__main__":
    main()
