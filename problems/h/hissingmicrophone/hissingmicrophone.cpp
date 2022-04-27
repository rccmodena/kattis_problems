/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string phrase;

    cin >> phrase;

    if (phrase.find("ss") != string::npos) {
        std::cout << "hiss" << endl;
    }
    else {
        std::cout << "no hiss" << endl;
    }

}