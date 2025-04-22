#include <stdio.h>

int main() {
    float nota1, nota2, nota3, media;

    printf("Digite a nota da primeira prova (0 a 10): ");
    scanf("%f", &nota1);
    printf("Digite a nota da segunda prova (0 a 10): ");
    scanf("%f", &nota2);
    printf("Digite a nota da terceira prova (0 a 10): ");
    scanf("%f", &nota3);

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

    printf("Média final: %.2f\n", media);
    if (media >= 6.0) {
        printf("RESULTADO: APROVADO\n");
    } else {
        printf("RESULTADO: REPROVADO\n");
    }

    return 0;
}
