'''
Dicionários em Python (Tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor"
Chaves podem ser consideradas como o 'índice'
que vimos na lista e podem ser de tipo imutáveis
como: str, int, float, bool, tuple, etc...
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list'''
pessoa = {
    "nome": "Bruno",
    "sobrenome": "Batista",
    "idade": "30",
    "altura": "1.8",
    "endereços": [
    {"rua": "tal tal", "numero": 123},
    {"rua": "outra rua", "numero": 321},
    ]
}
# pessoa = {
#     "nome": "Bruno Batista",
#     "sobrenome": "Pinto",
# }
# pessoa = dict(nome="Bruno", sobrenome="Batista")

# print(pessoa, type(pessoa))
print(pessoa["nome"])
print(pessoa["sobrenome"])
print()
for chave in pessoa:
    print(chave, pessoa[chave])
