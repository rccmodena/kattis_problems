/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 301

int main(void) {
    char at_bats[MAX_SIZE];
    int n, at_bat;
    double slugging_sum, slugging_percentage;
    char *val_str;

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read a!");
    }

    if (fgets(at_bats, MAX_SIZE, stdin) == NULL) {
        printf("Failed to read at_bats!");
    }

    if ((strlen(at_bats) > 0) && (at_bats[strlen(at_bats) - 1] == '\n')) {
        at_bats[strlen(at_bats) - 1] = '\0';
    }

    val_str = strtok(at_bats, " ");

    slugging_sum = 0;
    while (val_str != NULL) {
        at_bat = atoi(val_str);
        if (at_bat == -1) {
            n += at_bat;
        }
        else {
            slugging_sum += at_bat;
        }
        val_str = strtok(NULL, " ");
    } 

    slugging_percentage = slugging_sum / (double)n;

    printf("%.17lf", slugging_percentage);

    return 0;
}