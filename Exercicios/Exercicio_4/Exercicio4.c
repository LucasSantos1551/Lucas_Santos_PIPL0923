#include <stdio.h>

int main() {
    float saldo_inicial, cheque;

    // Lê o saldo inicial do cliente
    printf("Digite o saldo inicial do cliente: ");
    scanf("%f", &saldo_inicial);

    // Lê o valor do cheque
    printf("Digite o valor do cheque: ");
    scanf("%f", &cheque);

    // Verifica se o cheque pode ser descontado
    if (cheque > saldo_inicial) {
        printf("Cheque não pode ser descontado. Saldo insuficiente.\n");
    } else {
        // Desconta o cheque
        saldo_inicial -= cheque;
        printf("Cheque descontado com sucesso.\n");
        printf("Novo saldo: %.2f\n", saldo_inicial);
    }

    return 0;
}