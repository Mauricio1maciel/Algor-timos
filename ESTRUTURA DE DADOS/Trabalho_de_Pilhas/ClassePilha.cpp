#include <stdio.h>
#include <stdlib.h>

#define LimpaTela system("cls");

class ClassePilha
{
public:
	//Construtor da classe
	ClassePilha(int tp);
	//Verifica se a pilha est� vazia
	bool PilhaVazia();
	//Faz a verificacao se a Pilha esta cheia    
	bool PilhaCheia();
	//Insere Valor na Pilha
	void Push(int valor);
	//Remove valor da Pilha
	int Pop();
	//Mostra pilha
	void MostrarPilha();
private:
	int pilha[10];
	int topo;
};

ClassePilha::ClassePilha(int tp)
{
	topo = tp;
}

bool ClassePilha::PilhaVazia()
{
	if(topo == -1)
		return true;
	else
		return false;
}

bool ClassePilha::PilhaCheia()
{
	//Aqui � um c�digo que vai ser utilizado varias vezes, 
    //Aqui verifica de o topo atingiu o final do tamanho da pilha
	if(topo == 9){
	  return true;
	}else{
	return false;
	}
}

void ClassePilha::Push(int valor)
{
	//Inserir o valor no topo.
    //Verifica se a pilha n�o est� cheia, aumenta o topo e insere o valor.
	if(!PilhaCheia()){
		pilha[++topo] = valor;
	}else{
		printf("Pilha esta cheia!\n");
	}
	}

int ClassePilha::Pop()
{
	//Retira o valor do Topo e retorna
    //Deve verificar se a Pilha n�o est� vazia, guarda o valor, diminui o topo e retorna o valor 
	if(!PilhaVazia()){
		int valor = pilha[topo--];
		return valor;
	}else{
		printf("Pilha esta vazia!\n");
		return -1;
	}
}

void ClassePilha::MostrarPilha()
{
	//Como voc� faria para mostrar uma Pilha sem perder seus valores?
    //Voc� ter� que desempilhar, empilhar em outra pilha e retornar os valores
    //while(!PilhaVazia())
    //Pop ou Push
	if(PilhaVazia()){
		printf("Pilha esta vazia!\n");
	}else{
		printf("Pilha: ");
		for(int i = topo; i >= 0; i--){
			printf("%d ",pilha[i]);
	}
	printf("\n");
	}
}


int main()
{
	int OP;
	ClassePilha PilhaObj(-1);
	while(1)
	{
		LimpaTela;
		printf("1 - Inserir na Pilha.\n");
		printf("2 - Retirar da Pilha.\n");
		printf("3 - Mostrar Pilha.\n");
		printf("0 - Sair.\n");
		printf("Entre com a opcao: ");
		scanf("%d", &OP);
		if (OP == 0)
			break;
		else if(OP == 1){
			int valor;
			printf("Entre com o valor a ser inserido: ");
			scanf("%d", &valor);
			PilhaObj.Push(valor);
		
		}else if(OP == 2){
			int valor;
			valor = PilhaObj.Pop();
			if(valor != -1){
				printf("Valor retirado: %d\n", valor);
			}
		
		}else if(OP == 3){
			PilhaObj.MostrarPilha();
				
		}
		system("pause");
	}
}
