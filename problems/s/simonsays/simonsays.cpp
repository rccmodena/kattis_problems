/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

#define AFTER_SIMON_SAYS 11

using namespace std;

int main() {
    int n;
    string command;
    string simon = "Simon says";

    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        getline(cin, command);

        int simon_says = 0;
        for (size_t j=0; j<simon.length(); j++) {
            if (command[j] == simon[j]) {
                simon_says = 1;
            }
            else {
                simon_says = 0;
                break;
            }
        }

        if (simon_says == 1) {
            for (size_t j=AFTER_SIMON_SAYS; j<command.length(); j++) {
                cout << command[j];
            }
            cout << endl;
        }
    }
}