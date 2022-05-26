from openpyxl import load_workbook

#https://letscode.com.br/blog/aprenda-a-integrar-python-e-excel
#https://openpyxl.readthedocs.io/en/stable/tutorial.html

#caminho = 'AULAS-EAD-REGISTRO-DE-ATIVIDADE.xlsx'
caminho = 'trabalhandocomplanilhas.xlsx'
arquivo_excel = load_workbook(caminho, data_only=True)

def selectionSort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
    return array

planilha = arquivo_excel.active

alunos = []
mediaAlunos = []
mediaAlunos2 = []
auxMediaPonderada = 0

for i in range(7, 12):
    aluno = planilha[f"B{i}"].value
    nota1 = planilha[f"C{i}"].value
    nota2 = planilha[f"D{i}"].value
    nota3 = planilha[f"E{i}"].value

    alunos.append(aluno)
    e = (nota1 + nota2 + nota3)/3
    mediaAlunos.append(e)



for i in range(0, 5):
    print(f"Aluno: {alunos[i]}\nMédia: {mediaAlunos[i]}\n")

mediaAlunos = selectionSort(mediaAlunos)

for i in range(1, 4):
    mediaAlunos2.append(mediaAlunos[i])
    auxMediaPonderada += mediaAlunos[i]

print(f"\nMédia ponderada da turma: {auxMediaPonderada/3}")

