X = []


for i in range(10):
    valor = int(input())
    
    if valor <= 0:
        valor = 1
    X.append(valor)


for i in range(10):
    print(f"X[{i}] = {X[i]}")