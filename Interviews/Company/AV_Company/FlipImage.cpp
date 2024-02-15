#include <vector>
#include <iostream>
using namespace std;

void flipImage(vector<vector<char> >& image) {
  for (size_t i = 0; i < image.size(); ++i) {
    size_t col_size = image[i].size();
    for (size_t j = 0; j < col_size / 2; ++j) {
      char tmp = image[i][j];
      image[i][j] = image[i][col_size - 1 - j];
      image[i][col_size - 1 - j] = tmp;
    }
  }
}


int main() {
    vector<vector<char> > image = {{'0', '0', '1', '1'}, {'1', '0', '0', '0'}};
    flipImage(image);

    for (size_t i = 0; i < image.size(); ++i) {
        for (size_t j = 0; j < image[i].size(); ++j) {
            cout << image[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
