class Product:
    def __init__ (self, id=0, name='', category='', price=0, quantity=0):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"| ID: {str(self.id):^5} "
                f"| NAME: {self.name:^5} "
                f"| CATEGORY: {self.category:^5} "
                f"| PRICE: ${self.price:^5} "
                f"| QUANTITY: {self.quantity:^5} |")
    
        
class Inventory:
    def __init__ (self, month='', products=[], inventoryManager=''):
        self.month = month
        self.products = products
        self.inventoryManager = inventoryManager
        
    def calculateTotalBudget (products):
        if products:
            cont = 0
            for product in products:
                cont += product.price
        else:
            cont = 0
        return cont
        

class InventoryManager:
    def __init__ (self, name='', lastname='', age=18, sex='', inventory=None):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.inventory = inventory 
    
    def __str__(self):
        return (f"| NAME: {str(self.name):^5} "
                f"| LASTNAME: {self.lastname:^5} "
                f"| AGE: {self.age:^5} "
                f"| SEX: ${self.sex:^5} "
                f"| INVENTORY: {self.inventory:^5} |")


