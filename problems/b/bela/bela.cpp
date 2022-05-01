/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, hands, points;
    char b, card_n, card_b;

    cin >> n;
    cin >> b;

    hands = n * 4;
    points = 0;

    for (int i=0; i<hands; i++) {
        cin >> card_n;
        cin >> card_b;
        
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
                if (card_b == b) {
                    points += 20;
                }
                else {
                    points += 2;
                }
                break;
            case 'T':
                points += 10;
                break;
            case '9':
                if (card_b == b) {
                    points += 14;
                }
                else {
                    points += 0;
                }
                break;
            case '8':
                points += 0;
                break;
            case '7':
                points += 0;
                break;
        }
    }

    cout << points << endl;
}