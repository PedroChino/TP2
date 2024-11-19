from src import db_connection
from src import livros
from src import funcionarios
from src import leitores
from src import emprestimos

if __name__ == "__main__":
    db_connection.inicializar_bd()
    menu()
