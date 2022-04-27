/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

int main(void) {
    char phrase[31];
    if (scanf("%s", phrase) != 1) {
        printf("Failed to read phrase!");
    }

    if (strstr(phrase, "ss") != NULL) {
        printf("hiss");
    }
    else {
        printf("no hiss");
    }

    return 0;
}