/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, total;

    cin >> n;

    vector<int> books;

    for (int i=0; i<n; i++) {
        int book;
        cin >> book;
        books.push_back(book);
    }

    sort(books.begin(), books.end(), greater<int>());

    total = 0;
    for (int i=0; i<n; i++) {
        if (i % 3 != 2) {
            total += books[i];
        }
    }

    cout << total << endl;
}