/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>
 
int main(void) {
    char month[7];
    int day;

    if (scanf("%s %d", month, &day) != 2) {
        printf("Failed to read data!");
    }

    if ((strcmp(month, "OCT") == 0 && day == 31) || (strcmp(month, "DEC") == 0 && day == 25)) {
        printf("yup");
    }
    else {
        printf("nope");
    }

    return 0;
}