import sqlite3

def get_connection():
    """
    Retorna uma conexão com o banco de dados SQLite.
    """
    return sqlite3.connect('biblioteca.db')

def inicializar_bd():
    """
    Inicializa o banco de dados criando todas as tabelas necessárias.
    """
    conexao = get_connection()
    cursor = conexao.cursor()

    # Criar tabelas
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        ano INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cargo TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS leitores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        contato TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        livro_id INTEGER NOT NULL,
                        leitor_id INTEGER NOT NULL,
                        data_emprestimo TEXT NOT NULL,
                        data_devolucao TEXT,
                        FOREIGN KEY (livro_id) REFERENCES livros(id),
                        FOREIGN KEY (leitor_id) REFERENCES leitores(id))''')

    conexao.commit()
    conexao.close()
