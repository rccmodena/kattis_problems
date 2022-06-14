/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;

    cin >> n;

    string input;
    vector<string> vector_names;

    for (int i=0; i<n; i++) {
        cin >> input;
        vector_names.push_back(input);
    }
    vector<string> increasing_vector = vector_names;
    vector<string> decreasing_vector = vector_names;

    sort(increasing_vector.begin(), increasing_vector.end());
    sort(decreasing_vector.begin(), decreasing_vector.end(), greater<string>());

    if (vector_names == increasing_vector) {
        cout << "INCREASING" << endl;
    }
    else if (vector_names == decreasing_vector) {
        cout << "DECREASING" << endl;
    }        
    else {
        cout << "NEITHER" << endl;
    }
 }
