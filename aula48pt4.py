'''
Lista em Python
Tipo list - mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
'''

lista_a = [1, 2 ,3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)