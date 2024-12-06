'''
Faça uma lista de compras com lista
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na sua lista,
'''
import os

lista = []
while True:
    print('Selecione uma opção!')
    opcao = input("Para a sua lista, gostaria de\n[i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system("cls")
        valor = input("Inserir: ")
        lista.append(valor) 
    elif opcao == 'a':
        indice_str = input(
            "Escolha o item para apagar: "
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Por favor digite número int")
        except IndexError:
            print("Índice não existe na lista")
        except Exception:
            print("Erro desconhecido")           
    elif opcao == 'l':
        os.system("cls")

        if len(lista) == 0:
            print("Nada para listar")
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print("Por favor, escolha i, a ou l.")