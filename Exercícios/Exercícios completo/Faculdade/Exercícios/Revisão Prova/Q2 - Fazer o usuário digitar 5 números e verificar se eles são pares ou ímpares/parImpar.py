for i in range(1, 6):
   num = int(input(f"Digite o {i}° número para verificar se ele é impar ou par: "))
   if(num%2 == 0):
       print(f'O número {num} é par\n')
   else:
       print(f'O número {num} é ímpar\n')