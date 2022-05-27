import gspread

def tratamentoString(linha, coluna):
    celula = dado.cell(linha, coluna+2).value
    celula = int(celula[3:(len(celula)) - 3])
    return celula

def tratamentoLista(lista, valor): #essa função serve para capturar os valores, só que ela precisa que tenha algum valor dentro da lista ja
    for i in range(len(lista)):
        if(valor == lista[i]):
            return lista
        else:
            if (i == (len(lista) - 1)):
                lista.append(valor)
                return lista

pessoaArthur = 0
pessoaAlice = 0
pessoaMatheus = 0
pessoas = [0] #usando um dicionário pra colocar o nome das pessoas
pessoasT = ('arthur', 'matheus', 'alice')
colunas = ('vendedor')

#essa parte é a minha chave de acesso do google drive à API do google sheets
gc = gspread.service_account(filename='api.json')
sheets = \
    {'VENDAS':'https://docs.google.com/spreadsheets/d/1dNsphjNxu9Wv3QEwcHbH2e5nu2O2VaIzj66BgXombUA/edit?usp=sharing'}

for planilha in sheets.values():
   sh = gc.open_by_url(planilha)
dado = sh.worksheet('Página1')
#

print('| : Carregando...')
for k in range(1, 9): #fazendo a busca da célula dos vendedores para capturar o nome de cada um e fazer a soma das comissões por pessoa
    celula = dado.cell(4, k).value
    tituloCelula = celula.lower()
    print("|")
    #print(f"Procurando coluna vendedor - {tituloCelula}")

    if(colunas == tituloCelula):
        #a partir daqui ele tem que buscar as correspondecias de nome e ir somando dentro de uma lista
       for i in range(5, 23):
            print("|")
            celula = dado.cell(i, k).value #aqui está sendo capturada a string
            tituloCelula = celula.lower()
            ##print('\n')
            ##print(f"Coletando nomes dos vendedores de forma unificada - {tituloCelula}")

            if(pessoas[0] == 0): #essa parte vai servir pra adicionar o primeiro nome sempre.
                pessoas[0] = tituloCelula
            pessoas = tratamentoLista(pessoas, tituloCelula) #função para eliminar repetições de nomes nas lista de vendedores
            #print(f'Unificando lista de vendedores: {pessoas}')

            if(tituloCelula == pessoasT[0]): #pra passar isso pra função, eu vou precisar repassar os valores de i, k
                pessoaArthur += tratamentoString(i, k)

            if (tituloCelula == pessoasT[1]):
                pessoaMatheus += tratamentoString(i, k)

            if (tituloCelula == pessoasT[2]):
                pessoaAlice += tratamentoString(i, k)

print(f"\n\nArthur: {pessoaArthur}\nMatheus: {pessoaMatheus}\nAlice: {pessoaAlice}")



