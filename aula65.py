'''
Escopo de funções em Python
Escopo siginifica o local onde aquele código pode atingir.
Existe o escopo flobal e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo apenas nomes do mesmo local
podem ser alcançados.
'''
x = 1


def escopo():
    #global x
    x = 10
    def outra_funcao():
        #global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)