import json
from product import Product

FILE_NAME = "data.json"

def save_cart(cart):
    data = []
    for item in cart.items.values():
        data.append({
            "pid": item['product'].pid,
            "name": item['product'].name,
            "price": item['product'].price,
            "quantity": item['quantity']
        })

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def load_cart(cart):
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)

        for item in data:
            product = Product(item["pid"], item["name"], item["price"])
            cart.add_item(product, item["quantity"])

    except FileNotFoundError:
        pass