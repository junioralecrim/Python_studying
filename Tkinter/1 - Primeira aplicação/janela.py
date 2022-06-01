from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira aplicação") #colocar o título da janela principal

menu_inicial.geometry("500x400+200+200") #definir a altura, largura, posição x e posição y da janela

menu_inicial.resizable(True, True) #define (por meio de valores booleanos True ou False) se a largura e altura podem ser redimensionáveis

menu_inicial.minsize(width=500, height=400) #denife o tamanho mínimo da janela

#menu_inicial.maxsize(1080, 720) #denife o tamanho máximo da janela

#menu_inicial.state("zoomed") #faz a janela iniciar com seu tamanho máximo
#menu_inicial.state("iconic") #faz a janela iniciar minimizada

menu_inicial.mainloop() #exibir a janela principal