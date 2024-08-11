while True:
    Rodadas = int(input())
    if Rodadas == 0:
        break
    
    jogador1_pontos = 0
    jogador2_pontos = 0
    
    for _ in range(Rodadas):
        A, B = input().split()
        A = int(A)
        B = int(B)
        if A > B:
            jogador1_pontos += 1
        elif B > A:
            jogador2_pontos += 1
    
    print(jogador1_pontos, jogador2_pontos)
