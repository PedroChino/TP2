from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_emprestimos = "lista_de_emprestimos.pk"


# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome emprestimos*.py existentes na pasta temp
# e faça um commit de cada vez.
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro emprestimos.py existente, deve apagar
# todos os outros ficheiros temp/emprestimos-*.py, e inclusive
# estes comentários

# ...
def cria_novo_emprestimo(lista_de_leitores, lista_de_livros, lista_de_funcionarios):
    """Pede ao utilizador para introduzir os dados de um novo emprestimo

    :return: dicionario com uma fatura, na forma
        {"leitor": <<id_leitor>>, "livro": <<id_livro>>, "funcionario": <<id_funcionario>>, "data": <<data>>, ...}
    """

    id_leitor = pergunta_id(questao="Qual o id do leitor?", lista=lista_de_leitores, mostra_lista=True)
    id_livro = pergunta_id(questao="Qual o id do livro?", lista=lista_de_livros, mostra_lista=True)
    id_funcionario = pergunta_id(questao="Qual o id do funcionario?", lista=lista_de_funcionarios, mostra_lista=True)
    # TODO: Pedir o resto dos dados da fatura, e não esquecer de os guardar no dicionario
    # ...

    emprestimo = {
        "leitor": id_leitor,
        "livro": id_livro,
        "funcionario": id_funcionario,
        "data": date.today(),
    }

    return emprestimo
