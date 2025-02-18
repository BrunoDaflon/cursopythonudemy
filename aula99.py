from sys import path

import aula99_package.modulo
from aula99_package.modulo import soma_do_modulo
from aula99_package import modulo
from aula99_package.modulo import * #má pratica

print(soma_do_modulo(1,2))
print(aula99_package.modulo.soma_do_modulo(1,2))
print(modulo.soma_do_modulo(1,2))
print(variavel)

# print(*path, sep='\n')
