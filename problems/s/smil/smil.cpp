/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    int eyes, position;
    string memory;

    getline(cin, memory);

    position = 0;
    eyes = 0;
    for (int i = 0; memory[i] != '\0'; i++) {
        if (memory[i] == ':' || memory[i] == ';') {
            position = i;
            eyes = 1;
        }
        else {
            if (eyes == 1) {
                if (memory[i] == ')') {
                    cout << position << endl;
                    eyes = 0;
                }
                else if (memory[i] != '-') {
                    eyes = 0;
                }
            }
        }
    }


 
}