#Media das notas bimestrais
from tkinter import *

def nota_bimestrais():
    nota01 = int(input('Digite sua primeira nota: '))
    nota02 = int(input('Digite sua segunda nota: '))
    nota03 = int(input('Digite sua terceira nota: '))
    nota04 = int(input('Digite sua ultima nota: '))
    media = ((nota01+nota02+nota03+nota04)/4)

    print('O valor da média de suas notas é = {}'.format(media))


janela = Tk()
janela.title("Média das notas Bimestrais")


botao = Button(janela, text="Clique aqui para calcular a média:", command=nota_bimestrais)
botao.grid(column=0, row=1, padx=20, pady=20)

janela.mainloop()

