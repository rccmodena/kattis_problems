/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int p, n, end_day;

    cin >> p >> n;

    end_day = 0;
    set<string, greater<string> > list_boat_parts;
    for (int i=0; i<n; i++) {
        string boat_part;
        cin >> boat_part;
        list_boat_parts.insert(boat_part);

        if (p == (int)list_boat_parts.size()) {
            end_day = i + 1;
            break;
        }
    }

    if (end_day == 0) {
        cout << "paradox avoided" << endl;
    }
    else {
        cout << end_day << endl;
    }
}