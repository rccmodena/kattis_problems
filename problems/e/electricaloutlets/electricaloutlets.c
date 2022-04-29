/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 35

int main(void) {
    int n, k, total_strips;
    char list_strips[MAX_SIZE];
    char *val_str;

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        if (fgets(list_strips, MAX_SIZE, stdin) == NULL) {
            printf("Failed to read list_strips!");
        }

        if ((strlen(list_strips) > 0) && (list_strips[strlen (list_strips) - 1] == '\n')) {
            list_strips[strlen (list_strips) - 1] = '\0';
        }

        val_str = strtok(list_strips, " ");

        total_strips = 0;
        k = 1;
        while (val_str != NULL) {
            if (k == 1) {
                total_strips -= atoi(val_str) - 1;
                k = 0;
            }
            else {
                total_strips += atoi(val_str);
            }
            val_str = strtok(NULL, " ");
        } 

        printf("%d\n", total_strips);
    }

    return 0;
}