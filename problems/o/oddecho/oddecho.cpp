/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string word;

    getline(cin, word);
    n = stoi(word);

    for (int i=0; i<n; i++) {
        getline(cin, word);

        if (i % 2 == 0) {
            cout << word << endl;
        }
    }
}