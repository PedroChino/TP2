from db_connection import get_connection

def adicionar_leitor():
    """
    Adiciona um novo leitor ao banco de dados.

    Solicita ao usuário o nome e o contato do leitor e insere os dados
    na tabela `leitores` do banco de dados.

    Inputs solicitados:
        - Nome (str): Nome do leitor.
        - Contato (str): E-mail ou telefone do leitor.

    Raises:
        Exception: Se ocorrer algum erro ao se conectar ou interagir com o banco de dados.

    Example:
        Nome: João Silva
        Contato: joao.silva@email.com
        Leitor adicionado com sucesso!
    """
    nome = input("Nome: ")
    contato = input("Contato (e-mail/telefone): ")
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO leitores (nome, contato) VALUES (?, ?)", (nome, contato))
    conexao.commit()
    conexao.close()
    print("Leitor adicionado com sucesso!")


def listar_leitores():
    """
    Lista todos os leitores cadastrados no banco de dados.

    Recupera os registros da tabela `leitores` e os exibe ao usuário no formato:
        - ID: ID do leitor.
        - Nome: Nome do leitor.
        - Contato: Contato do leitor.

    Raises:
        Exception: Se ocorrer algum erro ao se conectar ou inragir com o banco de dados.

    Example:
        ID: 1, Nome: João Silva, Contato: joao.silva@email.com
        ID: 2, Nome: Maria Souza, Contato: maria.souza@email.com
    """
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
    print("Leitor excluído com sucesso!")

