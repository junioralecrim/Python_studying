from tkinter import *

#janela
menu_inicial = Tk()
menu_inicial.title("Aplicação")
menu_inicial.geometry("500x300")


def botao_click(mensagem):
    print(mensagem)

#botão
botao1 = Button(menu_inicial, text="Executar", command=lambda: botao_click("Nova mensagem"))
#quando eu preciso passar argumentos pra dentro de uma função no clique de um botão eu preciso usar a função lambda da forma como
#está acima.
botao1.pack()

botao2 = Button(menu_inicial, text="Executar", command=lambda: print("Outra mensagem"))
botao2.pack()

#também é possível associar uma ação direta ao botão sem precisar passar por uma funcão

menu_inicial.mainloop()