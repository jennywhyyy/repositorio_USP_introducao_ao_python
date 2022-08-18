def maior_elemento(lista):
    clone = lista[:]
    maior = []

    for i in clone:
        if i not in maior:
            maior.append(i)

    n = -1
    while maior[n] < maior[n+1]:
        n += 1

    return (maior[n])
