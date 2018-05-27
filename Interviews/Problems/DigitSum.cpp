/**
 * Implement a program, which given an integer n, computes the sum of its digits.

If a negative number is given, the function should work as if it was positive.

For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum is 1 + 0 = 1.

In the test cases for this task we will have that -2^63 < n < 2^63.
 *
 */

#include <iostream>
#include <cmath>
using namespace std;


int digit_sum(long long number) {
    // Write your code here
    number = abs(number);
    int dsum = 0;
    while (number > 0) {
        dsum += number % 10;
        number /= 10;
    }
    return dsum;
}

int main() {
    long long number;
    cin >> number;
    int dsum = digit_sum(number);
    cout << dsum << endl;
    return 0;
}
