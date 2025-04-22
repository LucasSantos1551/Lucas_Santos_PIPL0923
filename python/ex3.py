soma = 0
 
for i in range(10):
    nota=int(input(f"introduza {i + 1} notas de 10 alunos "))
    soma += nota
 
media = soma / 10
print("a media das notas é", media)