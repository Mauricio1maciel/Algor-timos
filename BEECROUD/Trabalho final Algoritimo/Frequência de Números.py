N = int(input())
frequecia = {}
for _ in range(N):
    vezes = int(input())
    if vezes in frequecia:
        frequecia[vezes] = frequecia[vezes] + 1
    else:
        frequecia[vezes] = 1
for numero in sorted(frequecia.keys()):
    print("%d aparece %d vez(es)"%(numero, frequecia[numero]))