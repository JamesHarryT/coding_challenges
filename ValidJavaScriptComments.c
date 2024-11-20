#include<stdio.h>
#include <stdbool.h>
bool comments_correct(char *comment) {
    for (int i = 0; comment[i] != '\0';) {
        if (comment[i] == '/' && comment[i + 1] == '/') {
            i += 2;
        }
        else if (comment[i] == '/' && comment[i+1] == '*') {
            i += 2;
            if (comment[i] != '*' && comment[i + 1] != '/') {
                 return false;
            }
            i += 2; 
        }
        else {
            return false;
        } 
        }
    return true;
}
void main() {
    printf("%s\n", comments_correct("//////") ? "true" : "false");
    printf("%s\n", comments_correct("/**//**////**/") ? "true" : "false");
    printf("%s\n", comments_correct("///*/**/") ? "true" : "false");
    printf("%s\n", comments_correct("/////") ? "true" : "false");
}