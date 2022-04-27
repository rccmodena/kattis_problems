/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, t, m, designs;
    if (scanf("%d%d%d", &n, &t, &m) != 3) {
        printf("Failed to read n, t and m!");
    }

    designs = n * t * m;
    printf("%d", designs);

    return 0;
}