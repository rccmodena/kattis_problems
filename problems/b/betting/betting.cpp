/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int a;
    double option_one, option_two;

    cin >> a;

    option_one = a / 100.0;
    option_two = (100 - a) / 100.0;

    cout << fixed;
    cout << setprecision(10);

    if (option_one == 0){
        cout << option_one << endl;
    }
    else {
        cout << 1 / option_one << endl;
    }

    if (option_two == 0) {
        cout << option_two << endl;
    }
    else {
        cout << 1 / option_two << endl;
    }
}