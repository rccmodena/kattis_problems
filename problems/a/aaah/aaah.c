/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

#define AH_SIZE 1000


int main(void) {
    char marius_ah[AH_SIZE];
    char doctor_ah[AH_SIZE];

    if (scanf("%s\n", marius_ah) != 1) {
        printf("Failed to read marius_ah!");
    }

    if (scanf("%s\n", doctor_ah) != 1) {
        printf("Failed to read doctor_ah!");
    }

    if (strlen(marius_ah) >= strlen(doctor_ah)) {
        printf("go\n");
    }
    else {
        printf("no\n");
    }

    return 0;
}