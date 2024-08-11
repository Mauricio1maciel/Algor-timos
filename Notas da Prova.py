notas = int(input())
if notas == 0:
    conceito = 'E'
elif 1 <= notas <= 35:
    conceito = 'D'
elif 36 <= notas <= 60:
    conceito = 'C'
elif 61 <= notas <= 85:
    conceito = 'B'
else:
    conceito = 'A'
print(conceito)

