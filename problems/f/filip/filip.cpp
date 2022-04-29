/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int reverse_number(int num)
{
    int result = 0;

    while (num > 0) {
        result = (result * 10) + (num % 10);
        num = num / 10;
    }
    return result;
}

int main() {
    int a, b;

    cin >> a;
    cin >> b;

    a = reverse_number(a);
    b = reverse_number(b);

    if (a > b) {
        cout << a << endl;
    }
    else {
        cout << b << endl;
    }
}