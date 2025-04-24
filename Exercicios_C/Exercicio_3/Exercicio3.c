#include <stdio.h>

int main() {
    int num1=0, num2=0;
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);
    printf("Digite o segundo número: ");
    scanf("%d", &num2);


    printf("Ordem crescente: ");
    if (num1 < num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }
    printf("Ordem decrescente: ");
    if (num1 > num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }

    return 0;
}
