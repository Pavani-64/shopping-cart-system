class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.pid in self.items:
            self.items[product.pid]['quantity'] += quantity
        else:
            self.items[product.pid] = {
                'product': product,
                'quantity': quantity
            }

    def remove_item(self, pid):
        if pid in self.items:
            del self.items[pid]
        else:
            print("Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n--- Your Cart ---")
        for item in self.items.values():
            p = item['product']
            q = item['quantity']
            print(f"{p.pid} | {p.name} | ₹{p.price} x {q} = ₹{p.price * q}")

    def calculate_total(self):
        total = sum(
            item['product'].price * item['quantity']
            for item in self.items.values()
        )

        tax = total * 0.05
        discount = 0.1 * total if total > 1000 else 0

        final_total = total + tax - discount

        return total, tax, discount, final_total