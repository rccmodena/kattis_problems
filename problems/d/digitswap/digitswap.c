/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#define PASSWORD_SIZE 2

int main(void) {
    char a[PASSWORD_SIZE];
    if (scanf("%s", a) != 1) {
        printf("Failed to read a!");
    }

    for (int i=PASSWORD_SIZE-1; i>-1; i--) {
        printf("%c", a[i]);
    }

    return 0;
}