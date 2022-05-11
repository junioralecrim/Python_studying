v = [32, 1, 21, 59, 12, 7, 41, 16]
vAux = []
maxim = 0

for i in range(len(v)):
   aux = v[i]
   print(f"Auxiliar = {aux}")
   for j in range(len(v)):
       if(aux <= v[j]):
           print(f"Vetor: {v[j]}") #ele tá printando só os maiores que ele
           maxim = v[j]
           break
       else:
           print(f"Aqui precisa estar printado somente o 41: {aux}")

print(maxim)




def sort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
