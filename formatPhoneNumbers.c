#include <stdio.h>

void formatPhoneNumber(int number[11]) {
    printf("(");
    for (int i = 0; i < 3; i++) {
        printf("%d", number[i]);
    }
    printf(") ");
    for (int i = 3; i < 6; i++) {
        printf("%d", number[i]);
    }
    printf("-");
    for (int i = 6; i < 10; i++) {
        printf("%d", number[i]);
    }
    printf("\n");
}

void main() {
    int numberOne[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    formatPhoneNumber(numberOne);
    //output = "(123) 456-7890"
    int numberTwo[10] = {5, 1, 9, 5, 5, 5, 4, 4, 6, 8};
    formatPhoneNumber(numberTwo);
    //output = "(519) 555-4468"
    int numberThree[10] = {3, 4, 5, 5, 0, 1, 2, 5, 2, 7};
    formatPhoneNumber(numberThree);
    //output = "(345) 501-2527"
}
