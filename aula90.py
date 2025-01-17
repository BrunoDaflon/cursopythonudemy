# Generator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__e__next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))

for n in generator:
    print(n)
