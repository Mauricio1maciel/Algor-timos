import os

class ClasseListaSimples:
    def __init__(self, f):
        self.lista = [0]*10
        self.Fim = f
    
    def ListaVazia(self):
        if self.Fim == -1:
            return True
        else:
            return False

    def ValidaInsercao(self):
        print("")
    
    def ValidaLimiteLista(self):
        print("")
    
    def InserirValorFimLista(self,valor):
        print("")
    
    def InserirK_esimoValorLista(self,valor,k):
        print("")
	
    def InserirAposK_esimoValorLista(self,valor,k):
        print("")
	
    def RemoverK_esimoValorLista(self,k):
        print("")
	
    def MostrarLista(self):
        print("")
    
    def RetornarK_esimoElemento(self,k):
        print("")


ListaObj = ClasseListaSimples(-1)
while True:
    os.system('cls')
    print("1 - Inserir no fim da lista.")
    print("2 - Inserir valor no K-esimo indice da lista.")
    print("3 - Inserir valor apos o K-esimo indice da lista.")
    print("4 - Remover K-esimo valor da lista.")
    print("5 - Retornar K-ésimo elemento da lista.")
    print("6 - Mostrar lista.")
    print("0 - Sair.")
    OP = int(input("Entre com a operação desejada: "))
    if OP == 0:
        break
    elif OP == 4:
        if ListaObj.ListaVazia():
            print("A lista ainda se encontra vazia.")
        else:
            print("")
    input("Digite uma tecla para continuar.")  