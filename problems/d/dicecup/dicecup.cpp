/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;

    cin >> n >> m;

    vector<int> results;
    for (int i=1; i< n + m + 2; i++) {
        results.push_back(0);
    }

    for (int i=1; i<n+1; i++) {
        for (int j=1; j<m+1; j++) {
            int total = i + j;
            results[total]++;
        }
    }

    int max_outcome = *max_element(begin(results), end(results));
    for (size_t i=0; i<results.size(); i++) {
        if (results[i] == max_outcome){
            cout << i << endl;
        }
    }
}