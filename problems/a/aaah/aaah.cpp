/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    string marius_ah;
    string doctor_ah;

    cin >> marius_ah;
    cin >> doctor_ah;

    if (marius_ah.size() >= doctor_ah.size()) {
        cout << "go" << endl;
    }
    else {
        cout << "no" << endl;
    }
}