import numpy as np

def sigmoid(x):
    return 1. / (1. + np.exp(-x))


if __name__ == '__main__':
    X = np.array([-10, -1, 0, 1, 10])
    y = sigmoid(X)
    print(y)
