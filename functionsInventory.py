from constants import *
from classes import Inventory

def showInventory (inventories):
    if len(inventories) <= 0:
        print('\nNo inventories loaded, please add some first using option 2.')
    else:
        month = str(input('\nEnter month: ')).upper()
        while month not in MONTHS:
            month = str(input('Enter a valid month: ')).upper()
    
    for inventory in inventories:
        if inventory.month == month:
            print('\n|Month: ', inventory.month)
            for product in inventory.products:
                print(product)
            print('\nTotal budget: $', inventory.calculateTotalBudget())

def createInventory(inventories, products):
    month = str(input('\nEnter month: ')).upper()
    while month not in MONTHS:
        month = str(input('Enter valid month: ')).upper()

    if products:
        prods = products
    else:
        print('\nNot products loaded. Create products first.')
        return

    inv = Inventory(month, prods, '')
    inventories.append(inv)

def deleteInventoryByMonth(inventories):
    pass