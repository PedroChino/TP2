import sqlite3

def get_connection():
    """
    Retorna uma conexão com o banco de dados SQLite.

    Funcionalidade:
        - Cria ou abre um arquivo de banco de dados SQLite chamado 'biblioteca.db'.
    
    Saída:
        - Objeto de conexão SQLite para interação com o banco de dados.

    Exceções:
        - Gera erro caso o arquivo do banco de dados não possa ser criado ou acessado.
    """
    return sqlite3.connect('biblioteca.db')

def inicializar_bd():
    """
    Inicializa o banco de dados criando todas as tabelas necessárias.

    Funcionalidade:
        - Verifica a existência das tabelas: 'livros', 'funcionarios', 'leitores' e 'emprestimos'.
        - Cria as tabelas caso ainda não existam no banco de dados.

    Processo:
        - Estabelece conexão com o banco de dados usando `get_connection`.
        - Executa comandos SQL `CREATE TABLE IF NOT EXISTS` para cada tabela:
            - `livros`: Armazena informações sobre os livros cadastrados.
            - `funcionarios`: Armazena dados sobre os funcionários da biblioteca.
            - `leitores`: Registra informações sobre os leitores.
            - `emprestimos`: Registra os empréstimos de livros pelos leitores.

    Estrutura das Tabelas:
        1. **Tabela: livros**
            - `id` (INTEGER PRIMARY KEY AUTOINCREMENT): Identificador único do livro.
            - `titulo` (TEXT NOT NULL): Título do livro.
            - `autor` (TEXT NOT NULL): Nome do autor do livro.
            - `ano` (INTEGER NOT NULL): Ano de publicação.

        2. **Tabela: funcionarios**
            - `id` (INTEGER PRIMARY KEY AUTOINCREMENT): Identificador único do funcionário.
            - `nome` (TEXT NOT NULL): Nome do funcionário.
            - `cargo` (TEXT NOT NULL): Cargo ocupado pelo funcionário.

        3. **Tabela: leitores**
            - `id` (INTEGER PRIMARY KEY AUTOINCREMENT): Identificador único do leitor.
            - `nome` (TEXT NOT NULL): Nome do leitor.
            - `contato` (TEXT NOT NULL): Informações de contato do leitor.

        4. **Tabela: emprestimos**
            - `id` (INTEGER PRIMARY KEY AUTOINCREMENT): Identificador único do empréstimo.
            - `livro_id` (INTEGER NOT NULL): ID do livro emprestado (relacionado à tabela `livros`).
            - `leitor_id` (INTEGER NOT NULL): ID do leitor que pegou o empréstimo (relacionado à tabela `leitores`).
            - `data_emprestimo` (TEXT NOT NULL): Data em que o empréstimo foi realizado.
            - `data_devolucao` (TEXT): Data em que o livro foi devolvido.
            - `FOREIGN KEY (livro_id)`: Referência à coluna `id` na tabela `livros`.
            - `FOREIGN KEY (leitor_id)`: Referência à coluna `id` na tabela `leitores`.

    Saída:
        - Cria ou mantém o banco de dados em um estado inicializado com as tabelas necessárias.

    Exceções:
        - Gera erro caso não consiga criar ou acessar as tabelas no banco de dados.
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
