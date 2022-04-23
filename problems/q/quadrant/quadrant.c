#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x, y;
    while (scanf("%d%d", &x, &y) == 2)
        if (x > 0) {
            if (y > 0) {
                printf("%d", 1);
            }
            else {
                printf("%d", 4);
            }
        }
        else{
            if (y > 0) {
                printf("%d", 2);
            }
            else {
                printf("%d", 3);
            }
        }

    return 0;
}