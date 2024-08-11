salario = float(input("Informe seu salario: "))
tempo_trabalhado = int(input("Informe quantos anos trabalha na empresa: "))

reajuste = 0

if tempo_trabalhado <= 5:
    reajuste = 0.03
elif 6 <= tempo_trabalhado <= 10:
    reajuste = 0.05
elif 11 <= tempo_trabalhado <= 15:
    reajuste = 0.08
else:
    reajuste = 0.10
novo_salario = salario * (1 + reajuste)

print("O funcionario tem", tempo_trabalhado, "anos de servico obteve", reajuste * 100, "% de reajuste ficando com salario =", novo_salario)