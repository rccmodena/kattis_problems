/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

#define ESTIMATE_SIZE 102


void get_line(char string[], int size) {
    string = fgets(string, size, stdin);

    if ((strlen(string) > 0) && (string[strlen(string) - 1] == '\n'))
        string[strlen(string) - 1] = '\0';
}


int main(void) {
    int n, total;
    char estimate[ESTIMATE_SIZE];

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        get_line(estimate, ESTIMATE_SIZE);

        total = strlen(estimate);
        printf("%d\n", total);
    }

    return 0;
}