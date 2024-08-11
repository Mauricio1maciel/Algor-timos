import os

def LerVetor(VET):
    for i in range(10):
        VET.append(int(input("Entre com o valor %d: "% i)))

def MostrarVetor(vetor,VET):
    print("Valores do vetor %d."%vetor)
    for i in range (10):
        print("[%d] = %d."%(i, VET[i]))


vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []

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
	input()
	