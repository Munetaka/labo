import numpy as np

def softmax(x):
    e_x = np.exp(x -np.max(x)) # prevent overflow
    if e_x.ndim == 1:
        y = e_x / np.sum(e_x)
    else:
        y = e_x / np.sum(e_x, axis=1)[:, np.newaxis]
        # y = e_x / np.array([np.sum(e_x, axis=1)]).T
    return y

if __name__ == '__main__':
    X = np.array([40, 10, 100]);
    y = softmax(X)
    print(y)
    print(np.sum(y))

    X = np.array([[1, 10, 100], [53, 23, 30]]);
    y = softmax(X)
    print(y)
    print(np.sum(y, axis=1)[:, np.newaxis])
