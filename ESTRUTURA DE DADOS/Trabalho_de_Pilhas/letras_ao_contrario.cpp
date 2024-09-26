#include <stdio.h>      // Inclui a biblioteca padrão para entrada e saída
#include <stdlib.h>     // Inclui a biblioteca para funções auxiliares como system
#include <string.h>     // Inclui a biblioteca para manipulação de strings
#include <ctype.h>      // Inclui a biblioteca para funções relacionadas a caracteres

#define LimpaTela system("cls"); // Define um macro para limpar a tela usando o comando 'cls' do sistema

class ClassePilha { // Define a classe 'ClassePilha'
public:
    // Construtor da classe que inicializa o topo
    ClassePilha(int tp);
    // Verifica se a pilha está vazia
    bool PilhaVazia();
    // Verifica se a pilha está cheia
    bool PilhaCheia();
    // Insere um valor na pilha
    void Push(char valor);
    // Remove e retorna o valor do topo da pilha
    char Pop();
    
private:
    char pilha[50]; // Array para armazenar os elementos da pilha (máximo de 50 elementos)
    int topo;       // Índice do topo da pilha
};

// Implementação do construtor da classe
ClassePilha::ClassePilha(int tp) {
    topo = tp; // Inicializa o topo da pilha com o valor passado
}

// Verifica se a pilha está vazia
bool ClassePilha::PilhaVazia() {
    if (topo == -1) { // Se o topo é -1, a pilha está vazia
        return true;
    } else {
        return false; // Caso contrário, a pilha não está vazia
    }
}

// Verifica se a pilha está cheia
bool ClassePilha::PilhaCheia() {
    // Se o topo é 49, a pilha está cheia (máximo de 50 elementos)
    if (topo == 49) {
        return true;
    } else {
        return false; // Caso contrário, a pilha não está cheia
    }
}

// Insere um valor no topo da pilha
void ClassePilha::Push(char valor) {
    // Verifica se a pilha está cheia antes de inserir
    if (PilhaCheia()) {
        printf("Pilha esta cheia!\n"); // Exibe mensagem de erro se a pilha estiver cheia
    } else {
        topo++; // Incrementa o topo
        pilha[topo] = valor; // Adiciona o valor no topo da pilha
    }
}

// Remove e retorna o valor do topo da pilha
char ClassePilha::Pop() {
    // Verifica se a pilha está vazia antes de remover
    if (PilhaVazia()) {
        printf("Pilha esta vazia!\n"); // Exibe mensagem de erro se a pilha estiver vazia
        return '\0'; // Retorna o caractere nulo se não houver valor para remover
    } else {
        char valor = pilha[topo]; // Armazena o valor do topo
        topo--; // Decrementa o topo
        return valor; // Retorna o valor removido
    }
}

// Função que inverte as palavras de uma frase
void Palavra_ao_contrario(char frase[]) {
    ClassePilha pilha(-1); // Cria uma instância da pilha com topo inicial de -1
    int len = strlen(frase); // Obtém o comprimento da frase
    int i = 0; // Inicializa um índice para percorrer a frase

    // Loop para percorrer cada caractere da frase
    while (i < len) {
        if (frase[i] != ' ') { // Se o caractere não é um espaço
            pilha.Push(frase[i]); // Empilha o caractere
        } else { // Se encontrar um espaço
            // Desempilha todos os caracteres até encontrar a pilha vazia
            while (!pilha.PilhaVazia()) {
                printf("%c", pilha.Pop()); // Exibe e remove o caractere do topo da pilha
            }
            printf(" "); // Imprime um espaço
        }
        i++; // Incrementa o índice
    }

    // Desempilha quaisquer caracteres restantes após o último espaço
    while (!pilha.PilhaVazia()) {
        printf("%c", pilha.Pop()); // Exibe e remove o caractere do topo da pilha
    }
    printf("\n"); // Imprime uma nova linha após a frase invertida
}

int main() {
    int OP; // Declara uma variável para armazenar a operação escolhida (não utilizada aqui)
    char frase[50]; // Declara um array de caracteres para armazenar a frase (máximo de 50 caracteres)
    printf("Entre com a frase (máximo 50 caracteres): "); // Solicita ao usuário que insira uma frase
    scanf(" %[^\n]s", frase); // Lê a frase incluindo espaços até o final da linha
    printf("Frase criptografada: "); // Exibe uma mensagem antes de mostrar a frase invertida
    Palavra_ao_contrario(frase); // Chama a função que inverte as palavras na frase
    system("pause"); // Pausa a execução até que o usuário pressione uma tecla
}
