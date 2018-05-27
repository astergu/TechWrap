/**
 *
 * Implement pow(A, B) % C.
 * In other words, given A, B and C, find (AB)%C.
 *
 * Constraints:

        1 ≤ T ≤ 70

        1 ≤ A ≤ 10^5

        1 ≤ B ≤ 10^5

        1 ≤ C ≤ 10^5
* 
* Example:
*   3, 2, 4
*   
*   3^2 = 9
*   9 % 4 = 1
*
*   10, 9, 6
*   10 % 6 = 4
*
*
*/

#include <iostream>
using namespace std;


int expo(int a, int b, int c) {
    if (b == 0) {
        return 1;
    }
    if (b == 1) {
        return a % c;
    }
    a = a % c;
    if (b % 2 != 0) { // odd 
        return (a % c * (expo(a * a, b / 2, c) % c) % c);
    } else {
        return expo(a * a, b / 2, c) % c;
    }
}


int main() {
	//code
    int T;
    cin >> T;
    while (T--) {
        int a, b, c;
        cin >> a >> b >> c;
        int ret = expo(a, b, c);
        cout << ret << endl;
    }

	return 0;
}
