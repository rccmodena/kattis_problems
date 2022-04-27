/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, l, length;
    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    length = 0;
    for (int i=0; i<n; i++) {
        if (scanf("%d", &l) != 1) {
            printf("Failed to read n!");
        }
        length += l;
    }

    length -= n - 1;

    printf("%d", length);

    return 0;
}