A = []
for i in range(100):
    valor = float(input())
    A.append(valor)
for i in range(100):
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")
