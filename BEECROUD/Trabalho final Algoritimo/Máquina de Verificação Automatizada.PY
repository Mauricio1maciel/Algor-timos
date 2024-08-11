entrada1 = input().split()
X1 = int(entrada1[0])
X2 = int(entrada1[1])
X3 = int(entrada1[2])
X4 = int(entrada1[3])
X5 = int(entrada1[4])

entrada2 = input().split()
Y1 = int(entrada2[0])
Y2 = int(entrada2[1])
Y3 = int(entrada2[2])
Y4 = int(entrada2[3])
Y5 = int(entrada2[4])

compatíveis = True

if X1 == Y1 or X2 == Y2 or X3 == Y3 or X4 == Y4 or X5 == Y5:
    compatíveis = False

if compatíveis:
    print("Y")
else:
    print("N")
