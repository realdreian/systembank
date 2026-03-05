from funcoes import *


print("\n === Bem Vindo ao Banco DAPRASSA === \n")


while True:

    conta_usuario = cadastro_usuario()
    if conta_usuario != 'cpf invalido':
        print("\n Usuário Cadastrado com Sucesso \n")

    while True:
            menu_opcoes()
            opcao = input("Qual opção você deseja? ")

            match opcao:
                case "1": deposito(conta_usuario)
                case "2": sacar(conta_usuario)
                case "3": verificar_saldo(conta_usuario)
                case "4": mostrar_extrato(conta_usuario)
                case "5":
                    print("Encerrando o sistema...")
                    break                 
    break