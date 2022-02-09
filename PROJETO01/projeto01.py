 from tkinter import *

metros_lote = int(input("Quantos m2 tem o lote? "))
Valor_lote = int(input("Qual valor o lote foi avaliado? "))
herdeiros = int(input("Quantidade de herdeiros? "))

calc_metros = (metros_lote / herdeiros) #calculo da quantidade de metros para cada herdeiro do lote.
calc_valor = (Valor_lote / herdeiros) #Valor em dinheiro para cada herdeiro.
calc_porcent_lote = ((calc_metros*100) / metros_lote) #Porcentagem de cada herdeiro referente ao lote total.


janela = Tk()
janela.title("Calcular valor de Herança")

def calculo_lote():
    print("Cada herdeiro tem direito a {:.2f} m2 do lote que representa {:.2f}% do total do lote, avaliado pelo valor de R${:.2f} reais" .format(calc_metros, calc_porcent_lote, calc_valor))

calculo_lote()

metros_lote = Label(janela, text="Quantos m2 tem o lote?")
metros_lote.place(x=90, y=30)
var1 = Entry(janela)
var1.place(x=90, y=50)

Valor_lote = Label(janela, text="Qual valor o lote foi avaliado?")
Valor_lote.place(x=90, y=30)
var2 = Entry(janela)
var2.place(x=90, y=50)

herdeiros = Label(janela, text="Quantidade de herdeiros?")
herdeiros.place(x=90, y=30)
var3 = Entry(janela)
var3.place(x=90, y=50)

botao = Button(janela, text='Clique aqui para realizar o calculo:',command=calculo_lote)
botao.place(x=30, y=80)

janela.mainloop()

