# Cria uma lista com um tamanho fixo
lista = [None] * 10
num_elementos = 0  # Conta o número de elementos válidos na lista

# Lê 10 valores do usuário e os insere na lista
for i in range(10):
    valor = int(input(f'Insira o valor {i+1}: '))

    # Se a lista estiver vazia, insere o valor na primeira posição
    if num_elementos == 0:
        lista[0] = valor
        num_elementos += 1
        continue

    # Percorre a lista para encontrar a posição de inserção
    k = 0
    while k < num_elementos and lista[k] <= valor:
        k += 1

    # Se o valor já está na lista, continua para o próximo valor
    if k > 0 and lista[k-1] == valor:
        continue

    # Desloca os elementos para abrir espaço na posição correta
    for j in range(num_elementos, k, -1):
        lista[j] = lista[j-1]

    # Insere o valor na posição correta
    lista[k] = valor
    num_elementos += 1

# Exibe a lista final, cortando o excesso de elementos None
print("Lista final:", lista[:num_elementos])
