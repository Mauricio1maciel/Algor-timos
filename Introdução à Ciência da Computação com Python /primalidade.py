
numero = int(input())

if numero <= 1:
    eh_primo = False
else:
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break


if eh_primo:
    print("primo")
else:
    print("não primo")
