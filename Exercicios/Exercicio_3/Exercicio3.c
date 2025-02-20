#include <stdio.h>

int main() {
    int num1, num2;

    // Lê os dois números
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);
    printf("Digite o segundo número: ");
    scanf("%d", &num2);

    // Exibe em ordem crescente
    printf("Ordem crescente: ");
    if (num1 < num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }

    // Exibe em ordem decrescente
    printf("Ordem decrescente: ");
    if (num1 > num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }

    return 0;
}