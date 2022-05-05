/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>


double to_degrees(double radians) {
    return radians * (180.0 / M_PI);
}


double to_radians(double degrees) {
    return (degrees * M_PI ) / 180.0;
}


double get_t(double x1, double v0, double ang) {
    return x1 / (v0 * cos(to_radians(ang)));
}


double get_y1(double v0, double t, double ang){
    double g = 9.81;
    return v0 * t * sin(to_radians(ang)) - 0.5 * g * pow(t, 2);
}


int main(void) {
    int n;
    double v0, ang, x1, h1, h2, t, y1;

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        if (scanf("%lf %lf %lf %lf %lf", &v0, &ang, &x1, &h1, &h2) != 5) {
            printf("Failed to read values!");
        }

        t = get_t(x1, v0, ang);
        y1 = get_y1(v0, t, ang);

        if ((y1 >= (h1 + 1)) && (y1 <= (h2 - 1))) {
            printf("Safe\n");
        }
        else {
            printf("Not Safe\n");
        }
    }

    return 0;
}