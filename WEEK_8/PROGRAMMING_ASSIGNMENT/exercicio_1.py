def remove_repetidos(lista):
    clone = lista[:]
    remove = []
    clone.sort()

    for i in clone:
        if i not in remove:
            remove.append(i)

    remove.sort()
    return(remove)
    
