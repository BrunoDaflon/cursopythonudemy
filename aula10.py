nome = "Bruno Batista"
altura = 1.78
peso = 83
imc = peso / (altura * altura)

print(nome, "tem", altura, "de altura",)
print("pesa", peso, "quilos e seu imc é",)
print(imc)

linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} quilos e seu imc é"
linha_3 = f"{imc:.2f}"
print(linha_1)
print(linha_2)
print(linha_3)