from db_connection import get_connection

def adicionar_livro():
    """
    Adiciona um novo livro ao banco de dados.

    Funcionalidade:
        - Solicita ao usuário informações do livro (Título, Autor, Ano).
        - Insere os dados no banco de dados.

    Entrada:
        - Título: Nome do livro (string).
        - Autor: Nome do autor do livro (string).
        - Ano: Ano de publicação do livro (inteiro).

    Processo:
        - Estabelece conexão com o banco de dados.
        - Executa a query SQL `INSERT` para adicionar os dados.
        - Fecha a conexão com o banco de dados.

    Saída:
        - Mensagem de confirmação: "Livro adicionado com sucesso!"

    Exceções:
        - Gera erro caso não consiga se conectar ao banco de dados.
        - Gera erro caso as entradas sejam inválidas.
    """
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
    """
    Lista todos os livros cadastrados no banco de dados.

    Funcionalidade:
        - Conecta ao banco de dados.
        - Recupera todos os registros da tabela `livros`.

    Processo:
        - Executa a query SQL `SELECT * FROM livros`.
        - Itera pelos resultados e exibe os detalhes de cada livro:
            - ID
            - Título
            - Autor
            - Ano
        - Fecha a conexão com o banco de dados.

    Saída:
        - Lista de livros formatada.
        - Mensagem "Nenhum livro encontrado." caso não existam registros.

    Exceções:
        - Gera erro caso não consiga se conectar ao banco de dados.
        - Gera erro caso a tabela `livros` não exista ou esteja vazia.
    """
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
    """
    Atualiza as informações de um livro existente no banco de dados.

    Funcionalidade:
        - Solicita ao usuário o ID do livro a ser atualizado.
        - Permite modificar Título, Autor e Ano do livro.

    Entrada:
        - ID do Livro: Identificador único do livro (inteiro).
        - Novo Título: Novo nome do livro (string).
        - Novo Autor: Novo nome do autor (string).
        - Novo Ano: Novo ano de publicação (inteiro).

    Processo:
        - Lista todos os livros para referência.
        - Solicita os novos dados.
        - Executa a query SQL `UPDATE` para modificar os registros.
        - Fecha a conexão com o banco de dados.

    Saída:
        - Mensagem de confirmação: "Livro atualizado com sucesso!"

    Exceções:
        - Gera erro caso o ID não exista no banco de dados.
        - Gera erro caso a tabela `livros` não contenha o registro solicitado.
    """
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
    """
    Exclui um livro do banco de dados com base no ID fornecido.

    Funcionalidade:
        - Solicita ao usuário o ID do livro que deseja excluir.
        - Remove o registro correspondente da tabela `livros`.

    Entrada:
        - ID do Livro: Identificador único do livro (inteiro).

    Processo:
        - Lista todos os livros para referência.
        - Solicita o ID do livro a ser excluído.
        - Executa a query SQL `DELETE` para remover o registro.
        - Fecha a conexão com o banco de dados.

    Saída:
        - Mensagem de confirmação: "Livro excluído com sucesso!"

    Exceções:
        - Gera erro caso o ID fornecido não exista no banco de dados.
        - Gera erro caso a tabela `livros` esteja vazia ou não exista.
    """
    listar_livros()
    livro_id = int(input("ID do livro a ser excluído: "))
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conexao.commit()
    conexao.close()
    print("Livro excluído com sucesso!")
