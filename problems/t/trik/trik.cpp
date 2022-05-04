/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int ball = 1;
    string moves;

    getline(cin, moves);

    for (size_t i = 0; i < moves.length(); i++) {
        if (moves[i] == 'A') {
            if (ball == 1) {
                ball = 2;
            }
            else if (ball == 2) {
                ball = 1;
            }
        }
        else if (moves[i] == 'B') {
            if (ball == 2) {
                ball = 3;
            }
            else if (ball == 3) {
                ball = 2;
            }
        }
        else {
            if (ball == 3) {
                ball = 1;
            }
            else if (ball == 1) {
                ball = 3;
            }
        }

    }

    cout << ball << endl;
}