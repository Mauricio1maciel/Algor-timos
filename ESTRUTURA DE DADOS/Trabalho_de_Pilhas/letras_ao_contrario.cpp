#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define LimpaTela system("cls");

class ClassePilha
{
public:
	//Construtor da classe
	ClassePilha(int tp);
	//Verifica se a pilha está vazia
	bool PilhaVazia();
	//Faz a verificacao se a Pilha está cheia    
	bool PilhaCheia();
	//Insere Valor na Pilha
	void Push(char valor);
	//Remove valor da Pilha
	char Pop();
	//Mostra pilha
	void MostrarPilha();
private:
	char pilha[50]; // Modificado para caracteres
	int topo;
};

ClassePilha::ClassePilha(int tp)
{
	topo = tp;
}

bool ClassePilha::PilhaVazia()
{
	return topo == -1;
}

bool ClassePilha::PilhaCheia()
{
	return topo == 49; 
}

void ClassePilha::Push(char valor)
{
	if(!PilhaCheia()){
		pilha[++topo] = valor;
	}else{
		printf("Pilha está cheia!\n");
	}
}

char ClassePilha::Pop()
{
	if(!PilhaVazia()){
		return pilha[topo--];
	}else{
		printf("Pilha está vazia!\n");
		return '\0'; 
	}
}

void ClassePilha::MostrarPilha()
{
	if(PilhaVazia()){
		printf("Pilha está vazia!\n");
	}
	
	ClassePilha pilhaAux(-1);

	while (!PilhaVazia()){
		char valor = Pop();
		printf("%c", valor);
		pilhaAux.Push(valor);
	}
	while (!pilhaAux.PilhaVazia()){
		Push(pilhaAux.Pop());
	}
}


void CriptografarTexto(char frase[])
{
	ClassePilha pilha(-1);
	int len = strlen(frase);
	
	for(int i = 0; i < len; i++) {
		if(frase[i] != ' ') {
			pilha.Push(frase[i]);
		} else {
			while (!pilha.PilhaVazia()) {
				printf("%c", pilha.Pop());
			}
			printf(" "); 
		}
	}

	while (!pilha.PilhaVazia()) {
		printf("%c", pilha.Pop());
	}
	printf("\n");
}

int main()
{
	int OP;
	char frase[50];
	while(1)
	{
		LimpaTela;
		printf("1 - Inserir uma frase para criptografar.\n");
		printf("0 - Sair.\n");
		printf("Entre com a opção: ");
		scanf("%d", &OP);
		if (OP == 0)
			break;
		else if(OP == 1){
			printf("Entre com a frase (máximo 50 caracteres): ");
			scanf(" %[^\n]s", frase); 
			printf("Frase criptografada: ");
			CriptografarTexto(frase);
		}
		system("pause");
	}
}
