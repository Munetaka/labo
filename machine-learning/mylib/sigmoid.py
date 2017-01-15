import numpy as np

def sigmoid(x):
    sigmoid_min_int = -709
    x[x < sigmoid_min_int] = sigmoid_min_int
    return 1. / (1. + np.exp(-x))


if __name__ == '__main__':
    X = np.array([-1709, -709, 0, 1, 1000000000])
    y = sigmoid(X)
    print(y)
