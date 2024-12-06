#Operadores.Lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipe None que é
# usado para representar um não valor

# Falando de OR

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
#if TRUE condição
if (entrada == 'E' or entrada == "e") and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#Avaliação de curto circuito    
print(True and True and True)


senha = input("Senha: ") or "Sem senha"
print(senha)