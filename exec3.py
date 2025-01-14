# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, 
# na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json
import locale

# Configurar o locale para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Caminho do arquivo JSON
json_path = "dados.json"

# Ler e processar os dados do arquivo JSON
with open(json_path, "r") as file:
    data = json.load(file)

# Filtrar faturamento válido (maior que 0)
billing = [item["valor"] for item in data if item["valor"] > 0]

# Cálculos
minor_billing = min(billing)
biggest_billing = max(billing)
average = sum(billing) / len(billing)
days_above_the_average = sum(1 for valor in billing if valor > average)

# Resultados formatados
print(f"Menor faturamento: {locale.currency(minor_billing, grouping=True)}")
print(f"Maior faturamento: {locale.currency(biggest_billing, grouping=True)}")
print(f"Número de dias com faturamento superior à média: {days_above_the_average}")
print(f"Média mensal: {locale.currency(average, grouping=True)}")
