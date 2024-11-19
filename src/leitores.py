from io_terminal import imprime_lista

nome_ficheiro_lista_de_leitores = "lista_de_leitores.pk"

# Lista de leitores na memória
leitores = []

def cria_novo_leitor(nome, email, telefone, ativo=True):
    """Cria um novo leitor e adiciona à lista."""
    leitor = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "ativo": ativo
    }
    leitores.append(leitor)
    print(f"Leitor '{nome}' adicionado com sucesso!")
