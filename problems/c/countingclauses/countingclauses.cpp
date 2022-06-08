/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int m, n;
    int clause;

    cin >> m >> n;

    for (int i=0; i<m; i++) {
        cin >> clause;
    }

    if (m>=8) {
        cout << "satisfactory" << endl;
    }
    else {
        cout << "unsatisfactory" << endl;
    }
}