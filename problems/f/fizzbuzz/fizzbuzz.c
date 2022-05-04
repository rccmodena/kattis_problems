/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int x, y, n;
    if (scanf("%d %d %d", &x, &y, &n) != 3) {
        printf("Failed to read x, y, n!");
    }

    for (int i=1; i<=n; i++){
        if (i % x == 0 && i % y == 0) {
            printf("FizzBuzz\n");
        }
        else if (i % x == 0) {
            printf("Fizz\n");
        }
        else if (i % y == 0) {
            printf("Buzz\n");
        }
        else {
            printf("%d\n",i);
        }
    }

    return 0;
}