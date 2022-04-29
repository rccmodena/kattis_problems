/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int a; 
    double option_one, option_two;
    if (scanf("%d", &a) != 1) {
        printf("Failed to read a!");
    }

    option_one = a / 100.0;
    option_two = (100 - a) / 100.0;

    if (option_one == 0){
        printf("%.10lf\n", option_one);
    }
    else {
        printf("%.10lf\n", 1/option_one);
    }

    if (option_two == 0) {
        printf("%.10lf\n", option_two);
    }
    else {
        printf("%.10lf\n", 1/option_two);
    }

    return 0;
}