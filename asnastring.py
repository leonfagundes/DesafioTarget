'''
2) Escreva um programa que verifique, em uma string, a
existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a
quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada
através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
'''

def a_verify(texto):

    contador = texto.count('a') + texto.count('A')

    # Verificar se existe 'a' ou 'A' na string
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Exemplo de uso
string = input("Digite uma string: ")
a_verify(string)
