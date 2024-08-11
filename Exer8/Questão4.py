num = int(input("Digite um número para exibir a tabuada: "))

print("Tabuada do", num, "de 0 até 10:")
for i in range(11):
    resultado = num * i
    print(num, "*", i, "=", resultado)

  