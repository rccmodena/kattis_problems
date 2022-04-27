/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, r, e, c;

    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> r;
        cin >> e;
        cin >> c;
        
        if (r == (e - c)) {
            cout << "does not matter" << endl;
        }
        else if (r > (e - c)) {
            cout << "do not advertise" << endl;
        }
        else {
            cout << "advertise" << endl;
        }

    }

}