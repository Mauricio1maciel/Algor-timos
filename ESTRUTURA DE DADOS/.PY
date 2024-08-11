import os

def LerVetor(VET):
    for i in range(10):
        VET.append(int(input("Entre com o valor %d: "% i)))

def MostrarVetor(vetor,VET):
    print("Valores do vetor %d."%vetor)
    for i in range (10):
        print("[%d] = %d."%(i, VET[i]))

def CriarVetor2(VET1, VET2):
    VET2 = VET1[::-1]
    return VET2

def CriarVetor3(VET1, VET3, valor):
    VET3 = [x * valor for x in VET1]
    return VET3

def CriarVetor4(VET1, VET4, valor):
    VET4 = [1 if x == valor else 0 for x in VET1]
    return VET4

def CriarVetor5(VET1, VET5, valor):
    VET5 = [x for x in VET1 if x >= valor]
    return VET5

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []
valor3 = 0
valor4 = 0
valor5 = 0

while(True):
    os.system("clear")
    print("1. Entre com um vetor de 10 inteiros.")
    print("2. Criar um vetor 2.")
    print("3. Criar um vetor 3.")
    print("4. Criar um vetor 4.")
    print("5. Criar um vetor 5.")
    print("6. Mostrar vetores saida.")
    print("0. Sair.")
    opcao = int(input("Entre com a opcao desejada: "))
    if opcao == 0:
        break
    elif opcao == 1:
        LerVetor(vetor1)
    elif opcao == 2:
        if vetor1:
            vetor2 = CriarVetor2(vetor1, vetor2)
        else:
            print("Vetor 1 não criado.")
            input()
    elif opcao == 3:
        if vetor1:
            valor3 = int(input("Entre com o valor para multiplicar: "))
            vetor3 = CriarVetor3(vetor1, vetor3, valor3)
        else:
            print("Vetor 1 não criado.")
            input()
    elif opcao == 4:
        if vetor1:
            valor4 = int(input("Entre com o valor para comparar: "))
            vetor4 = CriarVetor4(vetor1, vetor4, valor4)
        else:
            print("Vetor 1 não criado.")
            input()
    elif opcao == 5:
        if vetor1:
            valor5 = int(input("Entre com o valor para filtrar: "))
            vetor5 = CriarVetor5(vetor1, vetor5, valor5)
        else:
            print("Vetor 1 não criado.")
            input()
    elif opcao == 6:
        MostrarVetor(1, vetor1)
        if vetor2:
            MostrarVetor(2, vetor2)
        if vetor3:
            print("Valor informado para vetor 3: ", valor3)
            MostrarVetor(3, vetor3)
        if vetor4:
            print("Valor informado para vetor 4: ", valor4)
            MostrarVetor(4, vetor4)
        if vetor5:
            print("Valor informado para vetor 5: ", valor5)
            MostrarVetor(5, vetor5)
        input()