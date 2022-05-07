/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

#define COMMAND_SIZE 101

void get_line(char string[], int size) {
    string = fgets(string, size, stdin);

    if ((strlen(string) > 0) && (string[strlen(string) - 1] == '\n'))
        string[strlen(string) - 1] = '\0';
}

int main(void) {
    int a;
    char command[COMMAND_SIZE];
    if (scanf("%d", &a) != 1) {
        printf("Failed to read a!");
    }
    get_line(command, COMMAND_SIZE);

    return 0;
}