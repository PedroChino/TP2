def carrega_as_listas_dos_ficheiros():
    """TODO: documentação"""

    lista_de_livros = le_de_ficheiro(nome_ficheiro_lista_de_livros)
    lista_de_leitores = le_de_ficheiro(nome_ficheiro_lista_de_leitores)
    lista_de_emprestimos = le_de_ficheiro(nome_ficheiro_lista_de_emprestimos)
    lista_de_funcionarios = le_de_ficheiro(nome_ficheiro_lista_de_funcionarios)

    return  lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios
