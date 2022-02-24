# receber a data atual, o dia, mes e ano que a pessoa nasceu e imprimir
# quantidade de dias, meses e anos que se passaram da data de nascimento da pessoa até a data atual. Quantos dias 29/02 tem?

#nota: a cada 4 anos, têm-se um ano bissexto. Vamos considerar, para fins de facilitação, que o ano em que o usuário
#nasceu é o que começou a contagem dos 4 para o bissexto.

diaNascimento = int(input("\nDiga o dia em que você nasceu: "))
mesNascimento = int(input("Diga o mês em que você nasceu: "))
anoNascimento = int(input("Diga o ano em que você nasceu: "))

diaAtual = int(input("\nDiga o dia em que você está: "))
mesAtual = int(input("Diga o mês em que você está: "))
anoAtual = int(input("Diga o ano em que você está: "))

# ANO
#vamos saber quantos anos se passaram pra dividir o bissexto
if((diaAtual >= diaNascimento) and (mesAtual >= mesNascimento)):
    quantAno =  anoAtual - anoNascimento #aqui vai ter-se a quantidade de anos que se passaram
else:
    quantAno = (anoAtual - anoNascimento) - 1
    

#Agora é feita a quantidade de anos bissextos que existiram durante a vida do usuário até o momento
anosBi = quantAno/4
anosBi = int(anosBi)


#Agora vamos saber a quantidade de meses que existiram durante a vida da pessoa até o presente momento
quantMes = 12*quantAno

# Agora vamos saber a quantidade de dias #

#Os anos bi são adicionados a fórmula pois correspondem a quantidade de dias a mais que um ano tem tradicionalmente, isso considerando
#a vida do usuário até o momento. 

#O 30.41666...7 é o número de dias que cada mês tem em um ano comum para fazer o cálculo considerando que o usuário não está no seu 
# aniversário. 


if((diaAtual < diaNascimento) and (mesAtual < mesNascimento)):
    quantDias = ((365*quantAno)+anosBi) + diaAtual + (30.41666666666667*(mesAtual - 1))

else: 
    quantDias = ((365*quantAno)+anosBi) + diaAtual + (30.41666666666667*(mesAtual - 1))









