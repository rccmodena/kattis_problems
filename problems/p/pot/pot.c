/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Slice a string from the begin until the position, and return the integer version of the string
int str_position(char str[], int position)
{
    char result[strlen(str)];

    for (int i = 0; i <= position; i++) {
        result[i] = str[i];
    }
    result[position + 1] = '\0';
    return atoi(result);
}

// Get the index of the last char in a string
int get_last_index(char str[]) {
    int position = 0;

    while (str[position] != '\0') {
        position++;
    }

    return position - 1;
}

int main(void) {
    const int MAX_LENGHT = 4;
    int n = 0;
    int x = 0;
    int last_index = 0;
    int number = 0;
    int power = 0;

    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        char p[MAX_LENGHT];

        // Read number as string
        if (scanf("%s", p) != 1) {
            printf("Failed to read p!");
        }

        // Determine number and power
        last_index = get_last_index(p);
        number = str_position(p, last_index - 1);
        power = p[last_index] - '0';

        // Calculate result
        x += pow(number, power);
    }

    printf("%d", x);
    return 0;
}