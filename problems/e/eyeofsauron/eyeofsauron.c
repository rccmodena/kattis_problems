/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

int main(void) {
    char n[101];
    int length, counter, correct;
    
    if (scanf("%s", n) != 1) {
        printf("Failed to read n!");
    }

    length = strlen(n);

    correct = 1;
    if (length % 2 == 1) {
        correct = 0;
    }
    else {
        counter = length - 1;
        for (int i=0; i<counter; i++) {
            if (n[i] != n[counter]) {
                if (n[i] == '(' && n[counter] == ')') {
                    correct = 1;
                }
                else {
                    correct = 0;
                    break;
                }
            }
            counter -= 1;
        }
    }

    if (correct == 1) {
        printf("correct");
    }
    else {
        printf("fix");
    }

    return 0;
}