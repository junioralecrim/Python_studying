import gspread

#https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf
gc = gspread.service_account(filename='projeto-teste-345723-aff6b27a9374.json')
sheets = \
    {'VENDAS':'https://docs.google.com/spreadsheets/d/1dNsphjNxu9Wv3QEwcHbH2e5nu2O2VaIzj66BgXombUA/edit?usp=sharing'}

def carregarTabelasBase():
    for planilha in sheets.values():
        sh = gc.open_by_url(planilha)
    dado = sh.worksheet('Página1')
    celula = dado.acell('F5').value
    print("Lendo a Planilha: ", celula)

carregarTabelasBase()