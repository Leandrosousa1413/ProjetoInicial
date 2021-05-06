import os
import tkinter as tk
from PIL import ImageTk, Image


def processar_resposta(resposta, nome):
    
    if resposta == '1':
        print(f'{os.linesep}{nome} De acordo com as minhas informações, segue o graficos dos cinco consoles com mais jogos de todos tempos no mundo inteiro :{os.linesep}')
        img= Image.open("C:/Users/leand/Documents/trabalho/download.png")
        img.show()      
    elif resposta == '2':
        print(f'{os.linesep}{nome} Segue um grafico que fiz para você com os jogos mais vendidos de todos os tempos no mundo: {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Boa pergunta, segue a lista dos generos de jogos mais vendidos em todo mundo até hoje :{os.linesep}')
    else:
        print('Por favor escolha umas das opções disponiveis')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo!')
    # pedir o nome
    nome = input('Digite seu nome: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - Quais consoles com mais jogos??{os.linesep}[2] - Quais jogos mais vendidos no mundo??{os.linesep}[3] - Quais generos mais vendidos de jogos no mundo?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()