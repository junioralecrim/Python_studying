#nao vamos colocar os bissextos
#7 meses tem 31, um tem 28 e os outros 4 tem 30
 
i = 1
contadorDias_1 = 0
contadorDias_2 = 0
 
data1_Dia = int(input("Digite o dia em que você nasceu: "))
data1_Mes = int(input("Digite o mes em que você nasceu: "))
data1_Ano = int(input("Digite o ano em que você nasceu: "))
 
data2_Dia = int(input("\nDigite o dia em que você está: "))
data2_Mes = int(input("Digite o mes em que você está: "))
data2_Ano = int(input("Digite o ano em que você está: "))
 
#quantidade de anos
anos = (data2_Ano - data1_Ano) - 1

## ANO EM QUE A PESSOA ESTÁ ## 
#quantidade de dias no ano em que a pessoa está

while (i < data2_Mes):

    if((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12)):
        contadorDias_1 = contadorDias_1 + 31    

    if((i == 4) or (i == 6) or (i == 9) or (i == 11)):
        contadorDias_1 = contadorDias_1 + 30

    if(i == 2):
        contadorDias_1 = contadorDias_1 + 28
    
    i += 1


contadorDias_1 += data2_Dia

###########
i = (data1_Mes + 1)

while (i <= 12):

    if((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12)):
        contadorDias_2 = contadorDias_2 + 31    

    if((i == 4) or (i == 6) or (i == 9) or (i == 11)):
        contadorDias_2 = contadorDias_2 + 30

    if(i == 2):
        contadorDias_2 = contadorDias_2 + 28
    
    i += 1

##FALTA SÓ PEGAR O MÊS EXATO EM QUE SE ESTÁ, POIS ESTOU EXCLUINDO ELE POR COMPLETO E PRECISO TIRAR APENAS OS DIAS A PARTIR DA DATA QUE DIGITEI
contadorDias_2 = contadorDias_2 + (data1_Dia)

#teoricamente esta certo

totalDias = (contadorDias_1 + contadorDias_2) + (anos*365)

print(f"Anos de vida {anos}")
print(f"A quantidade de dias entre a data digitada e a data atual é: {contadorDias_2}")
