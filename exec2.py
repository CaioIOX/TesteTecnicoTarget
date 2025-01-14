# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
# será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.

def verify_fibonacci_sequence(value):
    if value <  0:
        return f"O número {value} não pertence à sequência de Fibonacci."
    
    a, b = 0, 1
    
    while a < value:
        a, b = b, a + b
        
    if a == value:
        return f"O número {value} pertence à sequência de Fibonacci."
    else:
        return f"O número {value} não pertence à sequência de Fibonacci."
    
try:
    number = int(input("Digite um número: "))
    result = verify_fibonacci_sequence(number)
    print(result)
    
except ValueError:
    print("Por favor, insira um número inteiro válido.")