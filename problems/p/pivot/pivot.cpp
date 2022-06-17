/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> transformed_a;
    for (int i=0; i<n; i++) {
        int value;
        cin >> value;
        transformed_a.push_back(value);
    }

    vector<int> list_valid(n, 0);
    int max_value = transformed_a[0];
    int min_value = transformed_a[transformed_a.size()-1];

    for (int i=0; i<n; i++) {
        int pivot_left = transformed_a[i];
        if (pivot_left >= max_value) {
            list_valid[i] += 1;
            max_value = pivot_left;
        }

        int last_index = n - (i + 1);
        int pivot_right = transformed_a[last_index];
        if (pivot_right <= min_value) {
            list_valid[last_index] += 1;
            min_value = pivot_right;
        }
    }

    int total_pivot = 0;
    for (int i=0; i<n; i++) {
        if (list_valid[i] == 2) {
            total_pivot++;
        }
    }

    cout << total_pivot << endl;
}