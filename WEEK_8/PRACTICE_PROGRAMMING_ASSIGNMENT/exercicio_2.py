lista = []
n = (int(input("Digite um número inteiro: ")))

if n != 0:
    lista.append(n)

while n != 0:
    n = int(input("Digite um número inteiro: "))
    lista.append(n)

c = (len(lista)) - 1

del lista[c]

a = (len(lista) * (-1))
b = -1

while b >= a:
    print (lista[b])
    b += -1
