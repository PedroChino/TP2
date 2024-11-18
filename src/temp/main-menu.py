def menu():
    """Menu principal da aplicação"""

    lista_de_livros = []
    lista_de_leitores = []
    lista_de_emprestimos = []
    lista_de_funcionarios = []

    while True:
        print("""
        *********************************************************************
        :                       BIBLIOTECA TECA-TECA                        :
        *********************************************************************
        :                                                                   :
        : ne  - novo emprestimo      le  - listagem de emprestimos          :
        : nlv - novo livro           llv - listagem de livros               :
        : nlt - novo leitor          llt - listagem de leitores             :
        : ...                                                               :
        : nf  - novo funcionário     lf - listagem de funcionários          :
        : ...                                                               :
        : g - guarda tudo            c - carrega tudo                       :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()

        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios)

        elif op == "c":
            lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios = carrega_as_listas_dos_ficheiros()

        elif op == "nlt":
            novo_leitor = cria_novo_leitor()
            if novo_leitor is not None:
                lista_de_leitores.append(novo_leitor)

        elif op == "nlv":
            novo_livro = cria_novo_livro()
            if novo_livro is not None:
                lista_de_livros.append(novo_livro)

        elif op == "nf":
            novo_funcionario = cria_novo_funcionario()
            if novo_funcionario is not None:
                lista_de_funcionarios.append(novo_funcionario)

        elif op == "ne":
            if len(lista_de_leitores) == 0 or len(lista_de_livros) == 0 or len(lista_de_funcionarios) == 0:
                print("Não há leitores ou funcionarios ou livros registados...")
                continue

            novo_emprestimo = cria_novo_emprestimo(lista_de_leitores, lista_de_livros, lista_de_funcionarios)
            lista_de_emprestimos.append(novo_emprestimo)

        elif op == "llt":
            imprime_lista_de_leitores(lista_de_leitores)
            pausa()

        elif op == "llv":
            imprime_lista_de_livros(lista_de_livros)
            pausa()

        elif op == "lf":
            imprime_lista_de_funcionarios(lista_de_funcionarios)
            pausa()

        elif op == "le":
            imprime_lista_de_emprestimos(lista_de_emprestimos)
            pausa()
