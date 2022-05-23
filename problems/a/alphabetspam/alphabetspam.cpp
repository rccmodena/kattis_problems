/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;


int is_white(char letter) {
    if (letter == '_') {
        return true;
    }
    else {
        return false;
    }
}


int is_lower(char letter) {
    const char *LOWER = "abcdefghijklmnopqrstuvwxyz";
    for (int i=0; LOWER[i] != '\0'; i++) {
        if (LOWER[i] == letter) {
            return true;
        }
    }
    return false;
}


int is_upper(char letter) {
    const char *UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (int i=0; UPPER[i] != '\0'; i++) {
        if (UPPER[i] == letter) {
            return true;
        }
    }
    return false;
}


int main(void) {
    int string_size, count_white, count_lower, count_upper, count_symbol;
    string_size = count_white = count_lower = count_upper = count_symbol = 0;
    double ratio_white, ratio_lower, ratio_upper, ratio_symbol;
    string message;

    cin >> message;

    string_size = message.length();

    for (int i=0; i<string_size; i++) {
        if (is_white(message[i])) {
            count_white++;
        }
        else if (is_lower(message[i])) {
            count_lower++;
        }
        else if (is_upper(message[i])) {
            count_upper++;
        }
        else {
            count_symbol++;
        }
    }
    ratio_white = (double)count_white / (double)string_size;
    ratio_lower = (double)count_lower / (double)string_size;
    ratio_upper = (double)count_upper / (double)string_size;
    ratio_symbol = (double)count_symbol / (double)string_size;

    printf("%.16f\n", ratio_white);
    printf("%.16f\n", ratio_lower);
    printf("%.16f\n", ratio_upper);
    printf("%.16f\n", ratio_symbol);

    return 0;
}