N = int(input())
RPM = list(map(int,input().split()))
primeira_queda = 0
for i in range (1,N):
    if RPM[i] < RPM[i-1]:
        primeira_queda = i + 1
        break
print(primeira_queda)