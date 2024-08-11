numero = int(input("Digite um número inteiro: "))

soma_dos_digitos = 0
for digito in str(numero):
    soma_dos_digitos += int(digito)
print( soma_dos_digitos)
