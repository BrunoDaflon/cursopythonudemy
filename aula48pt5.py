'''
Cuidados com dados mutáveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memória
'''
#nome = "Bruno"
#noutra_variavel = nome
#nome = "Lorena"
#print(nome)
#print(noutra_variavel)

lista_a = ["Luiz", "Maria", 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = "Qualquer coisa"
print(lista_a)
print(lista_b)