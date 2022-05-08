/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, h, v, volume;

    if (scanf("%d %d %d\n", &n, &h, &v) != 3) {
        printf("Failed to read n, h and v!");
    }

    volume = 4;

    if (h > n - h) {
        volume *= h;
    }
    else {
        volume *= (n - h);
    }

    if (v > n - v)  {
        volume *= v;
    }
    else {
        volume *= (n - v);
    }

    printf("%d", volume);

    return 0;
}