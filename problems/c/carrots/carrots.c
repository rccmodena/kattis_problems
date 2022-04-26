/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, p;
    char contestant[30];

    if (scanf("%d%d", &n, &p) != 2) {
        printf("Failed to read n and p!");
    }

    for (int i=0; i<n; i++) {
        if (scanf("%s", contestant) != 1) {
            printf("Failed to read contestant!");
        }
    }
    
    printf("%d", p);

    return 0;
}