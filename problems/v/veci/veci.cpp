/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string x_str;
    int x;
    vector<int> x_vector;

    cin >> x_str;
    x = stoi(x_str);

    for (size_t i=0; i<x_str.size(); i++) {
        x_vector.push_back(x_str[i] - 48);
    }

    int smallest = 0;
    sort(x_vector.begin(), x_vector.end());
    do {
        int value = 0;
        for (int digit : x_vector) {
            value = value * 10 + digit;
        }
        if (value > x) {
            if (smallest == 0 || value < smallest) {
                smallest = value;
            }
        }
    } while (next_permutation(x_vector.begin(), x_vector.end()));

    cout << smallest << endl;
}