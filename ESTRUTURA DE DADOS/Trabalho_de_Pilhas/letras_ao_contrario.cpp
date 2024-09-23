#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LimpaTela system("cls");

class ClassePilha
{
public:
    // Construtor da classe
    ClassePilha();
    // Verifica se a pilha está vazia
    bool PilhaVazia();
    // Faz a verificação se a Pilha está cheia    
    bool PilhaCheia();
    // Insere Valor na Pilha
    void Push(char valor);
    // Remove valor da Pilha
    char Pop();
    // Mostra pilha
    void MostrarPilha();
private:
    char pilha[50];
    int topo;
};

ClassePilha::ClassePilha()
{
    topo = -1;
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
    if (!PilhaCheia())
    {
        pilha[++topo] = valor;
    }
    else
    {
        printf("A pilha está cheia!\n");
    }
}

char ClassePilha::Pop()
{
    if (!PilhaVazia())
    {
        return pilha[topo--];
    }
    else
    {
        printf("A pilha está vazia!\n");
        return '\0'; // Valor de erro
    }
}

void ClassePilha::MostrarPilha()
{
    if (PilhaVazia())
    {
        printf("A pilha está vazia!\n");
    }
    else
    {
        printf("Pilha: ");
        for (int i = topo; i >= 0; i--)
        {
            printf("%c", pilha[i]);
        }
        printf("\n");
    }
}

void CriptografarTexto(char texto[])
{
    ClassePilha pilha;
    int n = strlen(texto);

    for (int i = 0; i < n; i++)
    {
        if (texto[i] != ' ')
        {
            pilha.Push(texto[i]);
        }
        else
        {
            while (!pilha.PilhaVazia())
            {
                printf("%c", pilha.Pop());
            }
            printf(" ");
        }
    }

    while (!pilha.PilhaVazia())
    {
        printf("%c", pilha.Pop());
    }
    printf("\n");
}

int main()
{
    char texto[100];
    printf("Digite o texto a ser criptografado: ");
    fgets(texto, 100, stdin);
    texto[strcspn(texto, "\n")] = '\0'; // Remove o newline do final

    LimpaTela;
    printf("Texto criptografado: ");
    CriptografarTexto(texto);

    return 0;
}
