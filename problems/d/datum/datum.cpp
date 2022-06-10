/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int days_months[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    string days_week[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    int d, m, days;

    cin >> d >> m;

    // Start with 3, because the first day of 2009 was a Thursday
    days = 2;
    for (int i=0; i<m - 1; i++) {
        days += days_months[i];
    }

    days += d;

    cout << days_week[days % 7] << endl;
}