/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

#define MEMORY_SIZE 2049

int main(void) {
    int eyes, position;
    char memory[MEMORY_SIZE];

    fgets(memory, MEMORY_SIZE, stdin);

    if ((strlen(memory) > 0) && (memory[strlen(memory) - 1] == '\n'))
        memory[strlen(memory) - 1] = '\0';

    position = 0;
    eyes = 0;
    for (int i = 0; memory[i] != '\0'; i++) {
        if (memory[i] == ':' || memory[i] == ';') {
            position = i;
            eyes = 1;
        }
        else {
            if (eyes == 1) {
                if (memory[i] == ')') {
                    printf("%d\n", position);
                    eyes = 0;
                }
                else if (memory[i] != '-') {
                    eyes = 0;
                }
            }
        }
    }

    return 0;
}