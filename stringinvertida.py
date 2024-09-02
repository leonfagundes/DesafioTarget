'''
5) Escreva um programa que inverta os caracteres de um string.
'''

def inverter_string(s):
    return s[::-1]

string = input("Digite uma string: ")
string_invertida = inverter_string(string)

print(f"A string invertida é: {string_invertida}")
