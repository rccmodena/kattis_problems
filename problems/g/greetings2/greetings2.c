/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    char s[1001], r[2002];
    int n_e, counter_e;
    if (scanf("%s", s) != 1) {
        printf("Failed to read s!");
    }

    n_e = 0;
    for (int i=0; s[i] != '\0'; i++) {
        if (s[i] == 'e') {
            n_e++;
        }
    }

    r[0] = 'h';

    counter_e = 1;
    while (counter_e <= (n_e * 2)) {
        r[counter_e] = 'e';
        counter_e++;
    }
    r[counter_e] = 'y';
    r[counter_e + 1] = '\0';

    printf("%s", r);

    return 0;
}