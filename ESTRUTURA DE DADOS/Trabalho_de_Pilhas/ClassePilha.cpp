#include <stdio.h>      // Inclui a biblioteca padrão para entrada e saída
#include <stdlib.h>     // Inclui a biblioteca para funções auxiliares como system

#define LimpaTela system("cls"); // Define um macro para limpar a tela usando o comando 'cls' do sistema

class ClassePilha { // Define a classe 'ClassePilha'
public:
    // Construtor da classe que recebe o topo inicial da pilha
    ClassePilha(int tp);
    // Verifica se a pilha está vazia
    bool PilhaVazia();
    // Verifica se a pilha está cheia
    bool PilhaCheia();
    // Insere um valor na pilha
    void Push(int valor);
    // Remove um valor da pilha
    int Pop();
    // Mostra os valores da pilha
    void MostrarPilha();
private:
    int pilha[10]; // Array para armazenar os elementos da pilha (máximo de 10 elementos)
    int topo;      // Índice do topo da pilha
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
    // Se o topo é 9, a pilha está cheia (máximo de 10 elementos)
    if (topo == 9) {
        return true;
    } else {
        return false; // Caso contrário, a pilha não está cheia
    }
}

// Insere um valor no topo da pilha
void ClassePilha::Push(int valor) {
    // Verifica se a pilha está cheia antes de inserir
    if (PilhaCheia()) {
        printf("Pilha esta cheia!\n"); // Exibe mensagem de erro se a pilha estiver cheia
    } else {
        topo++; // Incrementa o topo
        pilha[topo] = valor; // Adiciona o valor no topo da pilha
    }
}

// Remove e retorna o valor do topo da pilha
int ClassePilha::Pop() {
    // Verifica se a pilha está vazia antes de remover
    if (PilhaVazia()) {
        printf("Pilha esta vazia!\n"); // Exibe mensagem de erro se a pilha estiver vazia
        return -1; // Retorna -1 indicando que não há valor para remover
    } else {
        int valor = pilha[topo]; // Armazena o valor do topo
        topo--; // Decrementa o topo
        return valor; // Retorna o valor removido
    }
}

// Mostra os valores da pilha sem perder seus dados
void ClassePilha::MostrarPilha() {
    // Verifica se a pilha está vazia
    if (PilhaVazia()) {
        printf("Pilha esta vazia!\n"); // Exibe mensagem se a pilha estiver vazia
    } else {
        ClassePilha pilhaAux(-1); // Cria uma pilha auxiliar para armazenar temporariamente os valores

        // Loop para desempilhar os valores e mostrá-los
        while (!PilhaVazia()) {
            int valor = Pop(); // Remove o valor do topo da pilha
            printf("%d\n", valor); // Exibe o valor removido
            pilhaAux.Push(valor); // Empilha o valor na pilha auxiliar
        }

        // Loop para restaurar os valores da pilha auxiliar de volta à pilha original
        while (!pilhaAux.PilhaVazia()) {
            Push(pilhaAux.Pop()); // Desempilha da pilha auxiliar e empilha de volta na pilha original
        }
    }
}

int main() {
    int OP; // Declara uma variável para armazenar a operação escolhida pelo usuário
    ClassePilha PilhaObj(-1); // Cria uma instância da classe ClassePilha com topo inicial de -1

    while (1) { // Loop infinito para exibir o menu até que o usuário decida sair
        LimpaTela; // Limpa a tela
        printf("1 - Inserir na Pilha.\n"); // Opção para inserir na pilha
        printf("2 - Retirar da Pilha.\n"); // Opção para retirar da pilha
        printf("3 - Mostrar Pilha.\n"); // Opção para mostrar os valores da pilha
        printf("0 - Sair.\n"); // Opção para sair do programa
        printf("Entre com a opcao: "); // Solicita que o usuário escolha uma opção
        scanf("%d", &OP); // Lê a opção escolhida

        // Verifica a opção escolhida pelo usuário
        if (OP == 0)
            break; // Sai do loop se o usuário escolher 0
        else if (OP == 1) {
            int valor; // Declara uma variável para o valor a ser inserido
            printf("Entre com o valor a ser inserido: "); // Solicita o valor
            scanf("%d", &valor); // Lê o valor
            PilhaObj.Push(valor); // Insere o valor na pilha
        } else if (OP == 2) {
            int valor; // Declara uma variável para armazenar o valor retirado
            valor = PilhaObj.Pop(); // Retira o valor do topo da pilha
            if (valor != -1) { // Verifica se o valor retirado não é -1 (indicando pilha vazia)
                printf("Valor retirado: %d\n", valor); // Exibe o valor retirado
            }
        } else if (OP == 3) {
            PilhaObj.MostrarPilha(); // Mostra os valores da pilha
        }
        system("pause"); // Pausa a execução até que o usuário pressione uma tecla
    }
}
