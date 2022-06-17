/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    while (cin >> n) {
        cin.ignore();

        stack<int> mock_stack;
        queue<int> mock_queue;
        priority_queue<int> mock_priority_queue;

        vector<int> valid_stack;
        vector<int> valid_queue;
        vector<int> valid_priority_queue;

        int command, x;
        for (int i=0; i<n; i++) {
            cin >> command >> x;
            cin.ignore();

            if (command == 1) {
                mock_stack.push(x);
                mock_queue.push(x);
                mock_priority_queue.push(x);
            }
            else {
                if (!mock_stack.empty()) {
                    if (mock_stack.top() == x) {
                        valid_stack.push_back(1);
                    }
                    else {
                        valid_stack.push_back(0);
                    }
                    mock_stack.pop();
                }
                else {
                    valid_stack.push_back(0);
                }

                if (!mock_queue.empty()) {
                    if (mock_queue.front() == x) {
                        valid_queue.push_back(1);
                    }
                    else {
                        valid_queue.push_back(0);
                    }
                    mock_queue.pop();
                }
                else {
                    valid_queue.push_back(0);
                }

                if (!mock_priority_queue.empty()) {                    
                    if (mock_priority_queue.top() == x) {
                        valid_priority_queue.push_back(1);
                    }
                    else {
                        valid_priority_queue.push_back(0);
                    }
                    mock_priority_queue.pop();
                }
                else {
                    valid_priority_queue.push_back(0);
                }
            }
        }

        vector<string> results;

        size_t sum_stack = 0;
        for (auto& value : valid_stack) {
            sum_stack += value;
        }
        if (valid_stack.empty() || (sum_stack>0 && sum_stack == valid_stack.size())) {
            results.push_back("stack");
        }

        size_t sum_queue = 0;
        for (auto& value : valid_queue) {
            sum_queue += value;
        }
        if (valid_queue.empty() || (sum_queue>0 && sum_queue == valid_queue.size())) {
            results.push_back("queue");
        }

        size_t sum_priority_queue = 0;
        for (auto& value : valid_priority_queue) {
            sum_priority_queue += value;
        }
        if (valid_priority_queue.empty() || (sum_priority_queue>0 && sum_priority_queue == valid_priority_queue.size())) {
            results.push_back("priority queue");
        }
        
        if (results.size() == 0) {
            cout << "impossible" << endl;
        }
        else if (results.size() == 1) {
            cout << results[0] << endl;
        }
        else {
            cout << "not sure" << endl;
        }
    }
}