/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

// Repeat three times the word separated by a single space.
void get_echo(char *word, char *echo_word) {

    int echo_position = 0;
    for (int i=0; i < 3; i++) {
        int word_position = 0;
        while (word[word_position] != '\0') {
            echo_word[echo_position] = word[word_position];
            word_position++;
            echo_position++;
        }
        echo_word[echo_position] = ' ';
        echo_position++;
    }
    echo_word[echo_position] = '\0';
}

int main(void) {
    const int MAX_LENGHT_WORD = 16;
    const int MAX_LENGHT_ECHO = MAX_LENGHT_WORD * 3 + 3;

    char word[MAX_LENGHT_WORD];
    char echo_word[MAX_LENGHT_ECHO];

    if (scanf("%s", word) != 1) {
        printf("Failed to read word!");
    }

    get_echo(word, echo_word);

    printf("%s", echo_word);

    return 0;
}