'''
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

    MyCircularDeque(int k) Initializes the deque with a maximum size of k.
    boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
    int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
    int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
    boolean isEmpty() Returns true if the deque is empty, or false otherwise.
    boolean isFull() Returns true if the deque is full, or false otherwise.

'''


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.q = [0] * self.size
        self.front = -1
        self.rear = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.size
        self.q[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        item = self.q[self.rear]
        if self.front == self.rear: # only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        item = self.q[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size
        return True                  

    def getFront(self) -> int:
        if self.front == -1:
            return -1
        return self.q[self.front]        

    def getRear(self) -> int:
        if self.rear == -1:
            return -1
        return self.q[self.rear]        

    def isEmpty(self) -> bool:
        return self.front == self.rear == -1

    def isFull(self) -> bool:
        if (self.rear + 1) % self.size == self.front:
            return True
        return False


if __name__ == '__main__':
    k = 3
    mcd = MyCircularDeque(k)