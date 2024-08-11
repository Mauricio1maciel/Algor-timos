numero_pesquisar = int(input("Digite o número a ser pesquisado: "))

print("Agora, informe mais 10 números inteiros:")

numeros = []

for i in range(10):
    numero = int(input("Digite o",i+1,"º número inteiro: "))
    if numero == numero_pesquisar:
        numero_encontrado = True
if numero_encontrado:
    print("NUMERO ENCONTRADO")
else:
    print("NUMERO NÃO ENCONTRADO")
