# 5) Escreva um programa que inverta os caracteres de um string.

string = input("Digite a string que deseja inverter: ")

inverse_string = ""

for i in range(len(string) - 1, -1, -1):
    inverse_string += string[i]

print(f"String original: {string}")
print(f"String invertida: {inverse_string}")
