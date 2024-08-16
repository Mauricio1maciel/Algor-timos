N = int(input())
Valo = input().split()
menor_valor = int(Valo[0])  
indice_menor = 0
for i in range(1,N):
    Valor_atual = int(Valo[i])
    if Valor_atual < menor_valor:
        menor_valor = Valor_atual
        indice_menor = i
print("Menor valor: %d"%menor_valor)
print("Posicao: %d"%indice_menor)

