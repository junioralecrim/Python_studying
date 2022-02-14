#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
# o valor que recebe por hora e calcula o salário desse funcionário. 
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

numFuncionário = input("\nDigite o número do funcionário: ")
horasTrabalhadas = float(input("\nDiga quantas horas você trabalha na semana: "))
recebidoHora = float(input("\nMuito bem! Agora diga quanto você recebe por hora: "))

salarioSemanal = (horasTrabalhadas*recebidoHora)

print("\nO valor semanal recebido pelo funcionário " + numFuncionário + " é: R$ {:.2f}".format(salarioSemanal))


