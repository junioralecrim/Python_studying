#Imagine que você ganha um salário e que este ano haverá um reajuste.
#Peça para digitar o percentual de reajuste e aplique no salário
#mostre: O salário anterior, o valor do reajuste e o valor final

salario = float(input("Diga o valor do seu salário atual: "))
percentualReajuste = int(input("Agora diga o percentual do reajuste (sem o %): "))

salarioComReajuste = salario + (salario*(percentualReajuste/100))

print(f"\nO seu salário inicial era de {salario}\nO percentual do reajuste foi de {percentualReajuste}%\n\nAgora o seu salário com o reajuste será de {round (salarioComReajuste, 2)}")