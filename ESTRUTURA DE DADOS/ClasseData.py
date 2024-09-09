import os

class ClasseData:
    def __init__(self, Dia, Mes, Ano):
        self.Dia = Dia
        self.Mes = Mes
        self.Ano = Ano

    def MostrarData(self):
        return '%0.2d/%0.2d/%0.4d' % (self.Dia, self.Mes, self.Ano)

    def AlteraData(self, D, M, A):
        self.Dia = D
        self.Mes = M
        self.Ano = A

    def VerificaBissexto(self):
        if self.Ano % 400 == 0:
            return True
        elif self.Ano % 4 == 0 and self.Ano % 100 != 0:
            return True
        else:
            return False
        
    def ValidaData(self):
        if self.Dia < 1:
            return False
        elif self.Mes < 1 or self.Mes > 12:
            return False
        elif self.Ano < 1900 or self.Ano > 9999:
            return False
        elif self.Mes in [4, 6, 9, 11] and self.Dia > 30:
            return False
        elif self.Mes in [1, 3, 5, 7, 8, 10, 12] and self.Dia > 31:
            return False
        elif self.Mes == 2 and self.VerificaBissexto() and self.Dia > 29:
            return False
        elif self.Mes == 2 and not self.VerificaBissexto() and self.Dia > 28:
            return False
        else:
            return True

    def MostrarDataExtenso(self):
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                 "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        MES = meses[self.Mes - 1]
        print("%d de %s de %d\n" % (self.Dia, MES, self.Ano))
        
    def AdicionarDiasData(self, Dias):
        for D in range(Dias):
            self.Dia += 1
            if self.Mes in [4, 6, 9, 11] and self.Dia > 30:
                self.Mes += 1
                self.Dia = 1
            elif self.Mes in [1, 3, 5, 7, 8, 10, 12] and self.Dia > 31:
                if self.Mes == 12:
                    self.Mes = 1
                    self.Dia = 1
                    self.Ano += 1
                else:      
                    self.Mes += 1
                    self.Dia = 1
            elif self.Mes == 2 and self.VerificaBissexto() and self.Dia > 29:
                self.Mes += 1
                self.Dia = 1
            elif self.Mes == 2 and not self.VerificaBissexto() and self.Dia > 28:
                self.Mes += 1
                self.Dia = 1

    def RetornaPascoa(self):
        a = self.Ano % 19
        b = self.Ano // 100
        c = self.Ano % 100
        d = b // 4
        e = b % 4
        g = (8 * b + 13) // 25
        h = (19 * a + b - d - g + 15) % 30
        j = c // 4
        k = c % 4
        m = (a + 11 * h) // 319
        r = (2 * e + 2 * j - k - h + m + 32) % 7
        n = (h - m + r + 90) // 25
        p = (h - m + r + n + 19) % 32

        return ClasseData(p, n, self.Ano)

DataInformada = False          
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1 - Informar nova data.")
    print("2 - Verificar se o ano é bissexto.")
    print("3 - Adicionar dias na data.")
    print("4 - Mostrar data extenso.")
    print("5 - Verificar dia da Páscoa.")
    print("6 - Verificar dia do carnaval.")
    print("0 - Sair.")
    OP = int(input("Entre com a operação desejada: "))
    
    if OP == 0:
        break
    elif OP == 1:
        D, M, A = map(int, input("Entre com a data formato DD MM YYYY: ").split())
        Data = ClasseData(D, M, A)
        if Data.ValidaData():
            print("Data informada: ", Data.MostrarData())
            DataInformada = True
        else:
            print("Data informada é inválida.")
            DataInformada = False
    elif OP == 2:
        if DataInformada:
            Data.MostrarDataExtenso()
            if Data.VerificaBissexto():
                print("O ano de %d é bissexto" % Data.Ano)
            else:
                print("O ano de %d não é bissexto" % Data.Ano)
        else:
            print("Favor informar uma data válida para usar esta funcionalidade.")
    elif OP == 3:
        if DataInformada:
            Dias = int(input("Entre com o número de dias a adicionar: "))
            Data.AdicionarDiasData(Dias)
            print("Nova data: ", Data.MostrarData())
        else:
            print("Favor informar uma data válida para usar esta funcionalidade.")
    elif OP == 4:
        if DataInformada:
            Data.MostrarDataExtenso()
        else:
            print("Favor informar uma data válida para usar esta funcionalidade.")
    elif OP == 5:
        if DataInformada:
            Pascoa = Data.RetornaPascoa()
            print("A Páscoa em %d será em: " % Data.Ano)
            Pascoa.MostrarDataExtenso()
        else:
            print("Favor informar uma data válida para usar esta funcionalidade.")
    input("Digite uma tecla para continuar.")
