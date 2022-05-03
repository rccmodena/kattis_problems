/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int x, y;
    int x_points[3], y_points[3];
    int fourth_x, fourth_y;
    for (int row=0; row<3; row++) {
        if (scanf("%d %d", &x, &y) != 2) {
            printf("Failed to read a!");
        }
        x_points[row] = x;
        y_points[row] = y;
    }
    if (x_points[0] == x_points[1]) {
        fourth_x = x_points[2];
    }
    else if (x_points[0] == x_points[2]) {
        fourth_x = x_points[1];
    }
    else {
        fourth_x = x_points[0];
    }

    if (y_points[0] == y_points[1]) {
        fourth_y = y_points[2];
    }
    else if (y_points[0] == y_points[2]) {
        fourth_y = y_points[1];
    }
    else {
        fourth_y = y_points[0];
    }

    printf("%d %d\n", fourth_x, fourth_y);

    return 0;
}