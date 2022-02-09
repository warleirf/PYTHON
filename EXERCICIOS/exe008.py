#Programa para calcular salario mensal:

hr_sal = int(input("Quanto você ganha por hora? "))
hr_trab = int(input("Quantas horas trabalhou nesse mês? "))
calculo = hr_sal*hr_trab
print("TOTAL DO SEU SALÁRIO ESSE MÊS = R${},00 reais" .format(calculo))