'''
Introdução às funções (def) em Python
Funções são techos de código usado para
prelicar adeterminada ação ao longo do seu codigo.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (Nada).
'''
#def Print(a, b, c):
#    print("Várias1")
#    print("Várias2")
#    print("Várias3")
#    print("Várias4")
    

#def imprimir(a, b, c):
#    print(a, b, c)

#imprimir(1, 2, 3)

def saudacao(nome="Sem nome"):
    print(f"Olá, {nome}!")

saudacao("Bruno Batista")
saudacao("Maria")
saudacao("Helena")
saudacao()