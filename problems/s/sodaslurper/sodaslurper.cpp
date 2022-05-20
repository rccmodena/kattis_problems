/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int e, f, c, remaining_bottles, soda_drinked, soda_bought;

    cin >> e >> f >> c;

    remaining_bottles = e + f;
    soda_drinked = 0;
    while (remaining_bottles >= c) {
        soda_bought = remaining_bottles / c;
        soda_drinked += soda_bought;
        remaining_bottles = (remaining_bottles % c) + soda_bought;
    }

    cout << soda_drinked << endl;
}