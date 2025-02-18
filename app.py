# snake_case para variaveis, funcoes e metodos
# PascalCase para classes

import os

def exibir_nome_projeto():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    ''')

def finalizar_app():
    os.system('cls')
    print('finalizando sistema...')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha a opção: '))
        match opcao_escolhida:
            case 1:
                print('Adicionar restaurante')
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurante')
            case 4:
                print('Finalizar app')
            case _:
                opcao_invalida()
    except:
            opcao_invalida()
            
            

def main():
    os.system('cls')
    exibir_nome_projeto()
    exibir_opcoes()
    escolher_opcao()

# Quando pedimos para que um programa Python seja executado, o interpretador
# cria uma variável chamada __name__. Se o __name__ for __main__ (principal, em inglês), significa que esse 
# código não será importado por outros scripts de código Python, e ele será o programa principal.
if __name__ == '__main__':
    main()
