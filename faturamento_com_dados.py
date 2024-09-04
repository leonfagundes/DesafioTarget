import json

# Carrega os dados do arquivo JSON
with open('dados.json') as file:
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
