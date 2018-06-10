/***
 * Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and returns the encoded string.


Input (To be used only for expected output):
    The first line contains T denoting no of test cases . Then T test cases follow . Each test case contains a string str which is to be encoded .

Output:
    For each test case output in a single line the so encoded string .

Constraints:
    1<=T<=100
    1<=length of str<=100
 *
 */

#include <iostream>
using namespace std;


char *encode(char *src)
{     
      //Your code here
      char *dest = new char[500];
      char prev = '\0';
      int count = 0;
      int i = 0, j = 0;
      while (src[i] != '\0') {    
          if (prev == '\0' || src[i] != prev) {
              if (prev != '\0') {
                  dest[j++] = '0' + count;
              }
              dest[j++] = src[i];
              count = 1;
              prev = src[i];
          } else {
              count++;
          }
          i++;
      }

      dest[j++] = '0' + count;

      return dest;
} 


int main() {
    int T;
    char src[100] = "hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac";
    //cin.getline(src, 100);
    cout << "src: " << src << endl;
    char* ret = encode(src);
    cout << "\nret: " << ret << endl;

    return 0;
}
