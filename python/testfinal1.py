def e_primo(num: int):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def num_divisores(num: int):
    divs = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divs += 1
    return divs

def num_perfeitos(limite: int):
    num = 0
    for i in range(1, limite + 1):
        soma = 0
        for n in range(1, i):
            if i % n == 0:
                soma += n
        if soma == i:
            num += 1
    return num

num = int(input("Introduza um número: "))
vezes = 0

for i in range(num, 0, -1):
    if vezes % 10 == 0 and vezes != 0:
        res = input("Deseja continuar? S ou N: ")
        if res == 'N':
            break
    print(f"O número {i}, tem {num_divisores(i)} divisores, tem {num_perfeitos(i)} números perfeitos.", end=" ")
    if e_primo(i):
        print("e é primo.")
    else:
        print("não é primo.")
    
    vezes += 1

while True:
    operacoes = "+-*/."
    print("\nCalculadora")
    print("\t+")
    print("\t-")
    print("\t*")
    print("\t/")    
    print("\t. - para mostrar a tabuada\n")
    
    operacao = input("Introduza a operação: ")
    if operacao in operacoes:
        break

if operacao == ".":
    num = int(input("Introduza o número para a tabuada: "))
    i = 1
    while i <= 10:
        if i % 20 == 1 and i != 1:
            res = input("Deseja continuar? S ou N: ")
            if res == 'N':
                break
        print(f"{num} x {i} = {num * i}")
        i += 1
else:
    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))
    
    if operacao == "+":
        res = num1 + num2
    elif operacao == "-":
        res = num1 - num2
    elif operacao == "*":
        res = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            res = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida!")
            res = None

    if res is not None:
        print(f"{num1} {operacao} {num2} = {res}")