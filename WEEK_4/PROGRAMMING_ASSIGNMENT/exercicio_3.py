num = int(input("Digite um número inteiro, cujos algoritmos serão somados: "))

if num >= 10:
    soma = 0
    while num != 0:
        resto = num % 10
        num = (num - resto) // 10
        soma = soma + resto
    print(soma)
else:
    print(num)
    
        
