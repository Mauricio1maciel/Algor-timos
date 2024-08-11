valor = int(input())
print(valor)
notas = [100, 50, 20, 10, 5, 2, 1]
if valor >= 100:
    notas_100 = valor // 100
    print(notas_100, "nota(s) de R$ 100,00")
    valor %= 100
else:
    print("0 nota(s) de R$ 100,00")
if valor >= 50:
    notas_50 = valor // 50
    print(notas_50, "nota(s) de R$ 50,00")
    valor %= 50
else:
    print("0 nota(s) de R$ 50,00")
if valor >= 20:
    notas_20 = valor // 20
    print(notas_20, "nota(s) de R$ 20,00")
    valor %= 20
else:
    print("0 nota(s) de R$ 20,00")
if valor >= 10:
    notas_10 = valor // 10
    print(notas_10, "nota(s) de R$ 10,00")
    valor %= 10
else:
    print("0 nota(s) de R$ 10,00")
if valor >= 5:
    notas_5 = valor // 5
    print(notas_5, "nota(s) de R$ 5,00")
    valor %= 5
else:
    print("0 nota(s) de R$ 5,00")
if valor >= 2:
    notas_2 = valor // 2
    print(notas_2, "nota(s) de R$ 2,00")
    valor %= 2
else:
    print("0 nota(s) de R$ 2,00")
if valor >= 1:
    notas_1 = valor
    print(notas_1, "nota(s) de R$ 1,00")
else:
    print("0 nota(s) de R$ 1,00")
