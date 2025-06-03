from functionsProducts import menu

def mainInventoryManager ():
    inventoryManagers = []
    op = 0
    
    while op >= 0:
        menu('Inventory Manager')
        op = int(input('\nChoose an option: '))
        while op <= 0:
            menu('Inventory Manager')
            op = int(input('\nChoose valid option: '))

        if op == 1:
            pass
        
        elif op == 2:
            pass
        
        elif op == 3:
            pass
        
        elif op == 4:
            return