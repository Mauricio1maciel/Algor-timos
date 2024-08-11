horas = int(input("Informe o tempo dedicado ao estudo (em horas por semana): "))
nota  = float(input("Informe a nota que você acha que vai tirar nas provas:"))
if horas < 2 and nota < 6:
    print("VAMOS ESTUDAR UM POUCO MAIS?")
elif horas < 2 and nota >= 6:
    print("VOCE SE ENGANOU.")
elif horas <= 2 and nota < 6:
    print("DEVE SE ACALMAR NA PROVA.")
else:
    print("PODE FICAR TRANQUILO.")