# A função lambda em python
# A função lambda é uma função como qualquer 
# outra em python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [
#     {'nome': 'Bruno', 'sobrenome': 'Batista'},
#     {'nome': 'Luiz', 'sobrenome': 'Miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Silva'},
#     {'nome': 'Daniel', 'sobrenome': 'Oliveira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
    
# ]

# lista = [4,31,1,24,5,6,6,21,]
# lista.sort(reverse=True)
# print(lista)

lista = [
    {'nome': 'Bruno', 'sobrenome': 'Batista'},
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Silva'},
    {'nome': 'Daniel', 'sobrenome': 'Oliveira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
    
]

# def ordena(item):
#     return item['nome']


# lista.sort(key=ordena)

# for item in lista:
#     print(item)


# AGORA EXPLICANDO COM LAMBDA
# lista.sort(key=lambda item: item['nome'])

# for item in lista:
#     print(item)






# Se eu quiser uma nova lista

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])


exibir(l1)
exibir(l2)