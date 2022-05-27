import gspread

# https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf
gc = gspread.service_account(filename='../api.json')
sheets = \
    {'VENDAS': 'https://docs.google.com/spreadsheets/d/1dNsphjNxu9Wv3QEwcHbH2e5nu2O2VaIzj66BgXombUA/edit?usp=sharing'}


def carregarTabelasBase():
    for planilha in sheets.values():
        # essa parte serve para acessar a planilha, o comanda abaixo pode ser usado apenas escrevendo o título
        # da planilha entre aspas simples
        sh = gc.open_by_url(planilha)

    dado = sh.worksheet('Página1')

    # celula = dado.cell(linha, coluna).value
    celula = dado.cell(4, 6).value
    print("Lendo a Planilha: ", celula)


carregarTabelasBase()
