a = "AAAAA"
b = "BBBBB"
c = 1.1
string = "a={nome1} b={nome2} c={nome3:.2f}"
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)


a = "AAAAA"
b = "BBBBB"
c = 1.1
string = "a={} b={} c={:.2f}"
formato = string.format(a, b, c)
print(formato)


a = "AAAAA"
b = "BBBBB"
c = 1.1
string = "a={0} b={1} c={2:.2f}"
formato = string.format(a, b, c)
print(formato)