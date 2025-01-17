# Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a
# print(a,b)

pessoa = {
    'nome': 'Bruno',
    'sobrenome': 'Batista',
}

dados_pessoa = {
    'idade': 30,
    'altura': 1.76,
}

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)


# args e kwargs
# args (já vimos)
# kwargs - Keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

#mostro_argumentos_nomeados(nome='Bruno', qlqr=123)
#mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    "arg1": 1,
    "arg2": 2,
    "arg3": 3,
    "arg4": 4,
}

mostro_argumentos_nomeados(**configuracoes)