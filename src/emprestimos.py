from src.db_connection import get_connection
from src.livros import listar_livros
from src.leitores import listar_leitores

def registrar_emprestimo():
    listar_livros()
    livro_id = int(input("ID do livro para empréstimo: "))
    
    listar_leitores()
    leitor_id = int(input("ID do leitor: "))
    
    data_emprestimo = input("Data de empréstimo (YYYY-MM-DD): ")
    data_devolucao = input("Data de devolução (YYYY-MM-DD ou deixe vazio se não souber): ") or None
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO emprestimos (livro_id, leitor_id, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", 
                   (livro_id, leitor_id, data_emprestimo, data_devolucao))
    conexao.commit()
    conexao.close()
    print("Empréstimo registrado com sucesso!")