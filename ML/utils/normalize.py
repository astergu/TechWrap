#coding=utf8

import sys
import numpy as np 


def normalizeRows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    x = x / x_norm
    return x


if __name__ == '__main__':
    x = np.array([[0, 3, 4], [1, 6, 4]])
    print("normalized rows(x): {}".format(normalizeRows(x)))