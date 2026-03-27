from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

product1 = Product("Laptop", 1000, 10)
product2 = Product("Phone", 500, 20)
product3 = Product("Headphones", 50, 30)

manager.add_products(product1)
manager.add_products(product2)
manager.add_products(product3)
manager.remove_products("Phone")

manager.display_all_products()
print(f"Total inventory value: {manager.total_inventory_value()}")

cart = Cart()

cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

cart.display_cart()
print(f"Total cart value: {cart.total_cart_value()}")