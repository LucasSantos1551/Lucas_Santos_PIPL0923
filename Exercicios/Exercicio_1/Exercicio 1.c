#include <stdio.h>

int main() {
    int segundos;
    int horas, minutos, segundos_restantes;

    printf("Digite o número de segundos: ");
    scanf("%d", &segundos);

    horas = segundos / 3600;
    minutos = (segundos % 3600) / 60;
    segundos_restantes = segundos % 60;

    printf("%d segundos equivalem a %d horas, %d minutos e %d segundos.\n", segundos, horas, minutos, segundos_restantes);

    return 0;
}
