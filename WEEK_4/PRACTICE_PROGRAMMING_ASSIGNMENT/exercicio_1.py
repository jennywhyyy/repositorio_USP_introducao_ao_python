n = int(input("Digite um número inteiro: "))

if (n % 2 == 0) or (n % 3 == 0 and n != 3) or (n % 5 == 0 and n != 5) or (n % 7 == 0 and n != 7):
    print("não primo")
else:
    print ("primo")
