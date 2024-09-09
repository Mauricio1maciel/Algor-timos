A, B, C,  =input().split()
A = int(A)
B = int(B)
C = int(C)
A1, B1, C1,  =input().split()
A1 = int(A1)
B1 = int(B1)
C1 = int(C1)
R1 = 0
R2 = 0
R3 = 0
if A < A1:
   R1 = A1 - A
if B < B1:
   R2 = B1 - B
if C < C1:
   R3 = C1 - C
print(R1+R2+R3)