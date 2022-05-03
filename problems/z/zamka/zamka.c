/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

int count_digits(int value) {
    int sum = 0;
    int number = value;
    int power = 0;

    while (number > pow(10, power)) {
        power++;
    }

    while (power >= 0) {
        int digit = number / pow(10, power);
        sum += digit;
        if (digit != 0) {
            number -= digit * pow(10, power);
        }
        power--;
    }
    return sum;
}

int main(void) {
    int l, d, x;
    int n, m;

    if (scanf("%d\n%d\n%d", &l, &d, &x) != 3) {
        printf("Failed to read l!");
    }

    n = 0;
    for (int val=l; val<d+1; val++) {
        if (x == count_digits(val)) {
            n = val;
            break;
        }
    }

    m = 0;
    for (int val=l; val<d+1; val++) {
        if (x == count_digits(val)) {
            m = val;
        }
    }

    printf("%d\n%d", n, m);
 
    return 0;
}