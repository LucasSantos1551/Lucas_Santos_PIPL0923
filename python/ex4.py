numero = int(input("Escreve um numero inteiro: "))
i = 2
primo = True  

while i < numero:
    if numero % i == 0:
        primo = False 
        break  
    i += 1


if numero < 2:
    print(f"{numero} não é um numero primo.")
elif primo:
    print(f"{numero} é um numero primo.")
else:
    print(f"{numero} não é um numero primo.")
