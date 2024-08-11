votos_dormir = 0
votos_estudar = 0
votos_passear = 0
votos_outros = 0
total_votos = 0

print("O que você mais gosta de fazer nos finais de semana?")
print("1) Dormir")
print("2) Estudar algoritmos")
print("3) Passear")
print("4) Outros")
print("5) Sair")

while True:
    voto = int(input("Digite o número correspondente à sua escolha (ou 5 para sair): "))
    
    if voto == 1:
        votos_dormir += 1
    elif voto == 2:
        votos_estudar += 1
    elif voto == 3:
        votos_passear += 1
    elif voto == 4:
        votos_outros += 1
    elif voto == 5:
        break
    else:
        print("Escolha inválida. Por favor, escolha um número de 1 a 5.")

    total_votos += 1

percentual_dormir = (votos_dormir / total_votos) * 100
percentual_estudar = (votos_estudar / total_votos) * 100
percentual_passear = (votos_passear / total_votos) * 100
percentual_outros = (votos_outros / total_votos) * 100

print("Estatísticas da enquete:")
print("Total de votos: ",total_votos)
print("Votos em Dormir: ",votos_dormir, "(%.2f%%)"%percentual_dormir)
print("Votos em Estudar: ",votos_estudar, "(%.2f%%)"%percentual_estudar)
print("Votos em Passear: ",votos_passear, "(%.2f%%)"%percentual_passear)
print("Votos em Outros: ",votos_outros, "(%.2f%%)"%percentual_outros)

mais_votado = "Dormir"
votos_mais_votado = votos_dormir

if votos_estudar > votos_mais_votado:
    mais_votado = "Estudar"
    votos_mais_votado = votos_estudar

if votos_passear > votos_mais_votado:
    mais_votado = "Passear"
    votos_mais_votado = votos_passear

if votos_outros > votos_mais_votado:
    mais_votado = "Outros"
print("A escolha mais votada é" ,mais_votado,".")
