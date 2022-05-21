/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>

#define EPSILON 0.000001

using namespace std;

int main() {
    int gunnar_dice[4], emma_dice[4];
    double gunnar_sum, emma_sum;

    if (scanf("%d %d %d %d\n", &gunnar_dice[0], &gunnar_dice[1], &gunnar_dice[2], &gunnar_dice[3]) != 4) {
        printf("Failed to read gunnar_dice!");
    }

    if (scanf("%d %d %d %d\n", &emma_dice[0], &emma_dice[1], &emma_dice[2], &emma_dice[3]) != 4) {
        printf("Failed to read emma_dice!");
    }

    gunnar_sum = ((gunnar_dice[0] + gunnar_dice[1]) / 2.0) + ((gunnar_dice[2] + gunnar_dice[3]) / 2.0);
    emma_sum = ((emma_dice[0] + emma_dice[1]) / 2.0) + ((emma_dice[2] + emma_dice[3]) / 2.0);

    if (abs(gunnar_sum - emma_sum) < EPSILON) {
        cout << "Tie" << endl;
    }
    else if (gunnar_sum > emma_sum) {
        cout << "Gunnar" << endl;
    }
    else {
        cout << "Emma" << endl;        
    }
}