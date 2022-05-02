/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STRING_SIZE 101

int main(void) {
    char word[STRING_SIZE];
    int n;
    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        if (fgets(word, STRING_SIZE, stdin) == NULL) {
            printf("Failed to read at_bats!");
        }

        if (i % 2 == 0) {
            printf("%s", word);
        }
    }

    return 0;
}