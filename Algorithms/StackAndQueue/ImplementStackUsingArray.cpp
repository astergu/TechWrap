#include <iostream>
using namespace std;


class Stack {
private:
    int arr[1000];
    int top;
public:
    Stack() { top = -1; }
    int pop() {
        return arr[top--];
    }

    void push(int x) {
        arr[++top] = x;
    }

    void printStack() {
        cout << "___________ Stack ____________" << endl;
        for (int i = 0; i <= top; ++i) {
            cout << arr[i] << endl;
        }
    }
};


int main() {
    Stack s;
    s.push(2);
    s.push(3);
    int ret = s.pop();
    cout << "Pop " << ret << endl;
    s.printStack();
    return 0;
}
