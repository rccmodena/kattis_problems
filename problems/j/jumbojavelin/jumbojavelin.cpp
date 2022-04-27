/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, l, length;

    cin >> n;

    length = 0;
    for (int i=0; i<n; i++) {
        cin >> l;
        length += l;
    }

    length -= n - 1;

    cout << length << endl;
}