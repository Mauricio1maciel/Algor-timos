grenais = 0
interV = 0
gremioV = 0
empates = 0

while True:
    gol_inter, gol_gremio = map(int, input().split())

    grenais = grenais + 1
    if gol_inter > gol_gremio:
        interV = interV + 1
    elif gol_gremio > gol_inter:
        gremioV = gremioV + 1
    else:
        empates = empates + 1

    print("Novo grenal (1-sim 2-nao)")
    novoGR = int(input())
    if novoGR == 2:
        break

print(grenais ,"grenais")
print("Inter:", interV)
print("Gremio:", gremioV)
print("Empates:", empates)

if interV > gremioV:
    print("Inter venceu mais")
elif gremioV > interV:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")