imposto_de_renda = float(input())
if imposto_de_renda <= 2000.00:
    imposto = "Isento"
elif imposto_de_renda <= 3000.00:
    imposto = (imposto_de_renda - 2000.00) * 0.08
elif imposto_de_renda <= 4500.00:
    imposto = (imposto_de_renda - 3000.00) * 0.18 + 1000.00 * 0.08
else:
    imposto = (imposto_de_renda - 4500.00) * 0.28 + 1500.00 * 0.18 + 1000.00 * 0.08
if imposto == "Isento":
    print("Isento")
else:
    print("R$ {:.2f}".format(imposto))