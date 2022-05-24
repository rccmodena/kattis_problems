/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

double calc_euclidian_area(int radius) {
    return M_PI * pow(radius, 2);
}


double calc_taxicab_area(int radius) {
    return 2.0 * pow(radius, 2);
}


int main(void) {
    int r;

    if (scanf("%d", &r) != 1) {
        printf("Failed to read r!");
    }
    
    printf("%lf\n", calc_euclidian_area(r));
    printf("%lf\n", calc_taxicab_area(r));

    return 0;
}