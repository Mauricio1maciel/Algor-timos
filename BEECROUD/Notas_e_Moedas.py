valor = float(input())
centavos = int(valor * 100)
notas = [10000, 5000, 2000, 1000, 500, 200]
print("NOTAS:")
if valor >= 100:
    notas_100 = int(valor // 100)
    print(notas_100, "nota(s) de R$ 100.00")
    valor %= 100
else:
    print("0 nota(s) de R$ 100.00")
if valor >= 50:
    notas_50 = int(valor // 50)
    print(notas_50, "nota(s) de R$ 50.00")
    valor %= 50
else:
    print("0 nota(s) de R$ 50.00")
if valor >= 20:
    notas_20 = int(valor // 20)
    print(notas_20, "nota(s) de R$ 20.00")
    valor %= 20
else:
    print("0 nota(s) de R$ 20.00")
if valor >= 10:
    notas_10 = int(valor // 10)
    print(notas_10, "nota(s) de R$ 10.00")
    valor %= 10
else:
    print("0 nota(s) de R$ 10.00")
if valor >= 5:
    notas_5 = int(valor // 5)
    print(notas_5, "nota(s) de R$ 5.00")
    valor %= 5
else:
    print("0 nota(s) de R$ 5.00")
if valor >= 2:
    notas_2 = int(valor // 2)
    print(notas_2, "nota(s) de R$ 2.00")
    valor %= 2
else:
    print("0 nota(s) de R$ 2.00")
print("MOEDAS:")
if valor >= 1:
    moedas_1 = int(valor)
    print(moedas_1, "moeda(s) de R$ 1.00")
    valor %= 1
else:
    print("0 moeda(s) de R$ 1.00")
if valor >= 0.50:
    moedas_50 = int(valor // 0.50)
    print(moedas_50, "moeda(s) de R$ 0.50")
    valor %= 0.50
else:
    print("0 moeda(s) de R$ 0.50")
if valor >= 0.25:
    moedas_25 = int(valor // 0.25)
    print(moedas_25, "moeda(s) de R$ 0.25")
    valor %= 0.25
else:
    print("0 moeda(s) de R$ 0.25")
if valor >= 0.10:
    moedas_10 = int(valor // 0.10)
    print(moedas_10, "moeda(s) de R$ 0.10")
    valor %= 0.10
else:
    print("0 moeda(s) de R$ 0.10")
if valor >= 0.05:
    moedas_5 = int(valor // 0.05)
    print(moedas_5, "moeda(s) de R$ 0.05")
    valor %= 0.05
else:
    print("0 moeda(s) de R$ 0.05")
if valor >= 0.01:
    moedas_1 = int(valor / 0.01)
    print(moedas_1, "moeda(s) de R$ 0.01")
else:
    print("0 moeda(s) de R$ 0.01")

#valor = float(input())
#centavos = int(valor * 100)
#notas = [10000, 5000, 2000, 1000, 500, 200]

#print("NOTAS:")
#for nota in notas:
#    qtd_notas = centavos // nota
#   print("{:>3} nota(s) de R$ {:5.2f}".format(qtd_notas, nota/100))
#    centavos %= nota

#print("MOEDAS:")
#moedas = [100, 50, 25, 10, 5, 1]
#for moeda in moedas:
#   qtd_moedas = centavos // moeda
#   print("{:>3} moeda(s) de R$ {:5.2f}".format(qtd_moedas, moeda/100))
#   centavos %= moeda
