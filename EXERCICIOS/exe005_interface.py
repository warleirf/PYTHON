from tkinter import *

janela = Tk()
janela.title("Programa conveter Metros em Centímetros")

def converter():
    print("converter")
    metros = int(var1.get())
    lb["text"] = metros*100
        

lb1 = Label(janela, text="Digite Quantos Metros?")
lb1.place(x=90, y=30)
var1 = Entry(janela)
var1.place(x=90, y=50)

botao = Button(janela, text='Clique aqui para converter em Centímetros',command=converter)
botao.place(x=30, y=80)

lb = Label(janela, text="??")
lb.place(x=100, y=120)
lb3 = Label(janela, text="Centímetros")
lb3.place(x=140, y=120)

janela.mainloop()