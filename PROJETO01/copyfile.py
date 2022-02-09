import os
import shutil

caminho_origem = f'D:\Fotos'
caminho_destino = f'D:\Fotos\teste'

try:
    os.mkdir(caminho_destino)
except FileExistsError as e:
    print(f'Pasta {caminho_destino} já existe.')

for root, dirs, files, in os.walk(caminho_origem):
    for file in files:
        print(file)