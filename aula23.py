#
"""
Formatação básica de strings
s - string
d - int 
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - Força o número a aparecer antes dos zeros
sinal - + ou - 
Ex.: 0>-100,.1f
conversion flags - !f !s !a __repr__
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}.")
print(f"{variavel: ^10}.")
print(f"{variavel:$^10}.")
print(f"{1000.4873648123746:,.1f}")
print(f"{1000.4873648123746:+,.1f}")
print(f"{1000.4873648123746:-,.1f}")
print(f"{1000.4873648123746:0>+10,.1f}")
print(f"{1000.4873648123746:0=+10,.1f}")
print(f"O hexadecimal de 1500 é {1500:08X}")
print(f"{variavel!r}")

