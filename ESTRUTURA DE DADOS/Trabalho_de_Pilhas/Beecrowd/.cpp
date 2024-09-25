#include <stdio.h>
#include <string.h>

#define MAX 1001 

int main() {
    int n;
    scanf("%d", &n);
    
    while (n--) {
        char linha[MAX];
        int diamantes = 0;
        char pilha[MAX];  
        int topo = 0;     

        scanf("%s", linha);
        
        for (int i = 0; i < strlen(linha); i++) {
            if (linha[i] == '<') {
                pilha[topo++] = '<';  
            } else if (linha[i] == '>') {
                if (topo > 0) {  
                    topo--;      
                    diamantes++; 
                }
            }
        }
        
        printf("%d\n", diamantes);
    }
    
    return 0;
}
