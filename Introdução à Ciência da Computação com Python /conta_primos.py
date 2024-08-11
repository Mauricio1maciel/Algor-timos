def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_primos(n):
    count = 0
    for num in range(2, n + 1):
        if eh_primo(num):
            count += 1
    return count
