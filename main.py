from classes import *
from constants import *
from functions import *

def main ():
    inventories = []
    inventoriesManagers = []
    products = []
    
    op = -1
    
    while op <= 0:
        menu()
        op = int(input('\nChoose an option: '))
        while op <= 0:
            menu()
            op = int(input('\nChoose valid option: '))

        if op == 1:
            if len(products) <= 0:
                op = int(input('\nNo products loaded, please choose another: '))
                while op <= 0:
                    menu()
                    op = int(input('\nChoose valid option: '))
            else:
                pass
        
        elif op == 2:
            
            id = int(input('\nEnter product id: '))
            while id < 0 or id > 1000:
                id = int(input('Enter valid id: '))
                
            name = str(input('\nEnter product name: '))
            while len(name) <= 2:
                name = str(input('Enter valid name: '))
                
            category = str(input('\nEnter product category: '))
            while category not in CATEGORIES:
                category = str(input('Enter valid category: '))
                
            price = float(input('\nEnter product price: '))
            while price <= 0:
                price = float(input('Enter valid price: '))
            
            quantity = int(input('\nEnter product quantity: '))
            while quantity <= 0:
                quantity = int(input('Enter valid quantity: '))
            
            newProd = Product(id ,name ,category ,price ,quantity)
            addInOrder(newProd, products)
            print('\nADDED NEW PRODUCT --> ', newProd, 'SUCCESSFULLY.')
            

        elif op == 3:
            pass
        
        elif op == 4:
            pass
        
        elif op == 5:
            print('\nGoodbye ! Thanks for use this software.')
            return
main()