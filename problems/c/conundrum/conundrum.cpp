/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    string cipher;
    string name = "PER";
    int number_days = 0;

    cin >> cipher;

    for (size_t i=0; i<cipher.size(); i++) {
        if (name[i % 3] != cipher[i]) {
            number_days++;
        }
    }

    cout << number_days << endl;
}