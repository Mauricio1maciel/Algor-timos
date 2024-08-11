armarios = [False] * 10

while True:
    print("MENU")
    print("1 – Mostrar a situação de todos os armários")
    print("2 – Mostrar os armários livres")
    print("3 – Utilizar Armário")
    print("4 – Remover Armário")
    print("5 – Resumo dos Armários")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        for i in range(1, 11):
            estado = "Ocupado" if armarios[i-1] else "Livre"
            print("Armário %d: %s" % (i, estado))
    elif opcao == '2':
        livres = ["Armário %d" % i for i in range(1, 11) if not armarios[i-1]]
        if livres:
            for livre in livres:
                print(livre)
        else:
            print("Nenhum armário livre.")
    elif opcao == '3':
        numero = int(input("Informe o número do armário a ser utilizado (1 a 10): "))
        if 1 <= numero <= 10:
            if armarios[numero-1]:
                print("ARMÁRIO SENDO UTILIZADO.")
            else:
                armarios[numero-1] = True
                print("Armário %d marcado como ocupado." % numero)
        else:
            print("Armário inválido.")
    elif opcao == '4':
        numero = int(input("Informe o número do armário a ser removido (1 a 10): "))
        if 1 <= numero <= 10:
            if not armarios[numero-1]:
                print("ARMÁRIO NÃO ESTÁ SENDO UTILIZADO.")
            else:
                armarios[numero-1] = False
                print("Armário %d liberado." % numero)
        else:
            print("Armário inválido.")
    elif opcao == '5':
        livres = sum(1 for estado in armarios if not estado)
        ocupados = 10 - livres
        print("%d Armários livres, %d Armários ocupados." % (livres, ocupados))
    elif opcao == '0':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
