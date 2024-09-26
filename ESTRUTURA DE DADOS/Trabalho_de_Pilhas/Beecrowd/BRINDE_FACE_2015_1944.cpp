#include <iostream>  // Inclui a biblioteca para entrada e saída
#include <string>    // Inclui a biblioteca para manipulação de strings

using namespace std; // Usa o espaço de nomes padrão para evitar a necessidade de 'std::'

class PainelPilha {
public:
    // Construtor da classe, que inicializa o painel
    PainelPilha() {
        reset_painel(); // Chama a função para reiniciar o painel
        topo = -1; // Inicializa o topo da pilha como -1 (indicando que a pilha está vazia)
    }

    // Função para verificar se a pilha está vazia
    bool PilhaVazia() {
        if (topo == -1) { // Se o topo é -1, a pilha está vazia
            return true;
        } else {
            return false; // Caso contrário, a pilha não está vazia
        }
    }

    // Função para verificar se a pilha está cheia
    bool PilhaCheia() {
        if (topo == 9) { // Se o topo é 9, a pilha está cheia (máximo de 10 elementos)
            return true;
        } else {
            return false; // Caso contrário, a pilha não está cheia
        }
    }

    // Função para adicionar um elemento à pilha
    void Push(const string& letra) {
        if (!PilhaCheia()) { // Verifica se a pilha não está cheia
            topo++; // Incrementa o topo
            painel[topo] = letra; // Adiciona o elemento no topo da pilha
        }
    }

    // Função para remover e retornar o elemento do topo da pilha
    string Pop() {
        if (!PilhaVazia()) { // Verifica se a pilha não está vazia
            string valor = painel[topo]; // Armazena o valor do elemento no topo
            topo--; // Decrementa o topo
            return valor; // Retorna o valor removido
        }
        return ""; // Se a pilha estiver vazia, retorna uma string vazia
    }

    // Função para reiniciar o painel com valores padrão
    void reset_painel() {
        topo = -1; // Reseta o topo para -1
        Push("F"); // Adiciona "F" ao painel
        Push("A"); // Adiciona "A" ao painel
        Push("C"); // Adiciona "C" ao painel
        Push("E"); // Adiciona "E" ao painel
    }

    // Função para verificar se há um brinde
    bool verifica_brinde() {
        // Verifica se há pelo menos 8 elementos na pilha
        if (topo >= 7) {
            // Verifica se os elementos no topo formam um brinde específico
            return painel[topo] == painel[topo - 7] &&
                   painel[topo - 1] == painel[topo - 6] &&
                   painel[topo - 2] == painel[topo - 5] &&
                   painel[topo - 3] == painel[topo - 4];
        }
        return false; // Retorna falso se não houver brinde
    }

private:
    string painel[10]; // Array para armazenar os elementos da pilha (máximo 10)
    int topo; // Índice do topo da pilha
};

int main() {
    int N; // Declara uma variável para o número de operações
    cin >> N; // Lê o número de operações da entrada padrão

    PainelPilha painelPilha; // Cria uma instância da classe PainelPilha
    int brindes = 0; // Inicializa um contador para os brindes encontrados
    int i = 0; // Inicializa um índice para o loop principal

    // Loop para realizar N operações
    while (i < N) {
        string l1, l2, l3, l4; // Declara variáveis para armazenar as strings de entrada
        cin >> l1 >> l2 >> l3 >> l4; // Lê as quatro strings da entrada

        // Adiciona as strings ao painel
        painelPilha.Push(l1);
        painelPilha.Push(l2);
        painelPilha.Push(l3);
        painelPilha.Push(l4);

        // Verifica se há um brinde
        if (painelPilha.verifica_brinde()) {
            int count = 0; // Inicializa um contador para remover elementos da pilha
            // Remove 8 elementos do painel
            while (count < 8) {
                painelPilha.Pop(); // Remove o elemento do topo da pilha
                count++;
            }
            brindes++; // Incrementa o contador de brindes
        }

        // Verifica se a pilha está vazia
        if (painelPilha.PilhaVazia()) {
            painelPilha.reset_painel(); // Reinicia o painel se estiver vazio
        }

        i++; // Avança para a próxima operação
    }

    // Imprime o número total de brindes encontrados
    cout << brindes << endl;

    return 0; // Retorna 0, indicando que o programa terminou corretamente
}
