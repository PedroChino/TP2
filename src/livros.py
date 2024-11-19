from src.db_connection import get_connection

def adicionar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)", (titulo, autor, ano))
    conexao.commit()
    conexao.close()
    print("Livro adicionado com sucesso!")