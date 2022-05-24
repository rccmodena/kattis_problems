/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

double calc_area_circle(int radius) {
    return M_PI * pow(radius, 2);
}


int main(void) {
    int r, c;
    double total_area, total_cheese, percent_cheese;

    if (scanf("%d %d\n", &r, &c) != 2) {
        printf("Failed to read r and c!");
    }
    
    total_area = calc_area_circle(r);
    total_cheese = calc_area_circle(r - c);
    percent_cheese = total_cheese / total_area * 100;

    printf("%lf", percent_cheese);

    return 0;
}