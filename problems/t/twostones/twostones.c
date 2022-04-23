/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int input_number;
    while (scanf("%d", &input_number) == 1)
        if (input_number % 2 == 0){
            printf("Bob");
        }
        else {
            printf("Alice");
        }
    return 0;
}