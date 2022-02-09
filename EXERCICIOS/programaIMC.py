#Calculo do IMC (Indice Massa Corporal)
from tkinter import *

janela = Tk()
janela.title("Verificar seu IMC")

lb1 = Label(janela, text="Digite qual o seu peso: ")
lb1.place(x=90, y=30)
var1 = Entry(janela)
var1.place(x=90, y=50)

lb2 = Label(janela, text="Digite qual a sua altura: ")
lb2.place(x=90, y=80)
var2 = Entry(janela)
var2.place(x=90, y=100)

lb3 = Label(janela, text="")
lb3.place(x=100, y=160)


#Calculo imc
def calculo_imc():
    imc = Entry(entry.get(var1/ (var2*var2)))

    
botao = Button(janela, text="CALCULAR IMC", command=calculo_imc)
botao.grid(padx=100, pady=120)

#Calculo classificação do IMC
classificacao = None

def classificacao_imc():
    if imc <= 18.5:
        classificacao = 'Classificação IMC: Baixo peso'
    elif imc <= 24.9:
        classificacao = 'Classificação IMC: Peso ideal'
    elif imc <= 29.9:
        classificacao = 'Classificação IMC: Sobrepeso'
    elif imc <= 34.9:
        classificacao = 'Classificação IMC: Obesidade 1º'
    elif imc <= 39.9: 
        classificacao = 'Classificação IMC: Obesidade 2º'
    else:
        classificacao = 'Classificação IMC: Obesidade grave'
        classificacao = print(classificacao_imc)


janela.geometry("300x200")
janela.mainloop()