/**
 * The task is to complete select() function which is used to implement Selection Sort.

    Input:
    First line of the input denotes number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.


    Output:
    Sorted array in increasing order is displayed to the user.

Constraints:
    1 <=T<= 50
    1 <=N<= 1000
    1 <=arr[i]<= 1000

 *
 */

#include <iostream>
using namespace std;

int select(int arr[], int i);

void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n) {
   int i, j;
   for (i = n - 1; i >= 0; i--) {
        int j = select(arr, i);
        swap(&arr[i], &arr[j]);
   }
}

int select(int arr[], int i)
{
    // Your code here  
    int maxIdx = 0;
    for (int k = 0; k <= i; ++k) {
        if (arr[k] > arr[maxIdx]) {
            maxIdx = k;
        }
    }
    return maxIdx;
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
        selectionSort(arr, n);
        //cout << "________________" << endl;
        printArray(arr, n);
    }

    return 0;
}
