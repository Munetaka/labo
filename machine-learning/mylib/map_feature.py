import numpy as np

def mapFeature(X1, X2, degree=6):
    m = X1.shape[0]
    X = np.ones((m, 1))
    for i in range(1, degree + 1):
        for j in range(0, i + 1):
            newX = (X1 ** (i - j) * X2 ** j).reshape((m, 1))
            X = np.hstack((X, newX))
    return X
