limite = int(input("Digite o limite para procurar números perfeitos: "))

print("Números perfeitos encontrados:")
for num in range(2, limite + 1):
    soma_div = 0
    for i in range(1, num):
        if num % i == 0:
            soma_div += i
    if soma_div == num:
        print(num)
