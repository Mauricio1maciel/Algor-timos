codigo1,numero_peças1,valor_cada_peca1 = input().split()

codigo1 =int(codigo1)
numero_peças1=int(numero_peças1)
valor_cada_peca1 =float(valor_cada_peca1)

codigo2,numero_peças2,valor_cada_peca2 = input().split()

codigo2 =int(codigo2)
numero_peças2=int(numero_peças2)
valor_cada_peca2 =float(valor_cada_peca2)
totalaPagar = (numero_peças1 * valor_cada_peca1) + (numero_peças2 * valor_cada_peca2) 
print("VALOR A PAGAR: R$ %.2f"%totalaPagar)
