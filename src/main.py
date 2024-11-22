import db_connection
import leitores
import funcionarios
import livros
import emprestimos

def menu():
    """
    Exibe o menu principal do sistema de biblioteca e gerencia a navegação entre opções.

    As opções incluem o gerenciamento de livros, funcionários, leitores e empréstimos.
    Permite ao usuário sair do programa.

    Menu:
        1. Gerenciar Livros
        2. Gerenciar Funcionários
        3. Gerenciar Leitores
        4. Gerenciar Empréstimos
        5. Sair

    Raises:
        ValueError: Caso uma entrada inválida seja fornecida.
    """
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Funcionários")
        print("3. Gerenciar Leitores")
        print("4. Gerenciar Empréstimos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            gerenciar_livros()
        elif opcao == "2":
            gerenciar_funcionarios()
        elif opcao == "3":
            gerenciar_leitores()
        elif opcao == "4":
            gerenciar_emprestimos()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def gerenciar_leitores():
    """
    Exibe o submenu para gerenciamento de leitores.

    Permite adicionar, listar, atualizar ou excluir leitores, além de retornar ao menu principal.

    Submenu:
        1. Adicionar Leitor
        2. Listar Leitores
        3. Atualizar Leitor
        4. Excluir Leitor
        5. Voltar

    Raises:
        ValueError: Caso uma entrada inválida seja fornecida.
    """
    while True:
        print("\n--- Gerenciar Leitores ---")
        print("1. Adicionar Leitor")
        print("2. Listar Leitores")
        print("3. Atualizar Leitor")
        print("4. Excluir Leitor")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            leitores.adicionar_leitor()
        elif opcao == "2":
            leitores.listar_leitores()
        elif opcao == "3":
            leitores.atualizar_leitor()
        elif opcao == "4":
            leitores.excluir_leitor()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")


def gerenciar_livros():
    while True:
        print("\n--- Gerenciar Livros ---")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Excluir Livro")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            livros.adicionar_livro()
        elif opcao == "2":
            livros.listar_livros()
        elif opcao == "3":
            livros.atualizar_livro()
        elif opcao == "4":
            livros.excluir_livro()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def gerenciar_funcionarios():
    while True:
        print("\n--- Gerenciar Funcionários ---")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            funcionarios.adicionar_funcionario()
        elif opcao == "2":
            funcionarios.listar_funcionarios()
        elif opcao == "3":
            funcionarios.atualizar_funcionario()
        elif opcao == "4":
            funcionarios.excluir_funcionario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def gerenciar_emprestimos():
    while True:
        print("\n--- Gerenciar Empréstimos ---")
        print("1. Registrar Empréstimo")
        print("2. Listar Empréstimos")
        print("3. Atualizar Empréstimo")
        print("4. Excluir Empréstimo")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            emprestimos.registrar_emprestimo()
        elif opcao == "2":
            emprestimos.listar_emprestimos()
        elif opcao == "3":
            emprestimos.atualizar_emprestimo()
        elif opcao == "4":
            emprestimos.excluir_emprestimo()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    db_connection.inicializar_bd()
    menu()
