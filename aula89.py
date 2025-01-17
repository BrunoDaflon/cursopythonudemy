# dir, hasattr e getattr em Python
string = 'Bruno'
metodo = 'upper1'
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string,metodo)())
    # print(string.upper())
else:
    print('Não existe o método', metodo)

