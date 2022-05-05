/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int t, turtles, turtles_abroad, previous_turtles;

    cin >> t;

    for (int i=0; i<t; i++) {
        cin >> turtles;
        turtles_abroad = 0;
        previous_turtles = 1;
        while (turtles != 0) {
            if (turtles > (previous_turtles * 2))
                turtles_abroad += turtles - (previous_turtles * 2);
            previous_turtles = turtles;

            cin >> turtles;
        }
        cout << turtles_abroad << endl;
    }
}