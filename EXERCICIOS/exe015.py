#Programa para calcular salario Bruto, INSS, salario liquido.

def salario():
    sal_hora = int(input("Quanto você ganha por hora? "))
    hora_trab = int(input("Quantas horas trabalhou no mês? "))
    sal_bruto = sal_hora*hora_trab
    print("- Salário bruto é: R$ {} reais" .format(sal_bruto))
    cal_inss = sal_bruto*0.08
    print("- INSS (8%): R$ {} reais" .format(cal_inss))
    cal_ir = sal_bruto*0.11
    print("- IR (11%): R$ {} reais" .format(cal_ir))
    cal_sind = sal_bruto*0.05
    print("- Sindicato (5%): R$ {} reais".format(cal_sind)) 
    sal_liq = sal_bruto - cal_inss - cal_ir - cal_sind
    print("- Salario liquido é: R$ {} reais" .format(sal_liq))
salario()