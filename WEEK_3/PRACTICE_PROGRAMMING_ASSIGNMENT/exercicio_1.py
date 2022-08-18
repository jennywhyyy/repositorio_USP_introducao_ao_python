import math

coordenada1_x = float(input("Insira a coordenada x do primeiro ponto cartesiano: "))
coordenada1_y = float(input("Insira a coordenada y do primeiro ponto cartesiano: "))
coordenada2_x = float(input("Insira a coordenada x do segundo ponto cartesiano: "))
coordenada2_y = float(input("insira a coordenada y do segundo ponto cartesiano: "))
distancia = math.sqrt((coordenada1_x - coordenada2_x) **2 + (coordenada1_y - coordenada2_y) **2)

if distancia >= 10:
    print("longe")

else:
    print("perto")

