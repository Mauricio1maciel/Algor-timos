def contar_divisores(numero):
   
    quantidade_divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            quantidade_divisores += 1
    
    return quantidade_divisores

numero = int(input("Digite um número inteiro e positivo: "))

if numero > 0:
   
    print("O número",numero,"tem ",contar_divisores(numero)," divisores.")
else:
    print("O número deve ser inteiro e positivo.")
