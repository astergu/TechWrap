/**
 * Given N * M string array of O's and X's
    Return the number of 'X' total shapes. 'X' shape consists of one or more adjacent X's (diagonals not included).

    Example (1):

    OOOXOOO
    OXXXXXO
    OXOOOXO

    answer is 1 , shapes are  :
    (i)     X
        X X X X
        X     X

 *
 *  Constraints:

        1<=T<=100

        1<=N,M<=50
 */


#include <iostream>
#include <vector>
using namespace std;

int numberOfShapes() {
    return 0;
}


int main() {
	//code
    int T;
    cin >> T;
    while (T--) {
        int row, col;
        cin >> row >> col;
        vector<vector<char> > input[row][col];
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                char tmp;
                cin >> tmp;
                input[i][j]
                //cin >> input[i][j];
            }
        }
    }

	return 0;
}
