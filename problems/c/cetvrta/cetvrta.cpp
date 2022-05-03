/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int x_points[3], y_points[3];
    int fourth_x, fourth_y;

    for (int row=0; row<3; row++) {
            cin >> x_points[row];
            cin >> y_points[row];
    }

    if (x_points[0] == x_points[1]) {
        fourth_x = x_points[2];
    }
    else if (x_points[0] == x_points[2]) {
        fourth_x = x_points[1];
    }
    else {
        fourth_x = x_points[0];
    }

    if (y_points[0] == y_points[1]) {
        fourth_y = y_points[2];
    }
    else if (y_points[0] == y_points[2]) {
        fourth_y = y_points[1];
    }
    else {
        fourth_y = y_points[0];
    }

    cout << fourth_x << " " << fourth_y << endl;
}