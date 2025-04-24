num = int(input("Escreve um numero para contar seus divisores: "))

contador = 0

divisor = 1

while divisor <= num:
    if num % divisor == 0:  
        contador += 1
    divisor += 1 

print(f"O numero {num} possui {contador} divisores.")
