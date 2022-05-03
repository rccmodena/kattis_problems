/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>

using namespace std;


int count_digits(int value) {
    int sum = 0;
    int number = value;
    int power = 0;

    while (number > pow(10, power)) {
        power++;
    }

    while (power >= 0) {
        int digit = number / pow(10, power);
        sum += digit;
        if (digit != 0) {
            number -= digit * pow(10, power);
        }
        power--;
    }
    return sum;
}

int main() {
    int l, d, x;
    int n, m;

    cin >> l;
    cin >> d;
    cin >> x;

    n = 0;
    for (int val=l; val<d+1; val++) {
        if (x == count_digits(val)) {
            n = val;
            break;
        }
    }

    m = 0;
    for (int val=l; val<d+1; val++) {
        if (x == count_digits(val)) {
            m = val;
        }
    }

    cout << n << endl;
    cout << m << endl;
}