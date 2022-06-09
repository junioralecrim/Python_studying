from flask import Flask, url_for, render_template, redirect, request
from werkzeug.utils import redirect
#por algum motivo, quando tento importar tudo aqui não vai. Preciso importar o url_for e o render_template separadamente


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

# Fazer um cadastro de alunos online



'''----------------------------------EX5---------------------------------'''

'''app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/cadastroalunos")
def cadastrodealunos():
    return " Cadastro de alunos! <h1>Esta tela está reservada para construir a página de cadastro de alunos</h1>"

@app.route("/<name>") #o parâmetro é passado pela url (get)
def name(name):
    return render_template("index.html", content=name, parametro=["ai", "ei", "ou"])

@app.route("/admin")
def admin():
    return redirect((url_for("home")))


if __name__ == "__main__":
    app.run()'''



'''----------------------------------EX6---------------------------------'''

#redirect é para fazer o redirecionamento de pag
#url_for serve para passar uma url

'''app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/cadastroalunos")
def cadastrodealunos():
    return " Cadastro de alunos! <h1>Esta tela está reservada para construir a página de cadastro de alunos</h1>"


@app.route("/<usr>")
def name(usr):
    return f"<h1>{usr}</h1>"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nome"]
        #Conexao(user, idade, matricula)
        return redirect(url_for('name', usr=user))
        #return redirect(url_for('name2', name=user))
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run()'''



'''----------------------------------EX7---------------------------------'''


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

'''
@app.route("/<usr>")
def name(usr):
    return f"<h1>{usr}</h1>"'''


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nome"]
        #Conexao(user, idade, matricula)
        return redirect(url_for('name2', usr=user))
        #return redirect(url_for('name2', name=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def name2(usr):
    return render_template("index3.html", content=usr, parametro=["ai", "ei", "ou"])


if __name__ == "__main__":
    app.run()
    
#unir agora com o banco de dados do pgadmin, passando os parâmetros na função def name2 acima
