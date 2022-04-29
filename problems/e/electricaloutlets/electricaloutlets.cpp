/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, k, o, total_strips;

    cin >> n;


    for (int i=0; i<n; i++) {
        total_strips = 0;        
        cin >> k;
        total_strips -= k - 1;
        
        for (int j=0; j<k; j++) {
            cin >> o;
            total_strips += o;
        }
        
        cout << total_strips << endl;
    }
}