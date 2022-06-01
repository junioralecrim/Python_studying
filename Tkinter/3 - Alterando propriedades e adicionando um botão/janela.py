from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Aplicação")

menu_inicial.geometry("500x400+200+200")
menu_inicial.minsize(width=500, height=400)
menu_inicial.iconbitmap("imagens/icon.ico")

menu_inicial['bg'] = "grey" #serve para definir a cor de fundo da janela principal

#botao

botao = Button(menu_inicial, text="Executar") #Button(a onde o botão pertence, texto no botão)
botao.pack() #adicionando o botão à janela


menu_inicial.mainloop()