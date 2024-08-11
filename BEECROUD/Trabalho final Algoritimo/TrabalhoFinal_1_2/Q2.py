def Print_Tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print(f" {tabuleiro[i][j]} ", end='')
            if j < 2:
                print("|", end='')
        print()
        if i < 2:
            print("---|---|---")

def Quem_Ganhou(tabuleiro, jogador_atual):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return True
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return True
    return False

def Empatou(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                return False
    return True

tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
jogador_atual = 'X'

print("O jogo vai começar, X será o iniciante!")

while True:
    Print_Tabuleiro(tabuleiro)
    try:
        linha, coluna = map(int, input("Jogador %s , digite sua jogada (linha e coluna, 1 a 3): "%jogador_atual).split())
    except ValueError:
        print("Entrada inválida! Por favor, digite dois números separados por espaço.")
        continue

    if linha < 1 or linha > 3 or coluna < 1 or coluna > 3 or tabuleiro[linha - 1][coluna - 1] != ' ':
        print("Jogada inválida! Tente novamente.")
        continue

    tabuleiro[linha - 1][coluna - 1] = jogador_atual

    if Quem_Ganhou(tabuleiro, jogador_atual):
        Print_Tabuleiro(tabuleiro)
        print("Jogador %s venceu!"%jogador_atual)
        break

    if Empatou(tabuleiro):
        Print_Tabuleiro(tabuleiro)
        print("O jogo empatou!")
        break

    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
