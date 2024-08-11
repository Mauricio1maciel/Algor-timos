A, G, KMlA, KMlG = input().split()
A =float(A)
G =float(G)
KMlA =float(KMlA)
KMlG =float(KMlG)
consumoA = A / KMlA
consumoG = G / KMlG
if consumoA < consumoG:
    print('A')
else:
    print('G')