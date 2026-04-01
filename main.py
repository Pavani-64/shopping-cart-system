from product import Product
from cart import Cart
from storage import save_cart, load_cart

def show_menu():
    print("\n====== Shopping Cart ======")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Save & Exit")


def main():
    cart = Cart()
    load_cart(cart)

    product_id = 1

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            try:
                price = float(input("Enter price: "))
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input!")
                continue

            product = Product(product_id, name, price)
            cart.add_item(product, qty)
            product_id += 1
            print("Item added successfully!")

        elif choice == '2':
            try:
                pid = int(input("Enter product ID: "))
                cart.remove_item(pid)
            except ValueError:
                print("Invalid ID!")

        elif choice == '3':
            cart.view_cart()

        elif choice == '4':
            total, tax, discount, final = cart.calculate_total()
            print("\n--- Bill Summary ---")
            print(f"Subtotal: ₹{total}")
            print(f"Tax (5%): ₹{tax}")
            print(f"Discount: ₹{discount}")
            print(f"Final Total: ₹{final}")

        elif choice == '5':
            save_cart(cart)
            print("Cart saved. Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()