/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int r, n, found_room;

    if (scanf("%d %d\n", &r, &n) != 2) {
        printf("Failed to read r and n!");
    }

    int reserved_rooms[n];

    for (int i=0; i<n; i++) {
        if (scanf("%d", &reserved_rooms[i]) != 1) {
            printf("Failed to read reserved room!");
        }
    }

    if (r == n) {
        printf("too late");
    }
    else {
        for (int i=1; i<=r; i++){
            found_room = 1;
            for (int j=0; j<n; j++){
                if (i == reserved_rooms[j]){
                    found_room = 0;
                    break;
                }
            }
            if (found_room == 1) {
                printf("%d\n", i);
                break;
            }
        }
    }

    return 0;
}