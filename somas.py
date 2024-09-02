'''
3) Observe o trecho de código abaixo:

int INDICE = 12/13, SOMA = 0, K = 1/0;

    enquanto K < INDICE faça { 
        K = K + 1;
        SOMA = SOMA + K; 
    } 
    
imprimir(SOMA);
'''

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# soma=77 para indice=12 e k=1
# soma=91 para indice=13 e