from functionsProducts import menu
from functionsInventory import *

def mainInventory (inventories, products):
    
    op = 0
    
    while op >= 0:
        menu('Inventory')
        op = int(input('\nChoose an option: '))
        while op <= 0:
            menu('Inventory')
            op = int(input('\nChoose valid option: '))

        if op == 1:
            showInventory(inventories)
        
        elif op == 2:
            createInventory(inventories, products)
        
        elif op == 3:
            if len(inventories) <= 0:
                print('\nNo inventories loaded, please add some first using option 2.')
            else:
                month = str(input('\nEnter month: ')).lower()
                while month not in MONTHS:
                    month = str(input('Enter a valid month: ')).lower()
                deleteInventoryByMonth(month, inventories)
        
        elif op == 4:
            return