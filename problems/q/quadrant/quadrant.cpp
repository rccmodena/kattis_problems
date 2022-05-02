/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int x, y;

    cin >> x;
    cin >> y;


    if (x > 0) {
        if (y > 0) {
            printf("%d", 1);
        }
        else {
            printf("%d", 4);
        }
    }
    else{
        if (y > 0) {
            printf("%d", 2);
        }
        else {
            printf("%d", 3);
        }
    }

    return 0;

}