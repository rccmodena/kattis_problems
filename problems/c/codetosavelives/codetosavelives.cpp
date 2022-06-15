/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;

    cin >> t;
    cin.ignore();

    for (int i=0; i<t; i++) {
        int number_1, number_2;
        string number_str;
        
        getline(cin, number_str);
        number_str.erase(remove(number_str.begin(), number_str.end(), ' '), number_str.end());
        number_1 = stoi(number_str);

        getline(cin, number_str);
        number_str.erase(remove(number_str.begin(), number_str.end(), ' '), number_str.end());
        number_2 = stoi(number_str);        

        string str_total = to_string(number_1 + number_2);
        for (size_t i=0; i<str_total.size(); i++) {
            cout << str_total[i];

            if (i < str_total.size() - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }
}