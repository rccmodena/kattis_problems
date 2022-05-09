/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

double to_radians(double degrees) {
    return (degrees * M_PI ) / 180.0;
}

int main(void) {
    int h, v, ladder;

    if (scanf("%d %d", &h, &v) != 2) {
        printf("Failed to read h and v!");
    }

    ladder = ceil(h / sin(to_radians(v)));

    printf("%d", ladder);

    return 0;
}