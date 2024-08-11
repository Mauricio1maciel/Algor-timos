def Par_ou_Não(numero):
    return numero % 2 == 0
par_ou_impar = int(input("Digite um número inteiro:  "))
if  Par_ou_Não(par_ou_impar):
    print("Número é par")
else:
    print("Número não é par")