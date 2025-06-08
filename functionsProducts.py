from classes import *
from constants import *

def addInOrder(product, vect):
    n = len(vect)
    pos = n
    izq, der = 0, n-1
    
    while izq <= der:
        c = (izq+der) // 2
        
        if vect[c].id == product.id:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
        
    vect[pos:pos] = [product]
     
def menu(element):
    print('\n<<', element,'Menu >>')
    print('1- Show', element ,'\n2- Create' , element ,'\n3- Delete', element , '\n4- Save', element,'\n5- Menu')
    
def showProducts(products):
        if len(products) > 0:
            for product in products:
                print(product)
        else:
            print('\nNo products loaded, please add some first using option 2.')

def createProduct(products):
    id = int(input('\nEnter product id: '))
    while id < 0 or id > 1000:
         id = int(input('Enter valid id: '))
                
    name = str(input('\nEnter product name: '))
    while len(name) <= 2:
        name = str(input('Enter valid name: '))
                
    category = str(input('\nEnter product category: ')).upper()
    while category not in CATEGORIES:
        category = str(input('Enter valid category: ')).upper()
                
    price = float(input('\nEnter product price: '))
    while price <= 0:
        price = float(input('Enter valid price: '))
            
    quantity = int(input('\nEnter product quantity: '))
    while quantity <= 0:
        quantity = int(input('Enter valid quantity: '))
            
    newProd = Product(id ,name ,category ,price ,quantity)
    addInOrder(newProd, products)
    print('\nADDED NEW PRODUCT --> ', newProd, 'SUCCESSFULLY.')
    

def deleteProductById (id, products):
    finded = False
    
    for i in range(len(products) - 1):
        if products[i].id == id:
            products.remove(products[i])
            finded = True
    
    if finded:
        print('\nProduct eliminated.')
    else:
        print('\nProduct doesnt match any.')
        

def addProduct (products, inventories):

    inv = str(input('Enter inventory month: ')).upper()
    while inv not in MONTHS:
        inv = str(input('Enter valid month: '))

    for inventory in inventories:
        if inventory.month == inv:
            inventory.products = products
            print('\nProducts added to', inv, 'inventory.')
        print('That month doesnt have any inventory yet.')
    


    
