import tkinter as tk
from tkinter import messagebox
from product import Product
from cart import Cart
from storage import save_cart, load_cart
from auth import signup, login

BG_COLOR = "#1e1e2f"
TEXT_COLOR = "white"
BTN_COLOR = "#4CAF50"

cart = Cart()
load_cart(cart)
product_id = 1


# ================= LOGIN FUNCTIONS =================
def handle_login():
    user = username_entry.get()
    pwd = password_entry.get()

    if login(user, pwd):
        messagebox.showinfo("Success", "Login successful!")
        login_frame.pack_forget()
        main_app()
    else:
        messagebox.showerror("Error", "Invalid credentials!")


def handle_signup():
    user = username_entry.get()
    pwd = password_entry.get()

    if signup(user, pwd):
        messagebox.showinfo("Success", "Account created!")
    else:
        messagebox.showerror("Error", "User already exists!")


# ================= MAIN APP =================
def main_app():
    global name_entry, price_entry, qty_entry
    global cart_list, remove_entry, coupon_entry, bill_text
    global category_var

    main_frame = tk.Frame(root, bg=BG_COLOR)
    main_frame.pack(fill="both", expand=True)

    tk.Label(main_frame, text="🛍️ Shopping Cart",
             font=("Arial", 18, "bold"),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

    # Inputs
    name_entry = tk.Entry(main_frame)
    name_entry.pack()

    price_entry = tk.Entry(main_frame)
    price_entry.pack()

    qty_entry = tk.Entry(main_frame)
    qty_entry.pack()

    category_var = tk.StringVar(value="Electronics")
    tk.OptionMenu(main_frame, category_var,
                  "Electronics", "Clothing", "Food").pack()

    tk.Button(main_frame, text="Add Item",
              bg=BTN_COLOR, fg="white",
              command=add_item).pack(pady=5)

    cart_list = tk.Listbox(main_frame, width=60)
    cart_list.pack()

    remove_entry = tk.Entry(main_frame)
    remove_entry.pack()

    tk.Button(main_frame, text="Remove",
              bg="red", fg="white",
              command=remove_item).pack(pady=5)

    coupon_entry = tk.Entry(main_frame)
    coupon_entry.pack()

    tk.Button(main_frame, text="Checkout",
              bg="green", fg="white",
              command=checkout).pack()

    bill_text = tk.Text(main_frame, height=8)
    bill_text.pack()

    tk.Button(main_frame, text="Save & Exit",
              command=save_and_exit).pack(pady=10)

    view_cart()


# ================= CART FUNCTIONS =================
def add_item():
    global product_id
    try:
        p = Product(product_id, name_entry.get(), float(price_entry.get()))
        cart.add_item(p, int(qty_entry.get()))
        product_id += 1
        view_cart()
    except:
        messagebox.showerror("Error", "Invalid input!")


def remove_item():
    try:
        cart.remove_item(int(remove_entry.get()))
        view_cart()
    except:
        messagebox.showerror("Error", "Invalid ID!")


def view_cart():
    cart_list.delete(0, tk.END)
    for item in cart.items.values():
        p = item['product']
        cart_list.insert(tk.END, f"{p.pid} | {p.name}")


def checkout():
    total, tax, discount, final = cart.calculate_total()
    bill_text.delete("1.0", tk.END)
    bill_text.insert(tk.END, f"Final: ₹{final}")


def save_and_exit():
    save_cart(cart)
    root.destroy()


# ================= GUI ROOT =================
root = tk.Tk()
root.title("Login System")
root.geometry("400x400")
root.configure(bg=BG_COLOR)

login_frame = tk.Frame(root, bg=BG_COLOR)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Login / Signup",
         font=("Arial", 16),
         fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=20)

username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

tk.Button(login_frame, text="Login",
          bg=BTN_COLOR, fg="white",
          command=handle_login).pack(pady=5)

tk.Button(login_frame, text="Signup",
          command=handle_signup).pack(pady=5)

root.mainloop()