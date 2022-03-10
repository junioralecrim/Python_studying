print("\n----- MULTA DA MULTA POR EXCESSO DE KG DE PEIXE -----\n\n")
peso = int(input("Digite quantos KG de peixe você trouxe: "))

if(peso > 50):
    excesso = (peso - 50)*4
    print(f"A quantidade de KG de peixe trazida ultrapassou o limite estabelecido por lei.\nQuantidade trazida: {peso}\nValor da multa: R$ {excesso},00")
else:
    print(f"A quantidade de KG trazido ({peso}) não ultrapassou o limite estabelecido por lei.")
