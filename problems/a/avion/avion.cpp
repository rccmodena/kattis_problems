/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

#define REGISTRATIONS 5

using namespace std;

int main() {
    int regitration_size, found_fbi;
    string registration;

    found_fbi = 0;
    for (int i=0; i<REGISTRATIONS; i++) {
        cin >> registration;

        regitration_size = registration.length() - 3;

        for (int j=0; j<=regitration_size; j++) {
            if (registration[j] == 'F' && registration[j + 1] == 'B' && registration[j + 2] == 'I') {
                found_fbi = 1;
                cout << i + 1 << " ";
                break;
            }
        }
    }

    if (found_fbi == 0) {
        cout << "HE GOT AWAY!" << endl;
    }
   
}