/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STRING_SIZE 81


int count_vowels(char *sentence) {
    char *vowels = "aeiouAEIOU";
    int n_vowels = 0;

    for (int i = 0; sentence[i] != '\0'; i++) {
        for (int j = 0; vowels[j] !='\0'; j++ ) {
            if (sentence[i] == vowels[j]) {
                n_vowels++;
                break;
            }
        }
    }
    return n_vowels;
}


int main(void) {
    char s[STRING_SIZE];

    fgets(s, STRING_SIZE, stdin);

    if ((strlen(s) > 0) && (s[strlen(s) - 1] == '\n'))
        s[strlen(s) - 1] = '\0';

    printf("%d", count_vowels(s));

    return 0;
}