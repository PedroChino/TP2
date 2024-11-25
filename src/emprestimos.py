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

def listar_emprestimos():
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute('''SELECT e.id, l.titulo, le.nome, e.data_emprestimo, e.data_devolucao
                      FROM emprestimos e
                      JOIN livros l ON e.livro_id = l.id
                      JOIN leitores le ON e.leitor_id = le.id''')
    emprestimos = cursor.fetchall()
    conexao.close()
    
    if emprestimos:
        for emprestimo in emprestimos:
            print(f"ID: {emprestimo[0]}, Livro: {emprestimo[1]}, Leitor: {emprestimo[2]}, "
                  f"Empréstimo: {emprestimo[3]}, Devolução: {emprestimo[4]}")
    else:
        print("Nenhum empréstimo encontrado.")

def atualizar_emprestimo():
    listar_emprestimos()
    emprestimo_id = int(input("ID do empréstimo a ser atualizado: "))
    nova_data_devolucao = input("Nova data de devolução (YYYY-MM-DD): ")
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", 
                   (nova_data_devolucao, emprestimo_id))
    conexao.commit()
    conexao.close()
    print("Empréstimo atualizado com sucesso!")

    def excluir_emprestimo():
        listar_emprestimos()
        emprestimo_id = int(input("ID do empréstimo a ser excluído: "))
        
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM emprestimos WHERE id = ?", (emprestimo_id,))
        conexao.commit()
        conexao.close()
        print("Empréstimo excluído com sucesso!")

