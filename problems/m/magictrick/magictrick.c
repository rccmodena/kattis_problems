/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

#define CARDS_SIZE 51

int main(void) {
    int count_card;
    char s[CARDS_SIZE];
    if (scanf("%s", s) != 1) {
        printf("Failed to read s!");
    }

    for (int i=0; s[i] != '\0'; i++) {
        count_card = 0;
        for (int j=0; s[j] != '\0'; j++) {
            if (s[i] == s[j]) {
                count_card++;
            }
            if (count_card > 1) {
                break;
            }
        }
        if (count_card > 1) {
            break;
        }
    }

    if (count_card > 1) {
        printf("0");
    }
    else {
        printf("1");
    }


    return 0;
}