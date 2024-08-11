meses_extenso = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}
dia = int(input("Digite o dia (inteiro): "))
mes = int(input("Digite o mês (inteiro): "))
ano = int(input("Digite o ano (inteiro): "))
if mes in meses_extenso:
    print("Chapecó," ,dia, "/",meses_extenso[mes], "/",ano)
else:
    print("Mês inválido.")
