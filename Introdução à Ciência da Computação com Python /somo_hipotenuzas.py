import math

def é_hipotenusa(i):
    for j in range(1, i):
        k = math.sqrt(i*i - j*j)
        if k.is_integer():
            return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for i in range(1, n + 1):
        if é_hipotenusa(i):
            soma += i
    return soma
