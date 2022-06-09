num = int(input("Digite um número qualquer para verificar se este é um palíndromo ou não: "))

lista = []
aux = 0

'''- Tenho que ir pegando sempre o último número
        se o último número for 0, eu multiplico o número que estou usando para retirar o resto da div (inicialmente 10)
        por 10, diminuo pelo primeiro número que tinha encontrado e divido por 10
        
        verifico quantas casas o número tem
        divido por 10, diminuo pela parte inteira dele, multiplico por 10
        
        pra isso eu tenho que pegar tanto somente a parte inteira dele pra ir me auxiliando, quanto a parte depois da 
        vírgula
        
        '''


'''while(num > 0):
    num = num/10
    aux = int(num) - num #pegando somente a parte fracionada
    aux = aux * 10
    num = int(num) #pegando a parte inteira
'''

num = num / 10
aux1 = int(num)
print(aux1)
print(num)

num = num - aux1

print(num)

#aux = num - (int(num))  # pegando somente a parte fracionada



aux = aux * 10



num = int(num)  # pegando a parte inteira

