N = int(input())
for _ in range(N):
    nome = input()
    notas =input().split()
   
    P1 = P2 = T = R = None
    # Convertendo as notas conforme o número de entradas
    if len(notas) == 1:
        P1 = float(notas[0])
        P2 = 0 # Se só tem uma prova, a segunda é zero
        media = (P1 + P2) / 2
    elif len(notas) == 2:
        P1 = float(notas[0])
        P2 = float(notas[1])
        media = (P1 + P2) / 2
    elif len(notas) == 3:
        P1 = float(notas[0])
        P2 = float(notas[1])
        T  = float(notas[2])
        media = (P1 + P2 + T) / 3
    elif len(notas) == 4:
        P1 = float(notas[0])
        P2 = float(notas[1])
        T  = float(notas[2])
        R  = float(notas[3])
        # Identificando a menor nota entre P1, P2 e T
        if P1 <= P2 and P1 <= T:
          menor_nota = P1
        elif P2 <= P1 and P2 <= T:
          menor_nota = P2
        else:
         menor_nota = T
    
        # Substituindo a menor nota pela substitutiva se for maior
        if R > menor_nota:
            if menor_nota == P1:
                P1 = R
            elif menor_nota == P2:
                P2 = R
            else:
                T = R

        media = (P1 + P2 + T) / 3

   
    
    print(f"{nome}: {media:.1f}")