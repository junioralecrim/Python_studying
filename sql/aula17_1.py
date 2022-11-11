import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alunoaluno",
    database="turfe"
)



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

c = db.cursor()

c.execute('''
            SELECT nome FROM responsavel
            WHERE id in (
                SELECT id_resp FROM pet
                WHERE tipo =  
                    (SELECT tipo FROM pet
                    where tipo not in (SELECT tipo FROM pet
                                        where tipo = 'Cachorro')))
''')

for i in c.fetchall():
    print(i)

c.close()
db.close()
