def fibo(n):
    fib = [0, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

T = int(input())

for _ in range(T):
    N = int(input())
    print(f"Fib({N}) = {fibo(N)}")