/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int input_number;

    cin >> input_number;

    if (input_number % 2 == 0) {
        cout << "Bob" << endl;
    }
    else {
        cout << "Alice" << endl;
    }
}