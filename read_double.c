#include "read_input.h"
#include <stdio.h>
#include <limits.h>

#define SIZE 50

int read_real(char* digits, int n, double* num){
  if(get_string(digits, n)== EOF){
    return EOF;
  } 
  printf("%s","pass 1");

  if(is_valid_double(digits)){
    if(digits[0] == '-')
      *num = -convert_to_double(digits + 1);
    else if(digits[0] == '+') 
      *num = convert_to_double(digits + 1);
    else
      *num = convert_to_double(digits);
    return 1;
  }
// gcc -Wall prog_two.c read_double.c read_input.c -o lab4exC
  return 0;
}
int is_valid_double(const char* digits){
    int valid = 1;
    int i;
    int count = 0;
    
    if(digits[0] == '+' || digits[0] == '-'){
        i = 1;
    } else {
        i = 0;
    }
    if (digits[i] == '\0'){
      valid = 0;
    }else{
      printf("%s","pass 2");
    while (valid && (digits[i] != '\0')) {
      printf("%s","passing 3");
        if(digits[i] < '0' ||  digits[i] > '9'){
            if(digits[i] == '.' && count==0){
                count = 1;
            }else{
                valid = 0;
            }
        }
        i++;
    }
    }
  printf("%s","pass 3");
  return valid;
}
double convert_to_double(const char *digits){
    // float sum = 0;
    // int i = 0;
    // float position = 1;
    // while(*digits != '.') {
    //     sum = 10 * sum + (*digits - '0');
    //     digits++;
    // }
    // while(*digits != '\0') {
    //     for (int a = 0; a <= i; a++){
    //         position = position * 0.1;
    //     }
    //     sum = sum + (position*(*digits - '0'));
    // }
    // return sum;
    int sum1 = 0;
    double sum2 = 0;
    double sum3 = 0;
    int i = 0;
    int a;
    int post_point = 0;
    while(digits[i] != '.') {
        sum1 = 10 * sum1 + (digits[i] - '0');
        i++;
        post_point++;
    }
    i++;
    while (digits[i] != '\0'){
        i++;
    }
    for (a = i-1; a>post_point; a--){
        sum2 = 0.1 * sum2 + (digits[a] - '0');
        printf("%f\n", sum2);
    }
    sum2 = sum2*0.1;
    printf("%d  |  %f", sum1, sum2);
    sum3 = sum1 + sum2;
    return sum3;
}
