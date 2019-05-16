#coding=utf8

import sys
sys.path.append('..')
import numpy as np
from sklearn.linear_model import Perceptron as sk_perceptron
from common import activate_func


class Perceptron(object):
    def __init__(self, theta=0.01, n_iter=10):
        self._theta = theta   # learning rate
        self._n_iter = n_iter  # number of iterations

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self._n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self._theta * (target - self.predict(xi))
                #update = self._theta * self.predict(xi)
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
            print("iter: {}, error: {}".format(_, errors))
            if errors == 0:
                break
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def print_parameters(self):
        print("w: {}".format(self.w_))


if __name__ == '__main__':
    X = np.array([[-2, 3, -1, 0], [1, 3, -2, 1]])
    print(X.shape)
    y = np.array([1, -1])
    skp = sk_perceptron()
    skp.fit(X, y)
    print("----------------------------")
    print("Coef: {}".format(skp.coef_))
    print("Intercept: {}".format(skp.intercept_))
    print(skp.predict(X))

    print("----------------------------")
    p = Perceptron()
    p.fit(X, y)
    p.print_parameters()
    print(p.predict(X))
