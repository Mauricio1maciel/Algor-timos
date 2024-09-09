def dividir_sacolas(N, sacolas):
    # Verifica se a soma total de caramelos é par
    total_caramelos = sum(sacolas)
    if total_caramelos % 2 != 0:
        return -1
    
    # Tentaremos dividir as sacolas para que a soma de cada parte seja metade do total
    metade = total_caramelos // 2
    
    # Para armazenar as duas partes (Alice e Bob)
    parte_Alice = []
    soma_Alice = 0
    
    # Tentando encontrar uma combinação de sacolas que some metade
    for i, caramelo in enumerate(sacolas):
        if soma_Alice + caramelo <= metade:
            parte_Alice.append(i + 1)  # Guardamos o índice da sacola
            soma_Alice += caramelo
        
        # Se já atingimos a soma desejada, podemos parar
        if soma_Alice == metade:
            break
    
    # Se conseguimos distribuir corretamente
    if soma_Alice == metade:
        parte_Bob = [i + 1 for i in range(N) if (i + 1) not in parte_Alice]
        return parte_Alice, parte_Bob
    
    return -1

# Leitura da entrada
N = int(input())  # Número de sacolas
sacolas = list(map(int, input().split()))  # Quantidade de caramelos em cada sacola

# Resultado
resultado = dividir_sacolas(N, sacolas)

# Impressão da saída
if resultado == -1:
    print(-1)
else:
    parte_Alice, parte_Bob = resultado
    print("Alice:", ' '.join(map(str, parte_Alice)))
    print("Bob:", ' '.join(map(str, parte_Bob)))
