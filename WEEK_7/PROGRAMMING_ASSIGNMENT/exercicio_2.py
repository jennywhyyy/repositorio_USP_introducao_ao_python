b = int(input("digite a largura: "))
h = int(input("digite a altura: "))
largura = 0
altura = 0
base1 = 0
base2 = 0
meio = 0

while altura < h:
    while base1 < b:
        base1 += 1
        print("#", end="")

    print("")
    h = h - 2
    
    while meio < h:
        meio += 1
        print("#" + " " * (b - 3), "#")
        
    while base2 < b:
        base2 += 1
        print("#", end="")

    altura += 1

