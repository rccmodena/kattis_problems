/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;


string decimal_to_reversebinary(int decimal_number) {
    string binary_str;

    while(decimal_number != 0) {
        if (decimal_number % 2 == 0) {
            binary_str += "0";
        }
        else {
            binary_str += "1";
        }
        decimal_number /= 2;
    }
    return binary_str;
}


int binary_to_decimal(string binary_str) {
    int decimal_number, binary_size;

    binary_size = binary_str.size() - 1;
    decimal_number = 0;
    for (int i = binary_size; i >= 0; i--) {
        decimal_number +=  (binary_str[i] - 48) * pow(2, binary_size - i);
    }

    return decimal_number;
}


int main() {
    int n;
    string reversebinary;

    cin >> n;

    reversebinary = decimal_to_reversebinary(n);
    cout << binary_to_decimal(reversebinary) << endl;
}