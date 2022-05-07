/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <limits.h>
#include <math.h>

#define CARDS_SIZE 51
#define CARDS_TYPES 3

int main(void) {
    char cards[CARDS_SIZE];
    int min_all_cards, total;
    int count_cards[CARDS_TYPES] = {0};

    if (scanf("%s", cards) != 1) {
        printf("Failed to read cards!");
    }

    for (int i=0; cards[i] != '\0'; i++) {
        switch (cards[i])
        {
        case 'T':
            count_cards[0]++;
            break;

        case 'G':
            count_cards[1]++;
            break;

        case 'C':
            count_cards[2]++;
            break;
        }
    }

    total = 0;
    min_all_cards = INT_MAX;
    for (int i=0; i<CARDS_TYPES; i++) {
        if (count_cards[i] < min_all_cards) {
            min_all_cards = count_cards[i];
        }
        total += count_cards[i] * count_cards[i];
    }

    total += 7 * min_all_cards;

    printf("%d", total);

    return 0;
}