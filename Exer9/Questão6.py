N=int(input("Digite o número de casos de teste: "))
for _ in range(N):
    X=int(input("Digite um número inteiro positivo: "))
    if X<=1:
        print(X, "nao eh primo")
    else:
        primo=True
        for i in range(2, int(X ** 0.5) + 1):
            if X%i==0:
                primo=False
                break
        if primo:
            print(X, "eh primo")
        else:
            print(X, "nao eh primo")
