#imprimir o menor valor de uma lista de 5 inteiros
 
valores = []
for count in range(5):
    valores += input("Digite o %d° valor: " % (count+1))
 
print("\n")
print("O menor valor digitado foi:", min(valores))
   
