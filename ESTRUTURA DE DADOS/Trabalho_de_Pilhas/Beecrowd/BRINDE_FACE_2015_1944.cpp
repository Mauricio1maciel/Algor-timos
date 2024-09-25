#include <stdio.h>
#include <string.h>

#define MAX_VISITANTES 100
#define TAM_PAINEL 100

// Estrutura da pilha
char painel[TAM_PAINEL];
int topo = 0; // Índice do topo da pilha

// Função para inserir letras na pilha
void empilhar(char letra) {
    painel[topo++] = letra;
}

// Função para verificar se os últimos 4 formam o reverso
int verificar_brinde() {
    if (topo < 8) return 0; // Deve ter pelo menos 8 letras para verificar

    // Últimas 4 letras inseridas
    char ultimas_quatro[5] = {
        painel[topo - 1],
        painel[topo - 2],
        painel[topo - 3],
        painel[topo - 4],
        '\0'
    };

    // Quatro letras que estão antes das últimas inseridas
    char quatro_anteriores[5] = {
        painel[topo - 5],
        painel[topo - 6],
        painel[topo - 7],
        painel[topo - 8],
        '\0'
    };

    // Inverte as últimas 4 letras
    char reverso[5];
    for (int j = 0; j < 4; j++) {
        reverso[j] = ultimas_quatro[3 - j];
    }
    reverso[4] = '\0'; // Termina a string

    // Compara as quatro anteriores com o reverso
    return strcmp(quatro_anteriores, reverso) == 0;
}

int main() {
    int n;
    char entradas[MAX_VISITANTES][5]; // Para armazenar 4 letras + '\0'
    int brindes = 0;

    // Inicializa o painel com F A C E
    empilhar('F');
    empilhar('A');
    empilhar('C');
    empilhar('E');

    // Lê o número de visitantes
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        // Lê as letras inseridas pelo visitante
        scanf(" %c %c %c %c", &entradas[i][0], &entradas[i][1], &entradas[i][2], &entradas[i][3]);
        // Insere as letras na pilha
        for (int j = 0; j < 4; j++) {
            empilhar(entradas[i][j]);
        }

        // Verifica se ganhou um brinde
        if (verificar_brinde()) {
            brindes++;
        }
    }

    // Imprime a quantidade de brindes
    printf("%d\n", brindes);

    return 0;
}
