/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

#define STRING_SIZE 51

void get_line(char string[], int size) {
    string = fgets(string, size, stdin);

    if ((strlen(string) > 0) && (string[strlen(string) - 1] == '\n'))
        string[strlen(string) - 1] = '\0';
}

int main(void) {
    char s[STRING_SIZE];

    get_line(s, STRING_SIZE);

    printf("Thank you, %s, and farewell!", s);

    return 0;
}