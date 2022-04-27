/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    int day;
    string month;

    cin >> month >> day;

    if ((month == "OCT" && day == 31) || (month == "DEC" && day == 25)) {
        cout << "yup" << endl;
    }
    else {
        cout << "nope" << endl;
    }
}