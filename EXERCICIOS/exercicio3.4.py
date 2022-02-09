#Expressao para determinar se uma pessoal deve ou não pagar imposto, salario acima de 1200,00 paga imposto
from unittest import result


salario = int(input("Informe qual o seu salario? "))
imposto = int(1200)

if salario >= imposto:
    print("Paga imposto")
if salario < imposto:
    print("não paga imposto")

