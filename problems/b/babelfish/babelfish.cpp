/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    map<string, string> dictionary;

    string line;
    do {
        getline(cin, line);

        stringstream ss(line);
        string english, foreign_language;
        ss >> english >> foreign_language;

        dictionary[foreign_language] = english;
    } while (line.size() != 0);

    string word;
    while (cin >> word) {
        if (dictionary.find(word) == dictionary.end()) {
            cout << "eh" << endl;
        }
        else {
            cout << dictionary[word] << endl;
        }
    }
}