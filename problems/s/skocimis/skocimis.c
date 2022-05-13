/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

#define COMMAND_SIZE 101

int main(void) {
    int a, b, c, space_1, space_2;

    if (scanf("%d %d %d\n", &a, &b, &c) != 3) {
        printf("Failed to read a, b and c!");
    }
    
    space_1 = b - a;
    space_2 = c - b;

    if (space_1 > space_2) {
        printf("%d", space_1 - 1);
    }
    else {
        printf("%d", space_2 - 1);
    }

    return 0;
}