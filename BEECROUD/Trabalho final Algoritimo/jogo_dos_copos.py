N = int(input())
posicao_inicial = input()    
posicao_Moeda = posicao_inicial   
for _ in range(N):
    movimentos = int(input())
    if movimentos == 1:
        if posicao_Moeda == 'A':
            posicao_Moeda = 'B'
        elif posicao_Moeda == 'B':
            posicao_Moeda = 'A'
    elif movimentos == 2:
        if posicao_Moeda == 'B':
            posicao_Moeda = 'C'
        elif posicao_Moeda == 'C':
            posicao_Moeda = 'B'
    elif movimentos == 3:
        if posicao_Moeda == 'A':
            posicao_Moeda = 'C'
        elif posicao_Moeda == 'C':
            posicao_Moeda = 'A'
print(posicao_Moeda)