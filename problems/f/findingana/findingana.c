/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    char s[1001];
    int first_a = 0;

    if (scanf("%s", s) != 1) {
        printf("Failed to read s!");
    }

    for (int i=0; s[i] != '\0'; i++) {
        if (s[i] == 'a' && first_a == 0) {
            first_a = 1;
        }
        if (first_a == 1){
            printf("%c", s[i]);
        }
    }

    return 0;
}