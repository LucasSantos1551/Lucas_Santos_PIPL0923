#include <stdio.h>

int main() {
    int Num1=0, Num2=0, Num3=0;
    int temp=0;


    printf("Digite o primeiro valor: ");
    scanf("%d", &Num1);
    printf("Digite o segundo valor: ");
    scanf("%d", &Num2);
    printf("Digite o terceiro valor: ");
    scanf("%d", &Num3);

    if (Num1 > Num2) {
        temp = Num1;
        Num1 = Num2;
        Num2 = temp;
    }
    if (Num1 > Num3) {
        temp = Num1;
        Num1 = Num3;
        Num3 = temp;
    }
    if (Num2 > Num3) {
        temp = Num2;
        Num2 = Num3;
        Num3 = temp;
    }

    printf("Ordem crescente: %d, %d, %d\n", Num1, Num2, Num3);

    printf("Ordem decrescente: %d, %d, %d\n", Num3, Num2, Num1);

    return 0;
}
