'''import mysql.connector
from flask import Flask'''

'''db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alunoaluno",
    database="turfe"
)'''



#Adicionando dados nas tabelas

'''
c = db.cursor()

responsavel = [
    ('Maria', '44444444444', '85888888888'),
    ('João', '44444444445', '85888888888'),
    ('José', '44444444446', '85888888888')
]


sql = "insert into responsavel (nome, cpf, telefone) values (%s, %s, %s)"
c.executemany(sql, responsavel)


pet = [
    (1, 'Bib', 'Cachorro', 'Buldogue'),
    (1, 'Nuba', 'Cachorro', 'Buldogue'),
    (1, 'Tite', 'Gato', 'Buldogue'),
    (2, 'Dabi', 'Passaro', 'Papagaio'),
    (3, 'Neguin', 'Gato', 'Lagartixa'),
    (3, 'Bob', 'Gato', 'Naja')
]


sql = "insert into pet (id_resp, nome, tipo, raca) values (%s, %s, %s, %s)"
c.executemany(sql, pet)
db.commit()
print(c.rowcount)

'''

#FAZERNDO CONSULTAS NA TABELA

## 1 - Buscar todos os pets de Maria
'''c = db.cursor()


c.execute(SELECT resp.nome, p.nome FROM responsavel as resp
            join pet as p 
            on resp.id = p.id_resp
            where resp.nome = 'Maria'
            ) # pra usar linha quebrada tem q usar os três '

for i in c.fetchall():
    print(i)

c.close()
db.close()'''


## 2 - Quais tipos de pets existem no DB

'''
c = db.cursor()

c.execute(
            SELECT tipo FROM pet


for i in c.fetchall():
    print(i)

c.close()
db.close()
'''


## 3 - Quais raças existem
'''
c = db.cursor()

c.execute(
            SELECT raca FROM pet
)

for i in c.fetchall():
    print(i)

c.close()
db.close()'''


## 4 - Quem são os responsáveis que possuem gatos
'''
c = db.cursor()

c.execute(
            SELECT r.nome FROM pet as p
            join responsavel as r
            on r.id = p.id_resp
            where tipo = 'Gato'
)

for i in c.fetchall():
    print(i)

c.close()
db.close()
'''


## 5 - Quem tem gato e não tem cachorro

'''
c = db.cursor()

c.execute(
            SELECT nome FROM responsavel
            WHERE id in (
                SELECT id_resp FROM pet
                WHERE tipo =  
                    (SELECT tipo FROM pet
                    where tipo not in (SELECT tipo FROM pet
                                        where tipo = 'Cachorro')))
)

for i in c.fetchall():
    print(i)

c.close()
db.close()
'''











#AULA 18   
'''
app = Flask(__name__)

@app.route("/pet")
def pets():

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alunoaluno",
    database="turfe"
    )


    c = db.cursor()


    c.execute(SELECT resp.nome, p.nome FROM responsavel as resp
                join pet as p 
                on resp.id = p.id_resp
                where resp.nome = 'Maria'
                ) # pra usar linha quebrada tem q usar os três
    
    return list(c.fetchmany())

'''


# AULA 19





import flask
from flask import request
from flask.globals import g

import mysql.connector as MySQLConnector


# Inicialização do banco de dados
#  adicionamos o handle do conector no contexto do
#  app do flask.
def init_db():
    g.db = MySQLConnector.connect(
        host="localhost",
        user="root",
        password="alunoaluno",
        database="turfe"
    )
    return g.db


# Recupera o handle do banco de dados
def get_db():
    if "db" not in g:
        g.db = init_db()
    
    return g.db

# Inicialização da aplicação flask
def init_app():
    app = flask.Flask(__name__)

    with app.app_context():
        init_db()

    return app

app = init_app()

# Fechamos a conexão com o banco de dados
#  quando a aplicação se encerra.
@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Rota raiz que diz se você conseguiu se conectar no banco de dados
@app.route("/")
def index():
    db = get_db()

    return "Is connected? %s" % ("Yes" if db.is_connected else "No")

# Implementar rota de listar todos os pets
# utilizando a conexão através do get_db()
@app.route("/pet/listar-pets", methods=["GET"])
def list_all_pets():
    db = get_db()
    c = db.cursor()
    c.execute('''SELECT nome FROM pet''')
    return list(c.fetchall()) #pega tudo de uma vez
    

# Implementar rota de listar um pet em específico
# Mostrar nome do dono/responsável ao invés do id
@app.route("/pet/<pet_id>")
def list_pet_by_id(pet_id):
    db = get_db()
    c = db.cursor()
    c.execute(f'''SELECT p.id, p.nome, tipo, raca, r.nome FROM pet as p 
                  JOIN responsavel as r
                  ON p.id_resp = r.id
                  where p.id = {pet_id}
                 ''')
    return c.fetchmany() #pega apenas um item e vai inteirando sobre ele (se eu fizer um for)
    

# Implementar rota pra inserção de um pet
# o método padrão é POST
@app.route("/pet/pet-via-post", methods=["POST"])
def insert_pet():
    # dados recebidos através do método post
    pet_data = request.form # dicionário contendo todos os dados recebidos de um pet
    print(pet_data)

    # Inserir utilizando os dados recebidos e utilizando o SQL
    pass

# Gerar rotas para os donos/responsáveis
# 1. Listar todos os donos
# 2. Listar um dono em específico e o nome de todos os pets que ele possuí
# 3. Inserir um dono novo





