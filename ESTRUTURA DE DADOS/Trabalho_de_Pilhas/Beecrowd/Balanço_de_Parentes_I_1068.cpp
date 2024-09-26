#include <iostream> // Inclui a biblioteca para entrada e saída
#include <stack>    // Inclui a biblioteca para usar pilhas
#include <string>   // Inclui a biblioteca para usar strings

using namespace std; // Utiliza o espaço de nomes padrão para evitar digitar 'std::' antes de cada objeto

int main(){
    string linha; // Declara uma string para armazenar a linha de entrada
    bool correta; // Declara uma variável booleana para verificar se os parênteses estão corretos
    
    // Loop para ler várias linhas de entrada até o fim do arquivo (EOF)
    while (getline(cin, linha)){
        correta = true; // Assume inicialmente que a linha está correta
        stack<char> pilha; // Cria uma pilha para armazenar os parênteses
        int i = 0;  // Inicializa um índice para percorrer a string
       
        // Loop para percorrer cada caractere da linha
        while (i < linha.size()) {
            // Se encontrar um parêntese de abertura '(', empilha
            if (linha[i] == '(') {
                pilha.push(linha[i]);
            // Se encontrar um parêntese de fechamento ')'
            } else if (linha[i] == ')') {
                // Verifica se a pilha não está vazia
                if (!pilha.empty()) {
                    pilha.pop(); // Remove o parêntese de abertura correspondente da pilha
                } else {
                    correta = false; // Se a pilha estiver vazia, significa que não há parêntese de abertura correspondente
                }
            }
            i++;  // Avança para o próximo caractere
        }
        
        // Após percorrer toda a linha, verifica se a pilha está vazia e se a linha é correta
        if (pilha.empty() && correta) {
            cout << "correct" << endl; // Se ambos os critérios forem verdadeiros, imprime "correct"
        } else {
            cout << "incorrect" << endl; // Caso contrário, imprime "incorrect"
        }
    }
    
    return 0; // Retorna 0, indicando que o programa terminou corretamente
}
