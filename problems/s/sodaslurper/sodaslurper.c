/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int e, f, c, remaining_bottles, soda_drinked, soda_bought;
    
    if (scanf("%d %d %d\n", &e, &f, &c) != 3) {
        printf("Failed to read e, f and c!");
    }
            
    remaining_bottles = e + f;
    soda_drinked = 0;
    while (remaining_bottles >= c) {
        soda_bought = remaining_bottles / c;
        soda_drinked += soda_bought;
        remaining_bottles = (remaining_bottles % c) + soda_bought;
    }

    printf("%d", soda_drinked);

    return 0;
}