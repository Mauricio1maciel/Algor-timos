#include <stdio.h>      // Inclui a biblioteca padrão para entrada e saída
#include <string.h>     // Inclui a biblioteca para manipulação de strings

#define MAX 1001       // Define uma constante MAX para o tamanho máximo da string

int main() {
    int n; // Declara uma variável inteira para armazenar o número de casos de teste
    scanf("%d", &n); // Lê o número de casos de teste da entrada padrão
    
    // Loop para processar cada caso de teste
    while (n--) {
        char linha[MAX]; // Declara um array de caracteres (string) para armazenar a linha de entrada
        int diamantes = 0; // Inicializa uma variável para contar os pares de diamantes encontrados
        char pilha[MAX]; // Declara um array para simular uma pilha
        int topo = 0; // Inicializa o topo da pilha
        
        scanf("%s", linha); // Lê a linha de entrada
        
        int i = 0; // Inicializa um índice para percorrer a string

        // Loop para percorrer cada caractere da linha
        while (i < strlen(linha)) {
            // Se encontrar um caractere '<', empilha
            if (linha[i] == '<') {
                pilha[topo++] = '<'; // Adiciona o caractere '<' na pilha e incrementa o topo
            // Se encontrar um caractere '>'
            } else if (linha[i] == '>') {
                // Verifica se a pilha não está vazia (se existe um '<' correspondente)
                if (topo > 0) {  
                    topo--; // Remove o caractere '<' da pilha (desempilha)
                    diamantes++; // Incrementa o contador de diamantes (pares de '<' e '>')
                }
            }
            i++; // Avança para o próximo caractere
        }
        
        // Imprime o número de pares de diamantes encontrados na linha atual
        printf("%d\n", diamantes);
    }
    
    return 0; // Retorna 0, indicando que o programa terminou corretamente
}
