#include <stdio.h>

// Este programa no hace nada visible, pero contiene la flag en texto plano
int main() {
    // Flag oculta en binario para ser encontrada con OllyDbg
    char *flag = "flag{crackme_virtual_challenge}";
    return 0;
}
