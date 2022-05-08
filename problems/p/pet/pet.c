/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

#define CONTESTANTS_SIZE 5


int main(void) {
    int grade_1, grade_2, grade_3, grade_4, winner_id, winner_points, points;
    winner_id = 0;
    winner_points = 0;
    for (int i=0; i<CONTESTANTS_SIZE; i++) {
        if (scanf("%d %d %d %d\n", &grade_1, &grade_2, &grade_3, &grade_4) != 4) {
            printf("Failed to read grades!");
        }

        points = grade_1 + grade_2 + grade_3 + grade_4;

        if (winner_points < points) {
            winner_id = i + 1;
            winner_points = points;
        }
    }

    printf("%d %d", winner_id, winner_points);

    return 0;
}