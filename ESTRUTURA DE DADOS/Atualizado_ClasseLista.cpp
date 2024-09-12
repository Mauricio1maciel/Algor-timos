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
		bool ValidaInsercao(int k);
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

	bool ClasseListaSimples::ValidaInsercao(int k)
	{
		//Aqui � um c�digo que vai ser utilizado varias vezes, 
		//Aqui verifica de o f atingiu o final do tamanho da lista
		if(k > f || k < 0){
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
		if (f + 1 == 9 ){
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
		if(f == 9){
			printf("LISTA CHEIA\n");
		}else{
			info[f + 1] = valor;
			f++;
		}
	}

	void ClasseListaSimples::InserirK_esimoValorLista(int valor, int k)
	{
		//Pseudocodigo 3 do material
		if (k > f || k < 0){ 
			printf("K-ÉSIMO ELEMENTO NÃO EXISTE\n");
	    }else if( f == 9){
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
		if(k > f || k < 0){
			printf("K-ÉSIMO ELEMENTO NÃO EXISTE\n");
		}else if(f == 9){
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
		if(k > f || k < 0){
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
		if(k > f || k < 0){
			printf("Elemento não existe\n");
			return -1;
		}else{
			return info[k];
		}
		
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
				int valor;
				printf("Digite o valor a ser inserido: ");
				scanf("%d", &valor);
				ListaObj.InserirValorFimLista(valor);
			}
			else if(OP == 2){
				int valor, k;
				printf("Digite o valor a ser inserido: ");
				scanf("%d", &valor);
				printf("Digite o índice k: ");
                scanf("%d", &k);
				ListaObj.InserirK_esimoValorLista(valor, k);
			}
			else if(OP == 3){
				int valor, k;
				printf("Digite o valor a ser inserido: ");
				scanf("%d", &valor);
				printf("Digite o índice k: ");
                scanf("%d", &k);
                ListaObj.InserirAposK_esimoValorLista(valor, k);

			}
			else if(OP == 4){
				if(ListaObj.ListaVazia())
					printf("A lista ainda se encontra vazia.\n");
				else
				{
					int k;
                    printf("Digite o índice k: ");
                    scanf("%d", &k);
                    int valorRemovido = ListaObj.RemoverK_esimoValorLista(k);
                    if (valorRemovido != -1)
                        printf("Valor removido: %d\n", valorRemovido);
         
				}
			}
			 else if (OP == 5){
                  int k;
                  printf("Digite o índice k: ");
                  scanf("%d", &k);
                  int valor = ListaObj.RetornarK_esimoElemento(k);
                  if (valor != -1)
                      printf("Valor no índice %d: %d\n", k, valor);
            }
            else if (OP == 6){
            ListaObj.MostrarLista();
        }
			system("pause");
		}
	}
