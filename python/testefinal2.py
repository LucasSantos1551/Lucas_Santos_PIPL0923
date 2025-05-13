def calcular_desconto(compra):
    if 100 <= compra <= 200:
        return compra * 0.05
    elif 200 < compra < 500:
        return compra * 0.10
    elif compra >= 500:
        return compra * 0.15
    return 0

def inserir_cliente(clientes, numcli):
    nome = input("Nome do cliente: ")
    morada = input("Morada do cliente: ")
    telefone = input("Telefone do cliente: ")
    nif = input("NIF do cliente: ")
    compra = float(input("Valor da compra: "))
    
    desconto = calcular_desconto(compra)
    divfin = compra - desconto
    
    cliente = {
        "numcli": numcli,
        "nome": nome,
        "morada": morada,
        "telefone": telefone,
        "nif": nif,
        "compra": compra,
        "desconto": desconto,
        "divfin": divfin
    }
    
    clientes.append(cliente)
    print(f"Cliente {nome} inserido com sucesso!")

def listar_clientes(clientes):
    for cliente in clientes:
        print(f"\nNúmero Cliente: {cliente['numcli']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Morada: {cliente['morada']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"NIF: {cliente['nif']}")
        print(f"Compra: {cliente['compra']}")
        print(f"Desconto: {cliente['desconto']}")
        print(f"Divida Final: {cliente['divfin']}")
        continuar = input("Pressione Enter para continuar para o próximo cliente ou 'S' para parar: ")
        if continuar.lower() == 's':
            break

def buscar_cliente(clientes, numcli):
    for cliente in clientes:
        if cliente["numcli"] == numcli:
            print(f"\nNúmero Cliente: {cliente['numcli']}")
            print(f"Nome: {cliente['nome']}")
            print(f"Morada: {cliente['morada']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"NIF: {cliente['nif']}")
            print(f"Compra: {cliente['compra']}")
            print(f"Desconto: {cliente['desconto']}")
            print(f"Divida Final: {cliente['divfin']}")
            return
    print("Cliente não encontrado!")

def menu():
    clientes = []  
    numcli = 1    

    while True:
        print("\nMenu de Opções:")
        print("1. Inserir cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente por número")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            inserir_cliente(clientes, numcli)
            numcli += 1  
        elif opcao == '2':
            listar_clientes(clientes)
        elif opcao == '3':
            numcli_busca = int(input("Digite o número do cliente para busca: "))
            buscar_cliente(clientes, numcli_busca)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
menu()
