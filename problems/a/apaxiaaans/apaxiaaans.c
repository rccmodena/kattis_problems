/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

#define NAME_SIZE 251

int main(void) {
    char name[NAME_SIZE];

    if (scanf("%s", name) != 1) {
        printf("Failed to read name!");
    }

    for (int i=0; name[i] != '\0'; i++) {
        if (i == 0) {
            printf("%c", name[i]);
        }
        else {
            if (name[i - 1] != name[i]) {
                printf("%c", name[i]);
            }
        }
    }

    printf("\n");

    return 0;
}