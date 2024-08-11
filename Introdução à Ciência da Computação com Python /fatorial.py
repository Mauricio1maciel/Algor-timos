n = int(input("Digite o valor de n: "))
if n < 0:
      print("O número deve ser inteiro e positivo.")
else:
       resultado = 1
       for i in range(2, n + 1):
        resultado *= i
       print(resultado)