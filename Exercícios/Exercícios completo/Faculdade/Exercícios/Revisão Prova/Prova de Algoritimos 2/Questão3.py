num = int(input("Digite um número para saber se ele é ou não primo: "))
aux = 0

for i in range(1, num+1):
    if(num%i == 0):
        aux += +1
if(aux == 2):
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")



