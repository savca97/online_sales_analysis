class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_products(self, product):
        self.products.append(product)
    
    def display_all_products(self):
        for product in self.products:
            print(product.display_info())
    
    def total_inventory_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total
    
    def remove_products(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]