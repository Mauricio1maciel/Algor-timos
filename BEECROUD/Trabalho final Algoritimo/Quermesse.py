testando = 1

while True:
    N= int(input())
    if  N == 0:
        break
    
    ingressos = list(map(int, input().split()))
    
    Ganhador = None
    for i in range(N):
        if ingressos[i] == i + 1:
            Ganhador = ingressos[i]
            break
    
    print("Teste %d" % testando)
    print("%d" % Ganhador)
    print("")
    
    testando = testando + 1