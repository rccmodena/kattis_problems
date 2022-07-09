/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int s;

    cin >> s;

    cout << s << ":" << endl;

    for (int first_line=2; first_line<=(s/2+1); first_line++) {
        for (int second_line=first_line-1; second_line<=first_line; second_line++) {
            int two_lines = first_line + second_line; 
            if (s % two_lines == 0 or s % two_lines == first_line) {
                cout << first_line << "," << second_line << endl;
            }
        }
    }
}