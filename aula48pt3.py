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
#........0....1...2...3..
lista = [10, 20, 30, 40]
lista.append("Bruno")
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(0, 5)
print(lista)