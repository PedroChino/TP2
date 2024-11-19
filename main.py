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



if __name__ == "__main__":
    db_connection.inicializar_bd()
    menu()
