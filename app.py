# snake_case para variaveis, funcoes e metodos
# PascalCase para classes

import os

restaurantes = ['Madero', 'Outback']

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
    exibir_subtitulo('Finalizando sistema...\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal.\n')
    main()

def cadastrar_restaurantes():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

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
                cadastrar_restaurantes()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
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
