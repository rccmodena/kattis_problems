/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 1001

int main(void) {
    int n, val, negative_t;
    char t[MAX_SIZE];
    char *val_str;

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    if (fgets(t, MAX_SIZE, stdin) == NULL) {
        printf("Failed to read t!");
    }

    if ((strlen(t) > 0) && (t[strlen(t) - 1] == '\n')) {
        t[strlen(t) - 1] = '\0';
    }

    val_str = strtok(t, " ");

    negative_t = 0;
    while (val_str != NULL) {
        val = atoi(val_str);
        if (val < 0) {
            negative_t += 1;
        }
        val_str = strtok(NULL, " ");
    }

    printf("%d", negative_t);

    return 0;
}