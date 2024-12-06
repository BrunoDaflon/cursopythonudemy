# Operadores in e not in
# Strings são iteráveis
#  0  1  2  3  4 
#  B  R  U  N  O
# -5 -4 -3 -2 -1
nome = "Bruno"
print(nome[2])
print(nome[-3])

print("z" in nome)
print("uno" in nome)
print(10 * "-")
print("uno" not in nome)
print("zero" in nome)


nome = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")
