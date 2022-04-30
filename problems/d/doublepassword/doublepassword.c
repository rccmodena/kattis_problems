/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

#define PASSWORD_SIZE 4

int main(void) {
    char s1[PASSWORD_SIZE], s2[PASSWORD_SIZE];
    int sequences = 1;

    if (scanf("%s", s1) != 1) {
        printf("Failed to read s1!");
    }

    if (scanf("%s", s2) != 1) {
        printf("Failed to read s2!");
    }

    for (int i=0; i<PASSWORD_SIZE; i++) {
        if (s1[i] == s2[i]) {
            sequences *= 1;
        }
        else {
            sequences *= 2;
        }
    }
    printf("%d", sequences);

    return 0;
}