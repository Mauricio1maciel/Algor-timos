alunos = int(input("Informe quantos alunos tem na turma: "))
media = 0
soma_notas = 0
for i in range(0,alunos,1):
    nota = float(input("Informe a nota de cada aluno: "))
    soma_notas += nota
media = soma_notas / alunos
print ("A media da turma eh %.2f"%media)