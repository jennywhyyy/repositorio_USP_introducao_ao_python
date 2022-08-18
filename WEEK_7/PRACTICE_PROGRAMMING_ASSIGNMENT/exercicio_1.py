def ehprimo (k):
    fator = 2
    while k % fator != 0 and fator <= k / 2:
        fator += 1
    if k % fator == 0:
        return False
    else:
        return True

def n_primos(n):
    quantidade = 1
    i = 2
    
    while i <= n:
        if ehprimo(i):
            quantidade += 1
        i += 1
            
    return quantidade
    
            
        
    




   
