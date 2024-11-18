def cria_novo_livro():
    """Pede ao utilizador para introduzir um novo livro

    :return: dicionario com um livro na forma
        {"titulo": <<titulo>>, "autor": <<autor>>, ...}
    """

    titulo = input("titulo? ").title()
    autor = input("autor? ").title()
    # TODO: Pedir o resto dos dados do livro, e não esquecer de os guardar no dicionario
    # ...

    livro = {
        "titulo": titulo,
        "autor": autor,
        }

    return livro
