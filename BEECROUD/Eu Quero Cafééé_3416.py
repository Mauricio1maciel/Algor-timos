import math
N, L, D,  =input().split()
N = int(N)
L = int(L)
D = int(D)
total_necessario_cafe = N * D
litros_cafe = total_necessario_cafe / 1000
minimo_preparacoes = math.ceil(litros_cafe / L)
litros_preparados = minimo_preparacoes * L
print(litros_preparados)