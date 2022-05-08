/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

#define CONTESTANTS_SIZE 5

using namespace std;

int main() {
    int grade_1, grade_2, grade_3, grade_4, winner_id, winner_points, points;

    winner_id = 0;
    winner_points = 0;
    for (int i=0; i<CONTESTANTS_SIZE; i++) {

        cin >> grade_1 >> grade_2 >> grade_3 >> grade_4;

        points = grade_1 + grade_2 + grade_3 + grade_4;

        if (winner_points < points) {
            winner_id = i + 1;
            winner_points = points;
        }
    }

    cout << winner_id << " " << winner_points << endl;
}