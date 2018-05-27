/**
 * You know how sometimes files with numbers in them get sorted lexicographically, which produces incorrect sequences of files. For example people use to have tons and tons of pictures and they are often named like that: IMG123456.jpg.

Imagine that you have a set of N image files, which are numbered from 1 to N like that: IMG1.jpg, IMG2.jpg, IMG3.jpg, and so on.

If sorted by name the order could start to look incorrect if there are at least 10 files:

IMG1.jpg
IMG10.jpg
IMG11.jpg
IMG12.jpg
…

Your task is given N to return the sorted lexicographically list of file names. N is in the range [1, 1,000,000]. In 40% of the test cases N will be no higher than 1,000. If N if higher than 1,000 return just the first 1,000 file names.

Write a function which accepts two parameters - the number N and a list in which it must store the filenames in the correct sorted order. Look at the boilerplate code for your favorite language.
 *
 *
 */

#include <vector>
#include <string>
#include <sstream>

using namespace std;

void sort_the_files(int n, vector<string>& result) {
    // Write your code here
}

