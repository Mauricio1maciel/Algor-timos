nome_jogador1 = input("Nome do jogador 1: ")
opcao_jogador1 = int(input(nome_jogador1 + ", escolha a opção (1 - Ímpar, 2 - Par): "))
jogada_jogador1 = int(input(nome_jogador1 + ", faça sua jogada: "))

nome_jogador2 = input("Nome do jogador 2: ")
opcao_jogador2 = int(input(nome_jogador2 + ", escolha a opção (1 - Ímpar, 2 - Par): "))
jogada_jogador2 = int(input(nome_jogador2 + ", faça sua jogada: "))

soma_jogadas = jogada_jogador1 + jogada_jogador2

if(opcao_jogador1 == 1 and opcao_jogador2 == 1):
 if soma_jogadas % 2:
     print("Houve empate!")
 else:
    print("Niguem ganhou!")
elif(soma_jogadas % 2 == 0 and opcao_jogador1 == 2) or (soma_jogadas % 2 != 0 and opcao_jogador1 == 1):
    print("Jogador", nome_jogador1, "ganhou!")
elif (soma_jogadas % 2 == 0 and opcao_jogador2 == 2) or (soma_jogadas % 2 != 0 and opcao_jogador2 == 1):
    print("Jogador", nome_jogador2, "ganhou!")

