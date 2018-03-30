/*
 * Write a “C” function, int addOvf(int* result, int a, int b) If there is no overflow, the function places the resultant = sum a+b in “result” and returns 0. Otherwise it returns -1. The solution of casting to long and adding to find detecting the overflow is not allowed.
 */

#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int addOvf(int* result, int a, int b) {
    if (a > 0 && b > 0 && a > INT_MAX - b)
        return -1;
    else if (a < 0 && b < 0 && a < INT_MIN - b)
        return -1;
    else {
        *result = a + b;
        return 0;
    }
}


int main() {
    int *res = (int *)malloc(sizeof(int));
    int x = 2147483640;
    int y = 10;
    printf("%d", addOvf(res, x, y));
    printf("\n %d", *res);
    return 0;
}
