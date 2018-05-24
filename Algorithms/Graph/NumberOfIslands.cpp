#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char> >& grid) {
        if (grid.empty() || grid.size() == 0 || grid[0].size() == 0) {
            return 0;
        }
        
        int count = 0;
        const int rows = grid.size();
        const int cols = grid[0].size();
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j, rows, cols);
                }
            }
        }
        return count;
    }
    
    void dfs(vector<vector<char> >& grid, int i, int j, int rows, int cols) {
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] == '0') {
            return;
        }
        grid[i][j] = '0';
        dfs(grid, i + 1, j, rows, cols);
        dfs(grid, i - 1, j, rows, cols);
        dfs(grid, i, j + 1, rows, cols);
        dfs(grid, i, j - 1, rows, cols);
    }
};


int main() {
    vector<vector<char> > grid = {
                                {'1', '1', '0', '0', '0'},
                                {'1', '1', '0', '0', '0'},
                                {'0', '0', '1', '0', '0'},
                                {'0', '0', '0', '1', '1'}
                                };

    cout << grid.size() << endl;
    cout << grid[0].size() << endl;
    Solution s;
    int ret = s.numIslands(grid);
    cout << "ret: " << ret << endl;
    return 0;
}
