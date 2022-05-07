/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

#define COMMAND_SIZE 101
#define AFTER_SIMON_SAYS 11

void get_line(char string[], int size) {
    string = fgets(string, size, stdin);

    if ((strlen(string) > 0) && (string[strlen(string) - 1] == '\n'))
        string[strlen(string) - 1] = '\0';
}

int main(void) {
    int n;
    char command[COMMAND_SIZE];
    char simon[] = "Simon says";

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        get_line(command, COMMAND_SIZE);

        int simon_says = 0;
        for (int j=0; simon[j] != '\0'; j++) {
            if (command[j] == simon[j]) {
                simon_says = 1;
            }
            else {
                simon_says = 0;
                break;
            }
        }

        if (simon_says == 1) {
            for (int j=AFTER_SIMON_SAYS; command[j] != '\0'; j++) {
                printf("%c", command[j]);
            }
            printf("\n");
        }
    }

    return 0;
}