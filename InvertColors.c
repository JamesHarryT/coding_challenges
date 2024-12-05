#include <stdio.h>

void color_invert(int color[3]) {
    int output[3];
    printf("[");
    for (int i = 0; i < 3; i++) {
        int value = 255 - color[i];
        output[i] = value;
        printf("%d", output[i]);
        if (i < 2) {
            printf(", ");
        }
    }
    printf("]\n");

}

void main() {
    int option1[] = {255, 255, 255};
    color_invert(option1);
    int option2[] = {0, 0, 0};
    color_invert(option2);
    int option3[] = {165, 170, 221};
    color_invert(option3);
}