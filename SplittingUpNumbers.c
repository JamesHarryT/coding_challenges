#include <stdio.h>
#include <stdbool.h>

int size;
int value[10];

void num_split(int num) {
    size = 0;
    int place = 1;
    bool isNegative = false;
    if (num < 0) {
        isNegative = true;
        num = -num;
    }
    while (num > 0) {
        int digit = num % 10;
        if (isNegative) {
            int temp = digit * place;
            value[size] = -temp;
        }
        else {
            value[size] = digit * place;
        }
        num /= 10;
        place *= 10;
        (size)++;
    }
}

void printBackwards(int size) {
    printf("[");
    for (int i = size - 1; i >= 0; i--) {
        printf("%d", value[i]);
        if (i > 0) printf(", ");
    }
    printf("]\n");
}

void main() {

    num_split(39);
    printBackwards(size);

    num_split(-434);
    printBackwards(size);

    num_split(100);
    printBackwards(size);
}