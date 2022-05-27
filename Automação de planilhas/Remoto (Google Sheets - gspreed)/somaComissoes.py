import gspread

quantTotal = 0
listaComissoes = []
acharComissao = 'valor comissão'

#https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf

#essa parte é a minha chave de acesso do google drive à API do google sheets
gc = gspread.service_account(filename='api.json')
sheets = \
    {'VENDAS':'https://docs.google.com/spreadsheets/d/1dNsphjNxu9Wv3QEwcHbH2e5nu2O2VaIzj66BgXombUA/edit?usp=sharing'}

for planilha in sheets.values():
   sh = gc.open_by_url(planilha)

dado = sh.worksheet('Página1')

#nessa parte eu estou fazendo a busca de qual coluna que está o que eu quero somar. No caso, as comissões
for j in range(1, 9):
    celula = dado.cell(4, j).value
    tituloCelula = celula.lower()
    print(f"Buscando celula 'valor comissão' - {tituloCelula}")

    if (acharComissao == tituloCelula): #quando eu achar qual coluna está as comissões, vou fazer as somas
        #acessando os dados da coluna 8 e linha da 5(4) à 20
        for i in range(5, 23):
             celula = dado.cell(i, j).value
             #tratamento dos dados para transformar a string em um número do tipo float ou int
             quantStringFinal = len(celula)
             quantStringInicio = quantStringFinal - 6 ##PROBLEMA: Se os valores forem maior que 4 dígitos, não funciona.  
             quantStringFinal = quantStringFinal - 3
             celula = int(celula[quantStringInicio:quantStringFinal]) #essa parte está separando apenas os números

             quantTotal = quantTotal + celula


print(f"\nSoma total das comissões: {quantTotal}")
