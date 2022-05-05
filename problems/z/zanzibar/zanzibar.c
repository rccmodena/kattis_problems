/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int t, turtles, turtles_abroad, previous_turtles;
    if (scanf("%d", &t) != 1) {
        printf("Failed to read t!");
    }

    for (int i=0; i<t; i++) {
        if (scanf("%d ", &turtles) != 1) {
            printf("Failed to read turtles!");
        }
        turtles_abroad = 0;
        previous_turtles = 1;
        while (turtles != 0) {
            if (turtles > (previous_turtles * 2))
                turtles_abroad += turtles - (previous_turtles * 2);
            previous_turtles = turtles;

            if (scanf("%d ", &turtles) != 1) {
                printf("Failed to read turtles!");
            }
        }
        printf("%d\n", turtles_abroad);
    }

    return 0;
}
