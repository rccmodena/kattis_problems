/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n;
    string estimate;

    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> estimate;
        cout << estimate.length() << endl;
    }
}