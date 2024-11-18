def le_de_ficheiro(nome_ficheiro):
    """Lê os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """

    try:
        with open(nome_ficheiro, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"O ficheiro {nome_ficheiro} não existe.")
        return []
