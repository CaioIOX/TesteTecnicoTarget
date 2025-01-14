# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o 
# percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

billing = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_billing = sum(billing.values())

print("Percentual de representação de cada estado no faturamento mensal: ")
for state, value in billing.items():
    percentage = value/ total_billing * 100
    print(f"{state}: {percentage:.2f}%")

total_billing = locale.currency(total_billing, grouping=True)

print(f"\nFaturamento total: {total_billing}")