'''
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possivilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra,
você vai conferir se a letra digitada está
na palavra secreta.
    - se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário
'''
import os

palavra_secreta = "flamengo"
letras_acertadas = ""
numero_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print("Palavra formada: ", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("VOCÊ ACERTOU!!! PARABÉNS!!!")
        print("A palavra é ",palavra_formada)
        print("Tentativas: ",numero_tentativas)
        letras_acertadas = ""
        numero_tentativas = 0
        break