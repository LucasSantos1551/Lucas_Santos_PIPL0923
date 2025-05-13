#include <stdio.h>

int main() {
    char nome[100];
    float valorCompra=0, desconto=0, valorTotal=0;

    printf("Digite o nome do cliente: ");
    fgets(nome, sizeof(nome), stdin);

    printf("Digite o valor da compra: ");
    scanf("%f", &valorCompra);

    if (valorCompra <= 200.00) {
        desconto = 0.10;
    } else if (valorCompra > 200.00 && valorCompra <= 500.00) {
        desconto = 0.15;
    } else {
        desconto = 0.20;
    }
    float valorDesconto = valorCompra * desconto;
    valorTotal = valorCompra - valorDesconto;

    printf("\nNome do cliente: %s", nome);
    printf("Valor da compra: %.2f€\n", valorCompra);
    printf("Percentual de desconto: %.0f%%\n", desconto * 100);
    printf("Valor do desconto: %.2f€\n", valorDesconto);
    printf("Valor total a pagar: %.2f€\n", valorTotal);

    return 0;
}
