/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;


int count_vowels(string sentence) {
    string vowels = "aeiouAEIOU";
    int n_vowels = 0;

    for (size_t i = 0; i < sentence.length(); i++) {
        for (size_t j = 0; j < vowels.length(); j++ ) {
            if (sentence[i] == vowels[j]) {
                n_vowels++;
                break;
            }
        }
    }
    return n_vowels;
}


int main() {
    string s;

    getline(cin, s);

    cout << count_vowels(s) << endl;
}