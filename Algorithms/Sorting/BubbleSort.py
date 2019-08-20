def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


if __name__ == '__main__':
    A = [1, 3, 2, 9, 6]
    bubble_sort(A)
    print(A)
