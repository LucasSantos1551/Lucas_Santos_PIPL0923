livros = []
LIMITE_LIVROS = 100
 
def adicionar_livro():
    if len(livros) >= LIMITE_LIVROS:
        print("Limite de livros atingido.")
        return
 
    titulo = input("Titulo do livro: ").lower()
    autor = input("Autor do livro: ").lower()
    try:
        ano = int(input("Ano de publicacao: "))
    except ValueError:
        print("Ano invalido. Tente novamente.")
        return
 
    for livro in livros:
        if livro["titulo"] == titulo and livro["autor"] == autor:
            print("Livro ja cadastrado.")
            return
 
    novo = {"titulo": titulo, "autor": autor, "ano": ano}
    livros.append(novo)
    print("Livro adicionado com sucesso!")
 
def procurar_livro():
    termo = input("Digite o titulo ou autor para procurar: ").lower()
    encontrados = []
 
    for i, livro in enumerate(livros):
        if termo in livro["titulo"] or termo in livro["autor"]:
            encontrados.append((i, livro))
 
    if encontrados:
        print("\nLivros encontrados:")
        for pos, livro in encontrados:
            print(f"Posicao {pos}: Titulo: {livro['titulo'].title()}, Autor: {livro['autor'].title()}, Ano: {livro['ano']}")
    else:
        print("Nenhum livro encontrado com esse termo.")
 
def excluir_livro():
    try:
        pos = int(input("Informe a posicao do livro a excluir: "))
        if 0 <= pos < len(livros):
            removido = livros.pop(pos)
            print(f"Livro '{removido['titulo'].title()}' removido com sucesso.")
        else:
            print("Posicao invalida.")
    except ValueError:
        print("Entrada invalida. Informe um numero.")
 
def ordenar_livros():
    print("Ordenar por:")
    print("1 - Titulo")
    print("2 - Autor")
    op = input("Escolha a opcao: ")
 
    match op:
        case '1':
            livros.sort(key=lambda x: x["titulo"])
            print("Livros ordenados por titulo.")
        case '2':
            livros.sort(key=lambda x: x["autor"])
            print("Livros ordenados por autor.")
        case _:
            print("Opcao invalida.")
 
def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
 
    print("\nLista de Livros:")
    for i, livro in enumerate(livros):
        print(f"{i}: Titulo: {livro['titulo'].title()}, Autor: {livro['autor'].title()}, Ano: {livro['ano']}")
 
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar novo livro")
        print("2 - Procurar por titulo ou autor")
        print("3 - Excluir livro")
        print("4 - Ordenar livros")
        print("5 - Listar livros")
        print("6 - Sair do programa")
 
        opcao = input("Escolha uma opcao: ")
 
        match opcao:
            case '1':
                adicionar_livro()
            case '2':
                procurar_livro()
            case '3':
                excluir_livro()
            case '4':
                ordenar_livros()
            case '5':
                listar_livros()
            case '6':
                print("Saindo do programa...")
                break
            case _:
                print("Opcao invalida. Tente novamente.")
 
menu()
 