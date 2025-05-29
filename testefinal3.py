fornecedores = []
contador_numfor = 1
 
def validar_telefone():
    while True:
        telefone = input("Telefone : ")
        if len(telefone) == 9 and telefone.isdigit():
            return telefone
        print("Tem de ter 9 digitos")
 
def validar_nif():
    while True:
        nif = input("NIF : ")
        if len(nif) == 9 and nif.isdigit():  
            return nif
        print("Tem de ter 9 digitos")
 
def calcular_desconto(valor):
    if 1000 <= valor <= 5000:
        return valor * 0.08
    elif 5001 <= valor <= 10000:
        return valor * 0.12
    elif valor > 10000:
        return valor * 0.18
    else:
        return 0
 
def inserir_fornecedor():
    global contador_numfor
    print("\n--- Inserir novo fornecedor ---")
    nome = input("Nome do fornecedor: ")
    endereco = input("Endereco: ")
    telefone = validar_telefone()
    nif = validar_nif()
   
    while True:
        try:
            valor = float(input("Valor fornecido : "))
            if valor < 0:
                print("Valor nao pode ser negativo!")
                continue
            break
        except ValueError:
            print("Valor invalido! Digite um numero.")
   
    desconto = calcular_desconto(valor)
    valor_final = valor - desconto
   
    fornecedor = {
        "NumFor": contador_numfor,
        "NomeFor": nome,
        "Endereco": endereco,
        "Telefone": telefone,
        "NIF": nif,
        "ValorFornecido": valor,
        "Desconto": desconto,
        "ValorFinal": valor_final
    }
   
    fornecedores.append(fornecedor)
    print(f"Fornecedor inserido! Numero: {contador_numfor}")
    contador_numfor += 1
 
def mostrar_fornecedor(f):
    print(f"\nNumFor: {f['NumFor']}")
    print(f"Nome: {f['NomeFor']}")
    print(f"Endereco: {f['Endereco']}")
    print(f"Telefone: {f['Telefone']}")
    print(f"NIF: {f['NIF']}")
    print(f"Valor Fornecido: €{f['ValorFornecido']:.2f}")
    print(f"Desconto: €{f['Desconto']:.2f}")
    print(f"Valor Final: €{f['ValorFinal']:.2f}")
 
def listar_fornecedores():
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return
    for f in fornecedores:
        mostrar_fornecedor(f)
        input("Pressione Enter para continuar...")
 
def buscar_fornecedor():
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return
    try:
        num_str = input("Digite o numero do fornecedor: ")
        num = int(num_str)
    except ValueError:
        print("Numero invalido!")
        return
   
    for f in fornecedores:
        if f['NumFor'] == num:
            print("\n--- Dados do Fornecedor ---")
            mostrar_fornecedor(f)
            return
    print("Fornecedor nao encontrado.")
 
 
def menu():
    while True:
        print("\n--- Menu Fornecedores ---")
        print("1 - Inserir fornecedor")
        print("2 - Listar fornecedores")
        print("3 - Buscar fornecedor")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ")
       
        match opcao:
            case "1":
                inserir_fornecedor()
            case "2":
                listar_fornecedores()
            case "3":
                buscar_fornecedor()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opcao invalida!")
 
menu()
 