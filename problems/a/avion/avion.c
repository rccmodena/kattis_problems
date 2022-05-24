/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <string.h>

#define REGISTRATION_SIZE 12
#define REGISTRATIONS 5

int main(void) {
    int regitration_size, found_fbi;
    char registration[REGISTRATION_SIZE];

    found_fbi = 0;
    for (int i=0; i<REGISTRATIONS; i++) {
        if (scanf("%s", registration) != 1) {
            printf("Failed to read registration!");
        }

        regitration_size = strlen(registration) - 3;

        for (int j=0; j<=regitration_size; j++) {
            if (registration[j] == 'F' && registration[j + 1] == 'B' && registration[j + 2] == 'I') {
                found_fbi = 1;
                printf("%d ", i + 1);
                break;
            }
        }
    }

    if (found_fbi == 0) {
        printf("HE GOT AWAY!\n");
    }


    return 0;
}