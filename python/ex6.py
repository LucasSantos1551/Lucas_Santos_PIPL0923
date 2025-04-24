def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primos = []

num = 2

while len(primos) < 10:
    if primo(num):
        primos.append(num)
    num += 1
print(primos)
