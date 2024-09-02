'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na 
linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem 
ser ignorados no cálculo da média;
'''

import json

# Carrega os dados do arquivo JSON
with open('faturamento.json') as file:
    dados = json.load(file)

# Filtra os dias com faturamento maior que zero
faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcula o menor e maior valor de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_faturamento = sum(faturamentos) / len(faturamentos)

# Conta o número de dias com faturamento superior à média mensal
dias_acima_da_media = len([valor for valor in faturamentos if valor > media_faturamento])

print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
