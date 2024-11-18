def guarda_as_listas_em_ficheiros(lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios):
    """TODO: documentação

    :param lista_de_livros:
    :param lista_de_leitores:
    :param lista_de_emprestimos:
    :param lista_de_funcionarios:
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_livros, lista_de_livros)
        guarda_em_ficheiro(nome_ficheiro_lista_de_leitores, lista_de_leitores)
        guarda_em_ficheiro(nome_ficheiro_lista_de_emprestimos, lista_de_emprestimos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_funcionarios, lista_de_funcionarios)
    else:
        print("Gravação cancelada...")
