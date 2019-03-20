from math import exp


def sgn(x, center=0):
    """
    step function
    """
    if x >= center:
        return 1
    return 0


def sigmoid(x):
    """
    sigmoid function
    """
    return 1 / (1 + exp(-x))
