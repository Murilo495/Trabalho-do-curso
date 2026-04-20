valor = float(input("Qual o valor da compra: "))
categoria = input("Qual a sua categoria? a) comum b) vip c) funcionario: ")
vip = valor * 10 / 100
funcionario = valor * 20 / 100

if categoria == "vip":
    total = valor-vip

elif categoria == "funcionario":
    total = valor-funcionario

else:
    total = valor

print("Valor total da compra: ", total)

