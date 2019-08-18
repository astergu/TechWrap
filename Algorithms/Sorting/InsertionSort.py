"""
CLRS chapter 2.
"""


def insertionSort(A):
    for i in range(1, len(A)):
        if A[i] >= A[i - 1]:
            continue
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


if __name__ == '__main__':
    A = [1, 3, 5, 9, 2, 6]
    insertionSort(A)
    print(A)
