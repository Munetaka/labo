import numpy as np


def feature_normalize(x):
    if x.ndim == 1:
        x_mean = x.mean()
        mu = np.mean(x - x_mean)
        x_norm = x - x_mean
        sigma = np.std(x / np.std(x_norm))
        x_norm = x_norm / np.std(x_norm)
    else:
        x_mean = x.mean(axis=1)[:, np.newaxis]
        mu = np.mean(x - x_mean)
        x_norm = x - x_mean
        sigma = np.std(x / np.std(x_norm))
        x_norm = x_norm / np.std(x_norm)
    return x_norm, mu, sigma


if __name__ == '__main__':
    X = np.array([-10, -1, 0, 1, 10])
    X_norm, mu, sigma = feature_normalize(X)
    print(X_norm)
    print(mu)
    print(sigma)

    X = np.array([[-10, -4, -2, 10, 14], [ 2, 4, 6, 8, 10]])
    X_norm, mu, sigma = feature_normalize(X)
    print(X_norm)
    print(mu)
    print(sigma)

    # from sklearn.preprocessing import MinMaxScaler
    # mms = MinMaxScaler()
    # X_norm = mms.fit_transform(X)
