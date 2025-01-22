# Módulos padrão do Python (import, from, as e *)
# http://docs.python.org/3/py-modindex.html
# inteiro - import nome_produto
# Vantagens: Você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys
platform = "A minha"
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Descantagens: Sem o namespace do módulo
from sys import exit, platform
print("bla")

# aliás 1 - import nome_modulo as apelido

import sys as sisteminha
sys = 'algyma coisa'
print(sisteminha.platform)

# aliás 2 - from nome_modulo import objeto as apelido
from sys import platform as pf
from sys import exit as ex
print(pf)
print(ex)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagnes: importa tudo de um módulo
# Desvantagens: importa tudo de um mód
from sys import *
print(platform)
exit()