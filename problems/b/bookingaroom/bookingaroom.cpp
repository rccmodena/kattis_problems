/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int r, n, found_room;

    cin >> r >> n;

    int reserved_rooms[n];

    for (int i=0; i<n; i++) {
        cin >> reserved_rooms[i];
    }

    if (r == n) {
        cout << "too late" << endl;
    }
    else {
        for (int i=1; i<=r; i++){
            found_room = 1;
            for (int j=0; j<n; j++){
                if (i == reserved_rooms[j]){
                    found_room = 0;
                    break;
                }
            }
            if (found_room == 1) {
                cout << i << endl;
                break;
            }
        }
    }
}