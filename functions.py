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
     

