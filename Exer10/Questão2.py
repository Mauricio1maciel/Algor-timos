votos_Sertanejo = 0
votos_Funk = 0
votos_Techno = 0
votos_ReB = 0
votos_Axe = 0
total_votos = 0

print("O que você mais gosta de fazer nos finais de semana?")
print("1) Sertanejo")
print("2) Funk")
print("3) Techno")
print("4) R&0B")
print("5) Axe")
print("0) Sair")

while True:
    voto = int(input("Digite o número correspondente à sua escolha (ou 0 para sair): "))
    if voto == 0:
        break
    if voto == 1:
        votos_Sertanejo += 1
    elif voto == 2:
        votos_Funk += 1
    elif voto == 3:
        votos_Techno += 1
    elif voto == 4:
        votos_ReB += 1
    elif voto == 5:
        votos_Axe += 1
    else:
        print("Escolha inválida. Por favor, escolha um número de 0 a 5.")

    total_votos += 1

percentual_Sertanejo = (votos_Sertanejo / total_votos) * 100
percentual_Funk = (votos_Funk / total_votos) * 100
percentual_Techno = (votos_Techno / total_votos) * 100
percentual_ReB = (votos_ReB / total_votos) * 100
percentual_Axe = (votos_Axe / total_votos) * 100


print("Estatísticas da enquete:")
print("Total de votos: ",total_votos)
print("Votos em Sertenejo: ",votos_Sertanejo, "(%.2f%%)"%percentual_Sertanejo)
print("Votos em Funk: ",votos_Funk, "(%.2f%%)"%percentual_Funk)
print("Votos em Techno: ",votos_Techno, "(%.2f%%)"%percentual_Techno)
print("Votos em R&B: ",votos_ReB, "(%.2f%%)"%percentual_ReB)
print("Votos em Axe: ",votos_Axe, "(%.2f%%)"%percentual_Axe)


mais_votado = "Sertanejo"
votos_mais_votado = votos_Sertanejo

if votos_Funk > votos_mais_votado:
    mais_votado = "Funk"
    votos_mais_votado = votos_Funk

if votos_Techno > votos_mais_votado:
    mais_votado = "Techno"
    votos_mais_votado = votos_Techno

if votos_ReB > votos_mais_votado:
    mais_votado = "R&B"

if votos_Axe > votos_mais_votado:
    mais_votado = "Axe"
print("A escolha mais votada é" ,mais_votado,".")
