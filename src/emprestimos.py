from src.db_connection import get_connection
from src.livros import listar_livros
from src.leitores import listar_leitores

def registrar_emprestimo():
    """
    Lista os livros e leitores disponíveis, solicita informações do usuário e registra
    um novo empréstimo na tabela 'emprestimos' do banco de dados.

    Passos:
    1. Exibe a lista de livros disponíveis e solicita o ID do livro para empréstimo.
    2. Exibe a lista de leitores registrados e solicita o ID do leitor.
    3. Solicita a data do empréstimo e, opcionalmente, a data de devolução.
    4. Registra o empréstimo no banco de dados.

    Entradas:
    - ID do Livro
    - ID do Leitor
    - Data de Empréstimo (formato: YYYY-MM-DD)
    - Data de Devolução (opcional)

    Saída:
    - Mensagem de confirmação ao registrar o empréstimo.
    """
    listar_livros()
    livro_id = int(input("ID do livro para empréstimo: "))
    
    listar_leitores()
    leitor_id = int(input("ID do leitor: "))
    
    data_emprestimo = input("Data de empréstimo (YYYY-MM-DD): ")
    data_devolucao = input("Data de devolução (YYYY-MM-DD ou deixe vazio se não souber): ") or None
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO emprestimos (livro_id, leitor_id, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", 
        (livro_id, leitor_id, data_emprestimo, data_devolucao)
    )
    conexao.commit()
    conexao.close()
    print("Empréstimo registrado com sucesso!")

def listar_emprestimos():
    """
    Recupera e exibe todos os empréstimos registrados na tabela 'emprestimos',
    incluindo informações do livro, do leitor e das datas envolvidas.

    Saída:
    - Lista detalhada de empréstimos com ID, Livro, Leitor, Data de Empréstimo e Data de Devolução.
    - Mensagem indicando ausência de registros, caso nenhum empréstimo seja encontrado.
    """
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT e.id, l.titulo, le.nome, e.data_emprestimo, e.data_devolucao
        FROM emprestimos e
        JOIN livros l ON e.livro_id = l.id
        JOIN leitores le ON e.leitor_id = le.id
    ''')
    emprestimos = cursor.fetchall()
    conexao.close()
    
    if emprestimos:
        for emprestimo in emprestimos:
            print(f"ID: {emprestimo[0]}, Livro: {emprestimo[1]}, Leitor: {emprestimo[2]}, "
                  f"Empréstimo: {emprestimo[3]}, Devolução: {emprestimo[4]}")
    else:
        print("Nenhum empréstimo encontrado.")

def atualizar_emprestimo():
    """
    Permite ao usuário atualizar a data de devolução de um empréstimo existente.

    Passos:
    1. Exibe todos os empréstimos registrados.
    2. Solicita o ID do empréstimo a ser atualizado.
    3. Solicita a nova data de devolução.
    4. Atualiza o registro no banco de dados.

    Entradas:
    - ID do Empréstimo
    - Nova Data de Devolução (formato: YYYY-MM-DD)

    Saída:
    - Mensagem de confirmação ao atualizar o empréstimo.
    """
    listar_emprestimos()
    emprestimo_id = int(input("ID do empréstimo a ser atualizado: "))
    nova_data_devolucao = input("Nova data de devolução (YYYY-MM-DD): ")
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", 
        (nova_data_devolucao, emprestimo_id)
    )
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