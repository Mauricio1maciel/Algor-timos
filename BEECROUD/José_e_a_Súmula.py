N = int(input())
for _ in range(N):
    registro = input().split()
    prime_ou_segun = int(registro[0])
    tempo = registro[1]

    if tempo == '1T':
        tempo_corrido = prime_ou_segun
    elif tempo == '2T':
        tempo_corrido = 45 + prime_ou_segun
    
    if tempo_corrido <= 45:
        print(tempo_corrido)
    elif  tempo_corrido > 45 and tempo_corrido <= 90:
        m_porrogados = tempo_corrido - 45
        print("45+%d"%m_porrogados)
    else:
        m_extra = tempo_corrido - 90
        print("90+%d"%m_extra)