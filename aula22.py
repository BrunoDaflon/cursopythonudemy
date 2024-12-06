# 
"""
Interpolação basica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Bruno"
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) 
#entre parenteses tem o mesmo valor da variavel por isso funciona.
print(variavel)
print("O hexadecimal de %d é %04x" % (1500, 1500))