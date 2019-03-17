import numpy as np


def calculate_error(X, X_, D, lag):
    def part(x, x_):
        result = 0
        for i in range(len(x)):
            result = result + (x[i] - x_[i])**2
        return result

    N = len(X)
    std = np.std(X)
    E2 = (1 / ((N - D) * std ** 2)) * part(X, X_)
    return E2
