b = int(input("digite a largura: "))
h = int(input("digite a altura: "))
largura = 0
altura = 0

while altura < h:
    while largura < b:
        largura += 1
        print("#", end="")
    altura += 1
    largura = 0
    print("")
