from cadastrar_funcionario import cadastrar_funcionario
from listar_funcionarios import listar_funcionarios

def menu_principal():
    while True:
        print("\n Sistema de RH - Menu Principal")
        print("1 - Cadastrar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            print(" Encerrando o sistema. Até logo!")
            break
        else:
            print(" Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu_principal()

