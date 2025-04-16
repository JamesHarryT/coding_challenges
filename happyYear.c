#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void happyYear(int year) {
    bool isHappyYear = false;
    while (isHappyYear == false) {
        year += 1;
        char strYear[5];
        sprintf(strYear, "%d", year);
        bool foundDuplicate = false;
        int len = strlen(strYear);
        for (int i = 0; i < len; i++) {
            if (foundDuplicate == true) continue;

            for (int j = 0; j < len; j++) {
                if (i == j) continue;
                else if (strYear[i] == strYear[j]) {
                    foundDuplicate = true;
                    break;
                }

            if (foundDuplicate == true) break;
            
            }
        }
        if (foundDuplicate == false) {
            isHappyYear = true;
        }
    }
    printf("%d\n", year);
}

int main() {
    happyYear(2017);
    happyYear(1990);
    happyYear(2021);
}