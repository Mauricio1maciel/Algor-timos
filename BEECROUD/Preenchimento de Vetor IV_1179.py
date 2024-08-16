pares = []
impares = []
for _ in range(15):
    valor = int(input().strip())

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    if len(pares) == 5:
        for i in range(5):
            print(f"par[{i}] = {pares[i]}")
        pares = [] 

    if len(impares) == 5:
        for i in range(5):
            print(f"impar[{i}] = {impares[i]}")
        impares = [] 

if impares:
    for i in range(len(impares)):
        print(f"impar[{i}] = {impares[i]}")

if pares:
    for i in range(len(pares)):
        print(f"par[{i}] = {pares[i]}")
