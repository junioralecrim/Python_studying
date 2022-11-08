import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alunoaluno",
    database="turfe"
)

#pet: nome, tipo, raça - 6
#responsavel: nome, cpf, telefone - 3

c = db.cursor()

'''pet = [
    ('Bib', 'Cão', 'Buldogue'),
    ('Nuba', 'Cão', 'Buldogue'),
    ('Tite', 'Cão', 'Buldogue'),
    ('Dabi', 'Ave', 'Papagaio'),
    ('Neguin', 'Lagarto', 'Lagartixa'),
    ('Bob', 'Cobra', 'Naja')
]'''

responsavel = [
    ('Maria', '44444444444', '85888888888'),
    ('Jorge', '44444444445', '85888888888'),
    ('Pedro', '44444444446', '85888888888')
]

sql = "insert into responsavel (nome, cpf, telefone) values (%s, %s, %s)"
c.executemany(sql, responsavel)
db.commit()
print(c.rowcount)

c.close()
db.close()
