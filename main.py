from mainProducts import mainProducts
from mainInventory import mainInventory
from mainInventManager import mainInventoryManager

def mainMenu ():
    print('\n<<Main Menu - Navigate with the following options>>')
    print('1- Products options.\n2- Inventory options\n3- Invetory manager options\n4- Exit')


def main ():
    op = 0
    products = []
    inventories = []
    inventoryManagers = []
    
    while op >= 0:
        mainMenu()
        op = int(input('\nChoose an option: '))
        while op <= 0:
            mainMenu()
            op = int(input('\nChoose valid option: '))

        if op == 1:
            mainProducts(products, inventories)
        
        elif op == 2:
            mainInventory(inventories, products)
            
        elif op == 3:
            mainInventoryManager()
        
        elif op == 4:
            print('\nGoodbye, thanks for use this software.')
            break        
        
main()