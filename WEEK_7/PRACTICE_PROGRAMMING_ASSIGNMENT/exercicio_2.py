def eh_hipotenusa(a, b):
    x = (a*a) + (b*b)
    hipotenusa = x
    return hipotenusa


def hipotenusas(n):
    c = 1
    soma = 0
    a = 0
    b = 0
    i = 0
    while (c <= n):
        i = (c * c)
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (i == eh_hipotenusa(a,b)):
                    soma = soma + c
                    a = n
                b += 1
            a += 1
            b = a
        c += 1
    return soma


def soma_hipotenusas(n):
    if n <= 1:
        soma_hipotenusas()
        
    return(hipotenusas(n))
