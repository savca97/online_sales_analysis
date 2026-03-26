from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 1000, 10)
product2 = Product("Phone", 500, 20)
product3 = Product("Headphones", 50, 30)

manager.add_products(product1)
manager.add_products(product2)
manager.add_products(product3)

manager.display_all_products()
print(f"Total inventory value: {manager.total_inventory_value()}")