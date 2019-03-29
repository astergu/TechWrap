#coding=utf8

import numpy as np 


def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (n, m).

    Argument:
    x -- A numpy matrix of shape (n,m)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    """
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    s = x_exp / x_sum
    
    return s


if __name__ == '__main__':
    x = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])
    print("softmax(x) = {}".format(softmax(x)))