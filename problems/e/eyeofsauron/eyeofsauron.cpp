/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string n;
    size_t n_length, counter;
    bool correct;

    cin >> n;
    n_length = n.length();

    correct = true;
    if (n_length % 2 == 1) {
        correct = 0;
    }
    else {
        counter = n_length - 1;
        for (size_t i=0; i<counter; i++) {
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
        cout << "correct" << endl;
    }
    else {
        cout << "fix" << endl;
    }
}