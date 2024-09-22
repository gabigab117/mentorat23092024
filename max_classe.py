class Product:
    def __init__(self, name: str, price: float, discount: float = 0):
        self.name = name
        self.price = price
        self.discount = discount

    def get_final_price(self):
        return self.price * (1-self.discount)


products = [Product("pomme", 1.5), Product("banane", 0.5, 0.1), Product("cerise", 1.5, 0.2)]

expensive_product = max(products, key=Product.get_final_price)
expensive_product_bis = max(products, key=lambda p: p.price)  # Prend le premier qu'il rencontre en cas d'égalité

print(expensive_product.name)
print(expensive_product_bis.name)
