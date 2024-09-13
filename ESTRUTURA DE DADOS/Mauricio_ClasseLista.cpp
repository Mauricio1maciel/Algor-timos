	#include <stdio.h>
	#include <stdlib.h>

	#define LimpaTela system("cls");

	class ClasseListaSimples
	{
	public:
		//Construtor da classe
		ClasseListaSimples(int f);
		//Verifica se a lista est� vazia
		bool ListaVazia();
		//Faz a verificacao se a Lista esta cheia
		bool ValidaInsercao();
		//Faz a verificacao se o k est� dentre o inicio(0) e o fim(f)  
		bool ValidaLimiteLista(int k);
		//Insere valor no fim da lista
		void InserirValorFimLista(int valor);
		//Insere o valor no indice k desejado
		void InserirK_esimoValorLista(int valor, int k);
		//Insere o valor depois do indice k desejado
		void InserirAposK_esimoValorLista(int valor, int k);
		//Remove o valor do indice k desejado
		int RemoverK_esimoValorLista(int k);
		//Mostra lista obedecendo o limite(f) ja inserido
		void MostrarLista();
		//Retorna o valor do indice k desejado
		int RetornarK_esimoElemento(int k);
	private:
		int info[10];
		int f;
	};

	ClasseListaSimples::ClasseListaSimples(int fim)
	{
		f = fim;
	}

	bool ClasseListaSimples::ListaVazia()
	{
		if(f == -1)
			return true;
		else
			return false;
	}

	bool ClasseListaSimples::ValidaInsercao()
	{
		//Aqui � um c�digo que vai ser utilizado varias vezes, 
		//Aqui verifica de o f atingiu o final do tamanho da lista
		if (f == 9 ){
			return true;
		}
		else{
			return false;
		}
	}

	bool ClasseListaSimples::ValidaLimiteLista(int k)
	{
		//Aqui � um c�digo que vai ser utilizado varias vezes, 
		//por isso foi criada uma fun��o - se  k > f  ou  k < 0 entao 
		
		if(k > f || k < 0){
			return true;	
		}
		else{
		return false;
		}
	}

	void ClasseListaSimples::InserirValorFimLista(int valor)
	{
		//Inserir o valor no fim(f) da lista.
		//Aumenta o f e insere o valor, n�o tem rearanjo.
		if(ValidaInsercao()){
			printf("LISTA CHEIA\n");
		}else{
			info[f + 1] = valor;
			f++;
		}
	}

	void ClasseListaSimples::InserirK_esimoValorLista(int valor, int k)
	{
		//Pseudocodigo 3 do material
		if (ValidaLimiteLista(k)){ 
			printf("K-ÉSIMO ELEMENTO NÃO EXISTE\n");
	    }else if(ValidaInsercao()){
		  printf("LISTA CHEIA\n");
	    }else{
		  int i = f;
		  while(i >= k){
		  info[i + 1] = info[i];
		  i--;
		}
		info[k] = valor;
		f++;
		}
	}

	void ClasseListaSimples::InserirAposK_esimoValorLista(int valor, int k)
	{
		//Pseudocodigo 2 do material
		if(ValidaLimiteLista(k)){
			printf("K-ÉSIMO ELEMENTO NÃO EXISTE\n");
		}else if(ValidaInsercao()){
			printf("LISTA CHEIA\n");
		}else{
			int i = f;
			while(i > k){
				info[i + 1] = info[i];
				i--;
			}
			info[k + 1] = valor;
			f++;
		}
	}

	int ClasseListaSimples::RemoverK_esimoValorLista(int k)
	{
		//Pseudocodigo 4 do material
		if(ValidaLimiteLista(k)){
			printf("K-ÉSIMO ELEMENTO NÃO EXISTE\n");
			return -1;
		}else{
			int valor = info[k];
			while(k < f){
				info[k] = info[k + 1];
				k++;
			}
			f--;
			return valor;
		}
	}

	void ClasseListaSimples::MostrarLista()
	{
		//Mostrar � percorrer a lista at� o controle f
		int i = 0;
        while(i <= f){
           printf("%d ", info[i]);
           i++;
        }
        printf("\n");
	}

	int ClasseListaSimples::RetornarK_esimoElemento(int k)
	{
		//Pseudocodigo 1 do material
		if(ValidaLimiteLista(k)){
			printf("Elemento não existe\n");
			return -1;
		}else{
			int valor = info[k];
			return valor;
		}
		
	}


	int main()
{
    int OP, valor, k;
    ClasseListaSimples ListaObj(-1);
    
    while (1)
    {
        LimpaTela;
        printf("1 - Inserir no fim da lista.\n");
        printf("2 - Inserir valor no K-ésimo índice da lista.\n");
        printf("3 - Inserir valor após o K-ésimo índice da lista.\n");
        printf("4 - Remover K-ésimo valor da lista.\n");
        printf("5 - Retornar K-ésimo elemento da lista.\n");
        printf("6 - Mostrar lista.\n");
        printf("0 - Sair.\n");
        printf("Entre com a opcao: ");
        scanf("%d", &OP);
        
        if (OP == 0)
            break;
        else if (OP == 1)
        {
            printf("Entre com o valor para inserir no fim: ");
            scanf("%d", &valor);
            ListaObj.InserirValorFimLista(valor);
        }
        else if (OP == 2)
        {
            printf("Entre com o valor e o índice para inserir: ");
            scanf("%d %d", &valor, &k);
            ListaObj.InserirK_esimoValorLista(valor, k);
        }
        else if (OP == 3)
        {
            printf("Entre com o valor e o índice após o qual inserir: ");
            scanf("%d %d", &valor, &k);
            ListaObj.InserirAposK_esimoValorLista(valor, k);
        }
        else if (OP == 4)
        {
            if (ListaObj.ListaVazia())
                printf("A lista ainda se encontra vazia.\n");
            else
            {
                printf("Entre com o índice para remover: ");
                scanf("%d", &k);
                int removedValue = ListaObj.RemoverK_esimoValorLista(k);
                if (removedValue != -1)
                    printf("Valor removido: %d\n", removedValue);
            }
        }
        else if (OP == 5)
        {
            printf("Entre com o índice para retornar o valor: ");
            scanf("%d", &k);
            int value = ListaObj.RetornarK_esimoElemento(k);
            if (value != -1)
                printf("Valor no índice %d: %d\n", k, value);
        }
        else if (OP == 6)
        {
            ListaObj.MostrarLista();
        }
        else
        {
            printf("Opção inválida. Tente novamente.\n");
        }
        
        system("pause");
    }
    
    return 0;
}
