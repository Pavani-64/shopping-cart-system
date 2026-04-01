class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name,
            "price": self.price
        }