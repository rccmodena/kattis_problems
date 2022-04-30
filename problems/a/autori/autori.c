/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int first_letter = 1;
    char long_naming[101];
    if (scanf("%s", long_naming) != 1) {
        printf("Failed to read long_naming!");
    }

    for (int i=0; long_naming[i]!='\0';i++) {
        if (first_letter == 1) {
            printf("%c", long_naming[i]);
            first_letter = 0;
        }
        else {
            if (long_naming[i] == '-') {
                first_letter = 1;
            }
        }
    }

    return 0;
}