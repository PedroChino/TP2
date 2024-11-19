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

def listar_livros():
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conexao.close()
    
    if livros:
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}")
    else:
        print("Nenhum livro encontrado.")

def atualizar_livro():
    listar_livros()
    livro_id = int(input("ID do livro a ser atualizado: "))
    novo_titulo = input("Novo título: ")
    novo_autor = input("Novo autor: ")
    novo_ano = int(input("Novo ano: "))
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("UPDATE livros SET titulo = ?, autor = ?, ano = ? WHERE id = ?", 
                   (novo_titulo, novo_autor, novo_ano, livro_id))
    conexao.commit()
    conexao.close()
    print("Livro atualizado com sucesso!")

def excluir_livro():
    listar_livros()
    livro_id = int(input("ID do livro a ser excluído: "))
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conexao.commit()
    conexao.close()
    print("Livro excluído com sucesso!")