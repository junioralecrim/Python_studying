from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira aplicação")

menu_inicial.geometry("500x400+200+200")

menu_inicial.resizable(True, True)

menu_inicial.minsize(width=500, height=400)

menu_inicial.iconbitmap("imagens/icon.ico") #mudando o ícone da aplicação

menu_inicial.mainloop()