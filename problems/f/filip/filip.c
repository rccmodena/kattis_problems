/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int reverse_number(int num)
{
    int result = 0;

    while (num > 0) {
        result = (result * 10) + (num % 10);
        num = num / 10;
    }
    return result;
}

int main(void) {
    int a, b;
    if (scanf("%d%d", &a, &b) != 2) {
        printf("Failed to read a and b!");
    }
    a = reverse_number(a);
    b = reverse_number(b);
    if (a > b) {
        printf("%d", a);
    }
    else {
        printf("%d", b);
    }
    
    return 0;
}