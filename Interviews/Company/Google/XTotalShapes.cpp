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

bool checkSurrounding(const vector<vector<char> >& input, const vector<vector<bool> >& visited, int row, int col, int i, int j);

    
int numberOfShapes(const vector<vector<char> >& input, int row, int col) {
    int count = 0;
    vector<vector<bool> > visited;
    for (int i = 0; i < row; ++i) {
        vector<bool> colVisited;
        for (int j = 0; j < col; ++j) {
            colVisited.push_back(false);
        }
        visited.push_back(colVisited);
    }

    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (!visited[i][j]) {
                bool ret = checkSurrounding(input, visited, row, col, i, j);
                if (ret) {
                    count++;
                }
                visited[i][j] = true;
            }
        }
    }

    return count;
}


bool checkSurrounding(const vector<vector<char> >& input, const vector<vector<bool> >& visited, int row, int col, int i, int j) {
    if (i < 0 || i > row || j < 0 || j > col) {
        return true;
    }
    if (!visited[i][j] && input[i][j] == 'X') {
        bool x1 = checkSurrounding(input, visited, row, col, i - 1, j);
        bool x2 = checkSurrounding(input, visited, row, col, i + 1, j);
        bool x3 = checkSurrounding(input, visited, row, col, i, j - 1);
        bool x4 = checkSurrounding(input, visited, row, col, i, j + 1);
        return x1 && x2 && x3 && x4;
    } 
    return false;
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
                cin >> input[i][j];
            }
        }
    }

	return 0;
}
