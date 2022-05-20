/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int a, b, c, d, e, score;

    if (scanf("%d %d %d %d %d\n", &a, &b, &c, &d, &e) != 5) {
        printf("Failed to read thresholds!");
    }

    cin >> score;

    if (score >= a) {
        cout << "A";
    }
    else if (score >= b) {
        cout << "B";
    }
    else if (score >= c) {
        cout << "C";
    }
    else if (score >= d) {
        cout << "D";
    }
    else if (score >= e) {
        cout << "E";
    }
    else {
        cout << "F";
    }
}