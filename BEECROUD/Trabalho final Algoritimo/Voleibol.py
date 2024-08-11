N = int(input())
total_S = 0
total_B = 0
total_A = 0
total_S1 = 0
total_B1 = 0
total_A1 = 0
for i in range(N):
    nome = input()
    S,B , A = input().split()
    S1,B1 , A1 = input().split()
    S = int(S)
    B = int(B)
    A = int(A)
    S1 = int(S1)
    B1 = int(B1)
    A1 = int(A1)
    total_S = total_S + S
    total_B = total_B + B
    total_A = total_A + A
    total_S1 = total_S1 + S1
    total_B1 = total_B1 + B1
    total_A1 = total_A1 + A1
Persentual_Saque = (total_S1 / total_S) * 100
Persentual_Bloqueio = (total_B1 / total_B) * 100
Persentual_Aaque = (total_A1 / total_A) * 100
print("Pontos de Saque: %.2f %%."%Persentual_Saque)
print("Pontos de Bloqueio: %.2f %%."%Persentual_Bloqueio)
print("Pontos de Ataque: %.2f %%."%Persentual_Aaque)