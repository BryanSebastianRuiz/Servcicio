#include <stdio.h>
#include <string.h>

int main() {
    char entrada[50];
    char clave[] = "letmein123";

    printf("Introduce la contraseña: ");
    scanf("%49s", entrada);

    if (strcmp(entrada, clave) == 0) {
        printf("¡Acceso concedido! flag{crackme_virtual_challenge}\n");
    } else {
        printf("Contraseña incorrecta.\n");
    }
    return 0;
}
