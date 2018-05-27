/**
 * You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    You need to do this in place.

    Note that if you end up using an additional array, you will only receive partial score.

*   Example:

    If the array is 

    1 2 3 
    4 5 6 
    7 8 9

    Then the rotated array becomes: 
    
    7 4 1 
    8 5 2 
    9 6 3
 * 
 *
 * Constraints:

        1 ≤ T ≤ 70
        1 ≤ N ≤ 10
        1 ≤ A [ i ][ j ] ≤ 100
 */

#include <iostream>
#include <vector>
using namespace std;

void rotate(vector<vector<int> >& matrix) {

}


int main() {
	//code
	vector<vector<int> > matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    rotate(matrix);

    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}


