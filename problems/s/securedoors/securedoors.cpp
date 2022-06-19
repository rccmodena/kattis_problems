/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;

    cin >> n;
    cin.ignore();

    set<string> log;
    for (int i=0; i<n; i++) {
        string command, name;

        cin >> command >> name;
        cin.ignore();

        if (command == "entry") {
            if (log.find(name) != log.end()) {
                cout << name << " entered (ANOMALY)" << endl;
            }
            else {
                log.insert(name);
                cout << name << " entered" << endl;
            }
        }
        else {
            if (log.find(name) == log.end()) {
                cout << name << " exited (ANOMALY)" << endl;
            }
            else {
                log.erase(name);
                cout << name << " exited" << endl;
            }
        }
    }
}