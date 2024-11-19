from src import db_connection
from src import livros
from src import funcionarios
from src import leitores
from src import emprestimos

def menu():
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
            leitores.listar_leitorer()
        elif opcao == "3":
            leitores.atualizar_leitor()
        elif opcao == "4":
            leitores.excluir_leitor()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    db_connection.inicializar_bd()
    menu()
