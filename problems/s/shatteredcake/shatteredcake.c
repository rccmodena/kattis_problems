/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int w, n, wi, li, area;

    if (scanf("%d\n", &w) != 1) {
        printf("Failed to read w!");
    }

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    area = 0;
    for (int i=0; i<n; i++) {
        if (scanf("%d %d\n", &wi, &li) != 2) {
            printf("Failed to read wi and li!");
        }
        area +=  wi * li;
    }

    printf("%d", area/w);

    return 0;
}