'''
Repeticoes
while (enquanto)
Executa uma acao enquando a condicao for verdadeira
Loop infinito -> Quando um código nao tem fim
'''
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("NAO VOU MOSTRAR O 6.")
        continue

    if contador == 40:
        break
    
    if contador >= 10 and contador <= 27:
        print("Nao vou mostrar o", contador)
        continue
    

print("Acabou")