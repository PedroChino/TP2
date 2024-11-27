from db_connection import get_connection

def adicionar_funcionario():
    """
    Adiciona um novo funcionário ao banco de dados.

    Solicita ao usuário o nome e o cargo do funcionário e insere os dados
    na tabela `funcionarios` do banco de dados.

    Inputs:
        - Nome (str): Nome do funcionário.
        - Cargo (str): Cargo do funcionário.

    Raises:
        Exception: Caso ocorra algum erro ao se conectar ou interagir com o banco de dados.

    Example:
        Nome: Ana Souza
        Cargo: Gerente
        Funcionário adicionado com sucesso!
    """
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)", (nome, cargo))
    conexao.commit()
    conexao.close()
    print("Funcionário adicionado com sucesso!")

def listar_funcionarios():
    """
    Lista todos os funcionários cadastrados no banco de dados.

    Recupera os registros da tabela `funcionarios` e os exibe ao usuário no formato:
        - ID: Identificador único do funcionário.
        - Nome: Nome do funcionário.
        - Cargo: Cargo do funcionário.

    Raises:
        Exception: Caso ocorra algum erro ao se conectar ou interagir com o banco de dados.

    Example:
        ID: 1, Nome: Ana Souza, Cargo: Gerente
        ID: 2, Nome: Carlos Lima, Cargo: Assistente
    """
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    conexao.close()
    
    if funcionarios:
        for funcionario in funcionarios:
            print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}")
    else:
        print("Nenhum funcionário encontrado.")

def atualizar_funcionario():
    """
    Atualiza as informações de um funcionário no banco de dados.

    Solicita ao usuário o ID do funcionário, o novo nome e o novo cargo, 
    e atualiza as informações na tabela `funcionarios`.

    Inputs:
        - ID do funcionário (int): Identificador único do funcionário.
        - Novo nome (str): Nome atualizado do funcionário.
        - Novo cargo (str): Cargo atualizado do funcionário.

    Raises:
        Exception: Caso ocorra algum erro ao se conectar ou interagir com o banco de dados.

    Example:
        ID do funcionário a ser atualizado: 1
        Novo nome: Ana Carolina Souza
        Novo cargo: Diretora
        Funcionário atualizado com sucesso!
    """
    listar_funcionarios()
    funcionario_id = int(input("ID do funcionário a ser atualizado: "))
    novo_nome = input("Novo nome: ")
    novo_cargo = input("Novo cargo: ")

    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("UPDATE funcionarios SET nome = ?, cargo = ? WHERE id = ?", 
                   (novo_nome, novo_cargo, funcionario_id))
    conexao.commit()
    conexao.close()
    print("Funcionário atualizado com sucesso!")

def excluir_funcionario():
    listar_funcionarios()
    funcionario_id = int(input("ID do funcionário a ser excluído: "))
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (funcionario_id,))
    conexao.commit()
    conexao.close()
    print("Funcionário excluído com sucesso!")
