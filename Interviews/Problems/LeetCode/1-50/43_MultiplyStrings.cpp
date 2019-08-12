#include <string>
using namespace std;

class Solution {
 public:
  string multiply(string num1, string num2) {
    int carry = 0;
    int total_sum = 0;
    for (auto s1 : num1) {
      for (auto s2 : num2) {
        int n1 = s1 - "0";
        int n2 = s2 - "0";
        int local_sum = carry + n1 + n2;
        carry = local_sum / 10;
        int rem = local_sum % 10;
      }
    }
  }
};