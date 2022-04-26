/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

int main(void) {
    int n, points;
    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    // Start with 2, and then add powers of 2
    points = 2;
    for (int power=0; power<n; power++){
        points += pow(2, power);
    }
    points = pow(points, 2);

    printf("%d", points);

    return 0;
}