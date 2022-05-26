from tkinter import*

window = Tk()
window.minsize(400, 400)

bemvindo = Label(window, text='BEM VINDO AO CADASTRO!')
bemvindo.grid(row=5, column=1)

nomeAluno = Label(window, text="Nome: ")
nomeAluno.grid(row=0, column=1)
idadeAluno = Label(window, text="Idade: ")
idadeAluno.grid(row=1, column=1)
matriculaAluno = Label(window, text="Matricula ")
matriculaAluno.grid(row=2, column=1)


window.mainloop()

