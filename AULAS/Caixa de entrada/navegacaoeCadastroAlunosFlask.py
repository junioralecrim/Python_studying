from flask import Flask, url_for
from werkzeug.utils import redirect

'''app = Flask(__name__)

@app.route("/")

def home():
    return "Olá! Aula de Algoritimos usando Flask!<br><h1>Criando páginas usando Flask</h1>"

if __name__ == "__main__":
    app.run()'''


'''----------------------------------EX2---------------------------------Colocar um botão-'''



'''app = Flask(__name__)


@app.route("/")
def home():
    return "Olá! Aula de Algoritimos usando Flask!<br><h1>Criando páginas usando Flask</h1> <a href=""/cadastroalunos""><input type=""submit"" value=""Entrar""></a>"


@app.route("/cadastroalunos")
def cadastrodealunos():
    return " Cadastro de alunos! <h1>Esta tela está reservada para construir a página de cadastro de alunos</h1>"


if __name__ == "__main__":
    app.run()'''



'''----------------------------------EX3---------------------------------'''

'''app = Flask(__name__)


@app.route("/")
def home():
    return "Olá! Aula de Algoritimos usando Flask!<br><h1>Criando páginas usando Flask</h1>"


@app.route("/cadastroalunos")
def cadastrodealunos():
    return " Cadastro de alunos! <h1>Esta tela está reservada para construir a página de cadastro de alunos</h1>"

@app.route("/<name>")
def user(name):
    return f'Hello {name}'

@app.route("/admin")
def admin():
    return redirect((url_for("home")))


if __name__ == "__main__":
    app.run()'''
    
#Fazer um cadastro de alunos online