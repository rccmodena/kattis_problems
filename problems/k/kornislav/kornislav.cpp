/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

#define NUMBER_INTEGERS 4

int main() {
    int list_integers[NUMBER_INTEGERS];

    for (int i=0; i<NUMBER_INTEGERS; i++) {
        cin >> list_integers[i];
    }

    sort(list_integers, list_integers + NUMBER_INTEGERS);

    // To create a rectangle, use the two larger number as parallel sides and the two smaller to be the other sides.
    // The area of the biggest rectangle should be the smallest side x the smallest of the bigger sides.
    cout << list_integers[0] * list_integers[2] << endl;
}