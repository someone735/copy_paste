#include <stdio.h>
#include <limits.h>
#include <string.h>


char * copystr(const char* source){
    char* dest;
    int i = 0;
    while (source[i] != '\0'){
        dest[i] = source[i];
        i++;
    }
    dest[i] = '\0';
    return dest;
}

int main(void){
    const char *s1 = "ABCD";
    char *s2 = copystr(s1);
    printf(s2);
    return 0;
}