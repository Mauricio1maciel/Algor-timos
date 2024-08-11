numero = input("Digite um número inteiro: ")

tem_adj_iguais = False

for i in range(len(numero) - 1):
    if numero[i] == numero[i + 1]:
        tem_adj_iguais = True
        break

if tem_adj_iguais:
    print("sim")
else:
    print("não")
