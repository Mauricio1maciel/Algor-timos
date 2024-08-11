nome = input("Informe seu nome: ")
ddd = int(input("Informe o DDD do telefone que você deseja ligar: "))
if ddd == 49:
    regiao = "para o velho Oeste"
elif ddd == 48:
    regiao = "para o litoral"
elif ddd == 47:
    regiao = "para a região de Joinville"
else:
    regiao = "para fora de SC"
print("Olá,",nome)
print(nome," ,você ligou para um telefone  ",regiao)
