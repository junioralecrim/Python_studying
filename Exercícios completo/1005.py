#Média aluno com verificação

nota1 = float(input("Digite o primeiro valor: "))
if (nota1 > 10.0) or (nota1 < 0.00):
    print("A nota precisa estar entre 0.00 e 10.00!")
    
else:
    nota2 = float(input("Digite o segundo valor: "))    
    if (nota2 > 10.0) or (nota2 < 0.00):
        print("A nota precisa estar entre 0.00 e 10.00!")

soma = ((nota1*3.7) + (nota2*7.3))/11

print("A nota do aluno é: {:.2f}\n".format(soma))



