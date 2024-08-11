def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def maior_primo(n):
    for num in range(n, 1, -1):
        if eh_primo(num):
            return num