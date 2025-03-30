#include <stdio.h>
#include <stdbool.h>

void lemonade(int *payment, int size) {
    bool canPayChange = true;
    int tens = 0;
    int fives = 0;
    for (int i = 0; i < size; i++) {
        if (payment[i] == 5) {
            fives += 1;
        }
        else if (payment[i] == 10) {
            tens += 1;
            fives -= 1;
        }
        else if (payment[i] == 20) {
            if (fives >= 1 && tens >= 1) {
                fives -= 1;
                tens -= 1;
            }
            else if (fives >= 3) {
                fives -= 3;
            }
            else {
                canPayChange = false;
            }
        }
    }
    if (fives < 0 || tens < 0) {
        canPayChange = false;
    }
    printf("%s\n", canPayChange ? "true" : "false");
}
//FIX SO THAT FOR $20 IT PAYS $15
void main() {
    int arr1[5] = {5, 5, 5, 10, 20};
    lemonade(arr1, 5);
    //output = True
    int arr2[5] = {5, 5, 10, 10, 20};
    lemonade(arr2, 5);
    //output = False
    int arr3[2] = {10, 10};
    lemonade(arr3, 2);
    //output = False
    int arr4[3] = {5, 5, 10};
    lemonade(arr4, 3);
    //output = True
}