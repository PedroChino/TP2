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
