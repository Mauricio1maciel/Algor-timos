def InicializaData(D,M,A):
    Data = []
    Data.append(D)
    Data.append(M)
    Data.append(A)
    return Data

def MostrarData(Data):
    Dia = Data[0] 
    Mes = Data[1] 
    Ano = Data[2] 
    print("%02d/%02d/%04d."%(Dia,Mes,Ano))

def MostrarDataExtenso(Data):
    Dia = Data[0] 
    Mes = Data[1] 
    Ano = Data[2] 
    if (Mes == 1):
        MES = "janeiro"
    elif (Mes == 2):
        MES = "fevereiro"
    elif (Mes == 3):
        MES = "março"
    elif (Mes == 4):
        MES = "abril"
    elif (Mes == 5):
        MES = "maio"
    elif (Mes == 6):
        MES = "junho"
    elif (Mes == 7):
        MES = "julho"
    elif (Mes == 8):
        MES = "agosto"
    elif (Mes == 9):
        MES = "setembro"
    elif (Mes == 10):
        MES = "outubro"
    elif (Mes == 11):
        MES = "novembro"
    elif (Mes == 12):
        MES = "dezembro"    
    print("%d de %s de %d"%(Dia,MES,Ano))


def VerificaBissexto(Ano):
    if (Ano % 400 == 0):
        return True
    elif((Ano % 4 == 0)and(Ano % 100 != 0)):
        return True
    else:
        return False

def ValidaData(Data):
    Dia = Data[0] 
    Mes = Data[1] 
    Ano = Data[2] 
    if(Dia < 1):
        return False
    elif(Mes < 1 or Mes > 12):
        return False
    elif(Ano < 1900 or Ano > 9999):
        return False
    elif((Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11)and(Dia > 30)):
        return False
    elif((Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7
        or Mes == 8 or Mes == 10 or Mes == 12)and(Dia > 31)):
        return False
    elif(Mes == 2 and VerificaBissexto(Ano) and Dia > 29):
        return False
    elif(Mes == 2 and not VerificaBissexto(Ano) and Dia > 28):
        return False
    else:
        return True


def AdicionarDiasData(Dias,Data):
    Dia = Data[0] 
    Mes = Data[1] 
    Ano = Data[2] 
    for D in range(Dias):
        Dia+=1
        if((Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11)and(Dia > 30)):
            Mes+=1
            Dia = 1
        elif((Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7
           or Mes == 8 or Mes == 10 or Mes == 12)and(Dia > 31)):
            if(Mes == 12):
                Mes = 1
                Dia = 1
                Ano+=1
            else:
                Mes+=1
                Dia = 1
        elif(Mes == 2 and VerificaBissexto(Ano) and Dia > 29):
            Mes+=1
            Dia = 1
        elif(Mes == 2 and not VerificaBissexto(Ano) and Dia > 28):
            Mes+=1
            Dia = 1
    Data[0] = Dia
    Data[1] = Mes
    Data[2] = Ano
    
  
