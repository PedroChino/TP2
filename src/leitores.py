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

def listar_leitores():
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM leitores")
    leitores = cursor.fetchall()
    conexao.close()
    
    if leitores:
        for leitor in leitores:
            print(f"ID: {leitor[0]}, Nome: {leitor[1]}, Contato: {leitor[2]}")
    else:
        print("Nenhum leitor encontrado.")

def atualizar_leitor():
    listar_leitores()
    leitor_id = int(input("ID do leitor a ser atualizado: "))
    novo_nome = input("Novo nome: ")
    novo_contato = input("Novo contato: ")
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("UPDATE leitores SET nome = ?, contato = ? WHERE id = ?", 
                   (novo_nome, novo_contato, leitor_id))
    conexao.commit()
    conexao.close()
    print("Leitor atualizado com sucesso!")

def excluir_leitor():
    listar_leitores()
    leitor_id = int(input("ID do leitor a ser excluído: "))
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM leitores WHERE id = ?", (leitor_id,))
    conexao.commit()
    conexao.close()
    print("Leitor excluído com sucesso!"