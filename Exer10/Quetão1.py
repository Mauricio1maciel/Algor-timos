while True:
    M = int(input("Digite um valor inteiro positivo para M: "))
    N = int(input("Digite um valor inteiro positivo para N: "))
    
    if M >= N:
        print("O valor de M é maior ou igual a N. Terminando o programa.")
        break
    
    soma = M + N
    print("A soma de M e N é:", soma)
