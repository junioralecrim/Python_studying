from tkinter import *

#janela
menu_inicial = Tk()
menu_inicial.title("Aplicação")

#dimensões da janela
largura = 500
altura = 300

#resolução do nosso sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

print(largura_screen, altura_screen)

#posição da janela
posicaoX = (largura_screen/2) - (largura/2)
posicaoY = (altura_screen/2) - (altura/2)

#definindo a geometry
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posicaoX, posicaoY))


menu_inicial.mainloop()