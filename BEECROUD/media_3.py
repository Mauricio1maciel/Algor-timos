n1, n2, n3, n4 =input().split()
n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)
p1=2
p2=3
p3=4
p4=1
media=(n1*p1+n2*p2+n3*p3+n4*p4)/(p1+p2+p3+p4)
print("Media: %.1f" %media)
if  5.0<=media<7.0:
    print("Aluno em exame.")
    nota_exame=float(input())
    print("Nota do exame: %.1f" %nota_exame)
    media_final=(media+nota_exame)/2
    if media_final>=5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" %media_final)
else:
   if media>=7.0:
        print("Aluno aprovado.")
   else:
        print("Aluno reprovado.")
