from src.db_connection import get_connection

def adicionar_funcionario():
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)", (nome, cargo))
    conexao.commit()
    conexao.close()
    print("Funcionário adicionado com sucesso!")

def listar_funcionarios():
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
