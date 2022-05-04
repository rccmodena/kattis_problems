/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

#define STRING_SIZE 51

void get_line(char string[], int size) {
    fgets(string, size, stdin);

    if ((strlen(string) > 0) && (string[strlen(string) - 1] == '\n'))
        string[strlen(string) - 1] = '\0';

}


int main(void) {
    int ball = 1;
    char moves[STRING_SIZE];

    get_line(moves, STRING_SIZE);

    for (int i = 0; moves[i] != '\0'; i++) {
        if (moves[i] == 'A') {
            if (ball == 1) {
                ball = 2;
            }
            else if (ball == 2) {
                ball = 1;
            }
        }
        else if (moves[i] == 'B') {
            if (ball == 2) {
                ball = 3;
            }
            else if (ball == 3) {
                ball = 2;
            }
        }
        else {
            if (ball == 3) {
                ball = 1;
            }
            else if (ball == 1) {
                ball = 3;
            }
        }

    }
    printf("%d\n", ball);

    return 0;
}