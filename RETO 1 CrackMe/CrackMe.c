#include <stdio.h>
#include <string.h>

int main() {
    char password[20];

    printf("Introduce la clave: ");
    scanf("%19s", password);

    if (strcmp(password, "cyber123") == 0) {
        printf("Flag encontrada: flag{cyber123}\n");
    } else {
        printf("Clave incorrecta. Intenta de nuevo.\n");
    }

    return 0;
}

