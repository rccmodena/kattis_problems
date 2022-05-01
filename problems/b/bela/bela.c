/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, hands, points;
    char b, card_n, card_b;
    if (scanf("%d %c\n", &n, &b) != 2) {
        printf("Failed to read a!");
    }

    hands = n * 4;
    points = 0;

    for (int i=0; i<hands; i++) {
        if (scanf("%c%c\n", &card_n, &card_b) != 2) {
            printf("Failed to read card_n and card_b!");
        }
        if (card_b == b) {
            switch (card_n) {
                case 'A':
                    points += 11;
                    break;
                case 'K':
                    points += 4;
                    break;
                case 'Q':
                    points += 3;
                    break;
                case 'J':
                    points += 20;
                    break;
                case 'T':
                    points += 10;
                    break;
                case '9':
                    points += 14;
                    break;
                case '8':
                    points += 0;
                    break;
                case '7':
                    points += 0;
                    break;
            }
        }
        else {
            switch (card_n) {
                case 'A':
                    points += 11;
                    break;
                case 'K':
                    points += 4;
                    break;
                case 'Q':
                    points += 3;
                    break;
                case 'J':
                    points += 2;
                    break;
                case 'T':
                    points += 10;
                    break;
                case '9':
                    points += 0;
                    break;
                case '8':
                    points += 0;
                    break;
                case '7':
                    points += 0;
                    break;
            }
        }
    }

    printf("%d", points);

    return 0;
}