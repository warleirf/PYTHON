#Converter metros em centimetros.
from typing import Collection

def converter():
    metros = int(input('Digite quantos metros: '))
    formula = (metros*100)
    print('{} metros convertidos em centímetros é igual à = {}cm'.format(metros, formula))
converter()