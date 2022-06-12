/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include "vectorfunctions.h"

void backwards(std::vector<int>& vec){
    int vec_size = vec.size();
    for(int i=0; i<vec_size/2; i++) {
        int index_end = vec_size - i - 1;

        int temp = vec[index_end];
        vec[index_end] = vec[i];
        vec[i] = temp;
    }
}

std::vector<int> everyOther(const std::vector<int>& vec){
    std::vector<int> new_vec;
    for(size_t i=0; i<vec.size(); i++) {
        if(i % 2 == 0) {
            new_vec.push_back(vec[i]);
        }
    }

    return new_vec;
}

int smallest(const std::vector<int>& vec){
    int smallest_value = vec[0];
    for (int i : vec) {
        if (i < smallest_value) {
            smallest_value = i;
        }
    }

    return smallest_value;
}

int sum(const std::vector<int>& vec){
    int total = 0;

    for (int n : vec) {
        total += n;
    }

    return total;
}

int veryOdd(const std::vector<int>& suchVector){
    int total_odd = 0;

    for(size_t i=0; i<suchVector.size(); i++) {
        if (i % 2 == 1 && suchVector[i] % 2 == 1) {
            total_odd++;
        }
    }

    return total_odd;
}
