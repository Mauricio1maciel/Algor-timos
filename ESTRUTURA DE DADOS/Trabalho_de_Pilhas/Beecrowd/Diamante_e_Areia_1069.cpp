#include <stdio.h>
#include <string.h>


int main(){

    int n;
    scanf("%d", &n);

    while (n--)
    {
        char linha[1001];
        int diamantes = 0;
        int pilha = 0;

        scanf("%s", linha);

        for (int i = 0; i < strlen(linha); i++){
            if (linha[i] == '<'){
                pilha++;
            }else if(linha[i] == '>'){
                if(pilha > 0){
                    pilha--;
                    diamantes++;
                }
            }
    }
    printf("%d\n", diamantes);
    }
     return 0;
     }
    
        

    
