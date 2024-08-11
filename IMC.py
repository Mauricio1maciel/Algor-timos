peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura(em metros): "))
IMC = peso / (altura*altura) 
if  IMC < 0.00185:
    print ("Você está abaixo do peso ideal")
elif IMC  <= 0.00249:
        print ("Parabéns — você está em seu peso normal!")
elif IMC <= 0.00299:
    print("Você está acima de seu peso (sobrepeso)")
elif IMC <= 0.00349:
    print("Obesidade grau I")
elif IMC <= 0.00399:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
    
print("Seu IMC é:",IMC)