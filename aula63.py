'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumentos (valor)
'''


def soma (x, y, z):
    # Definição da função
    print(f'{x=} y={y} {z=}', "|", "x + y =", x + y + z)

soma(1, 2, 3) # Não nomeado (mesma ordem)
soma(1, y=2, z=5) # nome do parametro + o valor do argumento, se for nomeado o proximo tbm tem
print(1, 2, 3, sep="-")


