#
'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero_str = input('Vou dobrar o número que voçê digitar: ')

try: 
    numero_float = float(numero_str)
    print("FLOAT", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.0f}")
except:
    print("Isso náo é um número")
