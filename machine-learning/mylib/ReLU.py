import numpy as np

def ReLU(x):
    return x * (x > 0)


if __name__ == '__main__':
    X = np.array([[-1, 0, 3], [-10, -2, 6]])
    y = ReLU(X)
    print(y)
