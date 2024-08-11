camisetas = int(input("Informe a quantidade de camisetas que serão encomendadas: "))

if camisetas <= 30:
    valor_unitario = 25.50
else:
    valor_unitario = 20.50

valor_total = camisetas * valor_unitario

print("O valor de cada camiseta será de R$", valor_unitario)
print("O valor total a ser pago será de R$" ,valor_total)
