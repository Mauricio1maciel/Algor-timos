A1 = int(input())
A2 = int(input())
A3 = int(input())
if A1 >= 0 and A1 <= 1000 and A2 >= 0 and A2 <= 1000 and A3 >= 0 and A3 <= 1000:
    tempoA1 = (A2 * 2) + (A3 * 4)
    tempoA2 = (A1 * 2) + (A3 * 2)
    tempoA3 = (A1 * 4) + (A2 * 2)
    menortempo = float('inf')
    if tempoA1 < menortempo:
        menortempo = tempoA1
    if tempoA2 < menortempo:
        menortempo = tempoA2
    if tempoA3 < menortempo:
        menortempo = tempoA3
print(menortempo)