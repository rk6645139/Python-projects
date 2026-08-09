import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import uuid

# File paths
PIZZA_FILE = "pizzas.json"
ORDER_FILE = "orders.json"

# Initialize pizza data if not exists
if not os.path.exists(PIZZA_FILE):
    with open(PIZZA_FILE, "w") as f:
        json.dump([
            {"name": "Margherita", "price": 5},
            {"name": "Pepperoni", "price": 7},
            {"name": "Veggie", "price": 6}
        ], f)

# Initialize orders data
if not os.path.exists(ORDER_FILE):
    with open(ORDER_FILE, "w") as f:
        json.dump([], f)

# Load pizza data
def load_pizzas():
    with open(PIZZA_FILE, "r") as f:
        return json.load(f)

# Save a new order
def save_order(order):
    with open(ORDER_FILE, "r") as f:
        orders = json.load(f)
    orders.append(order)
    with open(ORDER_FILE, "w") as f:
        json.dump(orders, f, indent=4)

# Check order status
def check_order_status(order_id):
    with open(ORDER_FILE, "r") as f:
        orders = json.load(f)
    for order in orders:
        if order["id"] == order_id:
            return order
    return None

# GUI App
class PizzaDeliveryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Delivery App 🍕")
        self.root.geometry("400x400")
        
        self.pizzas = load_pizzas()
        
        # Pizza selection
        tk.Label(root, text="Select Pizza:").pack(pady=5)
        self.pizza_var = tk.StringVar()
        pizza_names = [f"{p['name']} (${p['price']})" for p in self.pizzas]
        self.pizza_combo = ttk.Combobox(root, values=pizza_names, state="readonly", textvariable=self.pizza_var)
        self.pizza_combo.pack(pady=5)
        self.pizza_combo.current(0)

        # Quantity selection
        tk.Label(root, text="Quantity:").pack(pady=5)
        self.quantity_spin = tk.Spinbox(root, from_=1, to=10)
        self.quantity_spin.pack(pady=5)
        
        # Place Order button
        tk.Button(root, text="Place Order", command=self.place_order).pack(pady=10)

        # Separator
        ttk.Separator(root, orient='horizontal').pack(fill='x', pady=10)

        # Order Status Check
        tk.Label(root, text="Enter Order ID to Check Status:").pack(pady=5)
        self.order_id_entry = tk.Entry(root)
        self.order_id_entry.pack(pady=5)
        tk.Button(root, text="Check Status", command=self.check_status).pack(pady=10)

    def place_order(self):
        pizza_index = self.pizza_combo.current()
        pizza = self.pizzas[pizza_index]
        quantity = int(self.quantity_spin.get())
        order_id = str(uuid.uuid4())[:8]
        order = {
            "id": order_id,
            "pizza": pizza["name"],
            "quantity": quantity,
            "status": "Pending"
        }
        save_order(order)
        messagebox.showinfo("Order Placed", f"Your order ID is: {order_id}")

    def check_status(self):
        order_id = self.order_id_entry.get()
        if not order_id:
            messagebox.showwarning("Input Error", "Please enter an order ID!")
            return
        order = check_order_status(order_id)
        if order:
            status = f"Order ID: {order['id']}\nPizza: {order['pizza']}\nQuantity: {order['quantity']}\nStatus: {order['status']}"
            messagebox.showinfo("Order Status", status)
        else:
            messagebox.showerror("Not Found", "Order ID not found!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaDeliveryApp(root)
    root.mainloop()
