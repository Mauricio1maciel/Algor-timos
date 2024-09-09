#include <stdio.h>
#include <stdlib.h>

#define LimpaTela system("cls");

class ClasseListaSimples
{
public:
	ClasseListaSimples(int f);
	bool ListaVazia();
	bool ValidaInsercao(int k);
	bool ValidaLimiteLista(int k);
	void InserirValorFimLista(int valor);
	void InserirK_esimoValorLista(int valor, int k);
	void InserirAposK_esimoValorLista(int valor, int k);
	int RemoverK_esimoValorLista(int k);
	void MostrarLista();
	int RetornarK_esimoElemento(int k);
private:
	int lista[10];
	int fim;
};

ClasseListaSimples::ClasseListaSimples(int f)
{
	fim = f;
}

bool ClasseListaSimples::ListaVazia()
{
	if(fim == -1)
		return true;
	else
		return false;
}

bool ClasseListaSimples::ValidaInsercao(int k)
{
	//TODO Generated function
	if(k > fim|| k < 0){
		return true;	
	}
	else{
	return false;
	}
}

bool ClasseListaSimples::ValidaLimiteLista(int k)
{
	//TODO Generated function
	if (fim + 1 == 10 ){
		return true;
	}
	else{
		return false;
	}
	
}

void ClasseListaSimples::InserirValorFimLista(int valor)
{
	//TODO Generated function
}


void ClasseListaSimples::InserirK_esimoValorLista(int valor, int k)
{
	//TODO Generated function
	if (k > fim || k < 0){ 
		 printf("K-ÉSIMO ELEMENTO NÃO EXISTE\n");
   }else if( fim == 10){
	printf("LISTA CHEIA\n");
   }else{
     int i = fim;
	while(i > k){
       lista[i] = lista[i - 1];
	   i--;
	}
	lista[k + 1] = valor;
	(fim)++;
	}
}

void ClasseListaSimples::InserirAposK_esimoValorLista(int valor, int k)
{
	//TODO Generated function
}

int ClasseListaSimples::RemoverK_esimoValorLista(int k)
{
	//TODO Generated function
	if(k > fim || k < 0){
		printf("K-ÉSIMO ELEMENTO NÃO EXISTE\n");
		return -1;
	}else{
		int valor = lista[k];
		while(k < fim - 1){
			lista[k] = lista[k + 1];
			k++;
		}
		fim--;
	    return valor;
	}
	
}

void ClasseListaSimples::MostrarLista()
{
	//TODO Generated function
}

int ClasseListaSimples::RetornarK_esimoElemento(int k)
{
	//TODO Generated function
	return 0;
}


int main()
{
	int OP;
	ClasseListaSimples ListaObj(-1);
	while(1)
	{
		LimpaTela;
		printf("1 - Inserir no fim da lista.\n");
		printf("2 - Inserir valor no K-esimo indice da lista.\n");
		printf("3 - Inserir valor apos o K-esimo indice da lista.\n");
		printf("4 - Remover K-esimo valor da lista.\n");
		printf("5 - Retornar K-�simo elemento da lista.\n");
		printf("6 - Mostrar lista.\n");
		printf("0 - Sair.\n");
		printf("Entre com a opcao: ");
		scanf("%d", &OP);
		if (OP == 0)
			break;
		else if(OP == 1)
		{

		}
		else if(OP == 4)
		{
			if(ListaObj.ListaVazia())
				printf("A lista ainda se encontra vazia.\n");
			else
			{

			}
		}
		system("pause");
	}
}
