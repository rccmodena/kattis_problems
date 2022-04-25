/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        printf("Failed to read a!");
    }

    for (int i=1; i<=n; i++) {
        printf("%d Abracadabra\n", i);
    }

    return 0;
}