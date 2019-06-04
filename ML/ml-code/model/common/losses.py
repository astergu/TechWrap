import numpy as np


class Loss(object):
    def log_loss(self, target, predicted, eps=1e-15):
        p = np.clip(predicted, eps, 1 - eps)
        if target == 1:
            return -log(p)
        return -log(1 - p)
        