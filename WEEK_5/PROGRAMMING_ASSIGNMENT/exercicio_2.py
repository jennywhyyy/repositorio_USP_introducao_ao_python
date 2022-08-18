def ehprimo (k):
    fator = 2
    while k % fator != 0 and fator <= k / 2:
        fator += 1
    if k % fator == 0:
        return False
    else:
        return True

def maior_primo(n):
    maior_numero = 0
    i = 2
    while i <= n:
        if ehprimo(i):
            maior_numero = i
        i += 1
    return maior_numero
    
            
        
    




   
