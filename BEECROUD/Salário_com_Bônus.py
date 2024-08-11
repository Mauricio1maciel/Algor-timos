nome_vendedor = input()
salario = float(input())
vendas_efetuadas = float(input())
total_de_comissao = vendas_efetuadas * 0.15
Sal_total= salario + total_de_comissao
print("TOTAL = R$ %.2f" %Sal_total)