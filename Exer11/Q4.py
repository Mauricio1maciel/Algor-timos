def fatorial(numero):
   
    if numero == 0 or numero == 1:
        return 1
    
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    
    return resultado

numero = int(input("Digite um número inteiro e positivo: "))

if numero >= 0:
    
    print("O fatorial de",numero, "é",fatorial(numero),".")
else:
    print("O número deve ser inteiro e positivo.")
