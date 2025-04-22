#include <stdio.h>

int main() {
    int nums[10];
    for(int i = 0; i < 10; i++) {
        printf("Introduze o número nº%i: ", i);
        scanf("%i", &nums[i]);
    }
    int par = 0, impar = 0;
    for(int i = 0; i < 10; i++) {
        if(nums[i] % 2 == 0) {
            par++;
        } else {
            impar++;
        }
    }
    printf("Existem %i números pares e %i números impares\n", par, impar);
}