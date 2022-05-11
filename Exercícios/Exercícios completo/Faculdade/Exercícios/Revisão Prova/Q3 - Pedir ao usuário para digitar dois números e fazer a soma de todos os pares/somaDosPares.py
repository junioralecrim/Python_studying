num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
lista = []
tupla = ()
somapares = 0

if (num2 > num1):
   for i in range(num1, num2):
       if(i%2 == 0):
           somapares += +i
           lista.append(i)
else:
   for i in range(num2, num1):
       if(i%2 == 0):
           somapares += +i
           lista.append(i)

tupla = lista

print(lista)

print(tupla)

#nao sei colocar itens em uma tupla
