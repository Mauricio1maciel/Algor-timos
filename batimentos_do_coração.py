idade = int(input("Por favor, insira a sua idade: "))
batimentos_por_minuto = 80
minutos_por_dia = 16 * 60
dias_por_ano = 365.25
total_batidas = idade * batimentos_por_minuto * minutos_por_dia * dias_por_ano
print("O coração de uma pessoa de",idade," anos já bateu aproximadamente",total_batidas,"vezes.")
