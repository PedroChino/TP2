from src.db_connection import get_connection

def adicionar_leitor():
    nome = input("Nome: ")
    contato = input("Contato (e-mail/telefone): ")
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO leitores (nome, contato) VALUES (?, ?)", (nome, contato))
    conexao.commit()
    conexao.close()
    print("Leitor adicionado com sucesso!")