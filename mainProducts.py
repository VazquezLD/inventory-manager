from classes import *
from constants import *
from functionsProducts import *

def mainProducts ():
    products = []
    
    op = 0
    
    while op >= 0:
        menu('Product')
        op = int(input('\nChoose an option: '))
        while op <= 0:
            menu('Product')
            op = int(input('\nChoose valid option: '))

        if op == 1:
            if len(products) <= 0:
                print('\nNo products loaded, please add some first using option 2.')
            else:
                showProducts(products)
        
        elif op == 2:
            createProduct(products)
        
        elif op == 3:
            if len(products) <= 0:
                print('\nNo products loaded, please add some first using option 2.')
            else:
                id = int(input('\nEnter id (if exists te product will be deleted): '))
                deleteProductById(id, products)
        
        elif op == 4:
            return