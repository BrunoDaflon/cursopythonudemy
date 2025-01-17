# Yield from

def gen1():
    print('COMEçOU GEN 1')
    yield 1
    yield 2
    yield 3
    print("ACABOU GEN 1")

def gen2(gen):
    yield from gen()
    print('COMEçOU GEN 2')
    yield 4
    yield 5
    yield 6
    print("ACABOU GEN 2")

g = gen2(gen1)
for numero in g:
    print(numero)
