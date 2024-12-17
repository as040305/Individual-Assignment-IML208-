import tkinter as tk
from tkinter import messagebox

order_database = []

def create_order():
    def submit_order():
        new_order = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "address": address_entry.get(),
            "cake_size": size_entry.get(),
            "flavour": flavour_entry.get(),
            "toppings": toppings_entry.get(),
            "allergens": allergens_entry.get(),  # Added allergens field
        }
        order_database.append(new_order)
        messagebox.showinfo("Success", "Order created successfully!")
        root.destroy()

    root = tk.Tk()
    root.title("Create Order")
    root.geometry("600x450")  # Larger window size

    tk.Label(root, text="Customer Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Phone Number:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(root, font=("Arial", 12))
    phone_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Address:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
    address_entry = tk.Entry(root, font=("Arial", 12))
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(root, text="Cake Size:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
    size_entry = tk.Entry(root, font=("Arial", 12))
    size_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(root, text="Flavour:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10)
    flavour_entry = tk.Entry(root, font=("Arial", 12))
    flavour_entry.grid(row=4, column=1, padx=10, pady=10)

    tk.Label(root, text="Toppings:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=10)
    toppings_entry = tk.Entry(root, font=("Arial", 12))
    toppings_entry.grid(row=5, column=1, padx=10, pady=10)

    tk.Label(root, text="Allergens:", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=10)  # Added allergens label
    allergens_entry = tk.Entry(root, font=("Arial", 12))
    allergens_entry.grid(row=6, column=1, padx=10, pady=10)  # Added allergens entry

    tk.Button(root, text="Submit", command=submit_order, font=("Arial", 14)).grid(row=7, column=0, columnspan=2, pady=20)

    root.mainloop()

def read_orders():
    root = tk.Tk()
    root.title("All Orders")
    root.geometry("600x450")  # Larger window size

    if not order_database:
        tk.Label(root, text="No orders available.", font=("Arial", 14)).pack(pady=20)
    else:
        for idx, order in enumerate(order_database, start=1):
            tk.Label(root, text=f"Order {idx}:", font=("Arial", 12)).pack(anchor="w", padx=20)
            for key, value in order.items():
                tk.Label(root, text=f"{key.capitalize()}: {value}", font=("Arial", 12)).pack(anchor="w", padx=40)
            tk.Label(root, text="", font=("Arial", 12)).pack()  # Spacer

    tk.Button(root, text="Close", command=root.destroy, font=("Arial", 14)).pack(pady=20)

    root.mainloop()

def update_order():
    def select_order():
        try:
            idx = int(order_idx_entry.get()) - 1
            if 0 <= idx < len(order_database):
                order = order_database[idx]
                update_fields(order)
            else:
                messagebox.showerror("Error", "Invalid order number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def update_fields(order):
        def submit_update():
            order["name"] = name_entry.get()
            order["phone"] = phone_entry.get()
            order["address"] = address_entry.get()
            order["cake_size"] = size_entry.get()
            order["flavour"] = flavour_entry.get()
            order["toppings"] = toppings_entry.get()
            order["allergens"] = allergens_entry.get()  # Updated allergens
            messagebox.showinfo("Success", "Order updated successfully!")
            root.destroy()

        tk.Label(root, text="Update Fields:", font=("Arial", 14)).grid(row=2, column=0, columnspan=2)

        tk.Label(root, text="Customer Name:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
        name_entry = tk.Entry(root, font=("Arial", 12))
        name_entry.insert(0, order["name"])
        name_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(root, text="Phone Number:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(root, font=("Arial", 12))
        phone_entry.insert(0, order["phone"])
        phone_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(root, text="Address:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=10)
        address_entry = tk.Entry(root, font=("Arial", 12))
        address_entry.insert(0, order["address"])
        address_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(root, text="Cake Size:", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=10)
        size_entry = tk.Entry(root, font=("Arial", 12))
        size_entry.insert(0, order["cake_size"])
        size_entry.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(root, text="Flavour:", font=("Arial", 12)).grid(row=7, column=0, padx=10, pady=10)
        flavour_entry = tk.Entry(root, font=("Arial", 12))
        flavour_entry.insert(0, order["flavour"])
        flavour_entry.grid(row=7, column=1, padx=10, pady=10)

        tk.Label(root, text="Toppings:", font=("Arial", 12)).grid(row=8, column=0, padx=10, pady=10)
        toppings_entry = tk.Entry(root, font=("Arial", 12))
        toppings_entry.insert(0, order["toppings"])
        toppings_entry.grid(row=8, column=1, padx=10, pady=10)

        tk.Label(root, text="Allergens:", font=("Arial", 12)).grid(row=9, column=0, padx=10, pady=10)  # Added allergens label
        allergens_entry = tk.Entry(root, font=("Arial", 12))
        allergens_entry.insert(0, order["allergens"])  # Pre-fill with existing allergens
        allergens_entry.grid(row=9, column=1, padx=10, pady=10)  # Added allergens entry

        tk.Button(root, text="Submit", command=submit_update, font=("Arial", 14)).grid(row=10, column=0, columnspan=2, pady=20)

    root = tk.Tk()
    root.title("Update Order")
    root.geometry("600x450")  # Larger window size

    tk.Label(root, text="Enter Order Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    order_idx_entry = tk.Entry(root, font=("Arial", 12))
    order_idx_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Select", command=select_order, font=("Arial", 14)).grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def delete_order():
    def submit_delete():
        try:
            idx = int(order_idx_entry.get()) - 1
            if 0 <= idx < len(order_database):
                del order_database[idx]
                messagebox.showinfo("Success", "Order deleted successfully!")
                root.destroy()
            else:
                messagebox.showerror("Error", "Invalid order number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    root = tk.Tk()
    root.title("Delete Order")
    root.geometry("600x450")  # Larger window size

    tk.Label(root, text="Enter Order Number to Delete:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    order_idx_entry = tk.Entry(root, font=("Arial", 12))
    order_idx_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Delete", command=submit_delete, font=("Arial", 14)).grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def main_menu():
    root = tk.Tk()
    root.title("Order Management System")
    root.geometry("600x450")  # Larger window size

    tk.Button(root, text="Create Order", command=create_order, font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Read Orders", command=read_orders, font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Update Order", command=update_order, font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Delete Order", command=delete_order, font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 14)).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
