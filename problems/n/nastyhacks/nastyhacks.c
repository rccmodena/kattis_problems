/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, r, e, c;
    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        if (scanf("%d%d%d", &r, &e, &c) != 3) {
            printf("Failed to read r, e and c!");
        }
        
        if (r == (e - c)) {
            printf("does not matter\n");
        }
        else if (r > (e - c)) {
            printf("do not advertise\n");
        }
        else {
            printf("advertise\n");
        }

    }

    return 0;
}