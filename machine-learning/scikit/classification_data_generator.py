# -*- coding: utf-8 -*-

import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


class ClassificationDataGenerator():

    @staticmethod
    def generate(
        n_samples,      # サンプル数
        n_features,     # 各サンプルの説明変数の数
        centers,        # 離散データのグループ数
        cluster_std,    # 離散データのバラけ具合(>0)
        random_state):  # 呼ぶたびにseedを変えずに固定

        X, y = make_blobs(
            n_samples = n_samples,
            n_features= n_features,
            centers = centers,
            cluster_std = cluster_std,
            random_state = random_state)

        return ClassificationDataGenerator.shuffle(X, y)

    @staticmethod
    def shuffle(X, y):
        rng = np.random.RandomState(0)
        permutation = rng.permutation(len(X))
        return X[permutation], y[permutation]



if __name__ == '__main__':
    X, y = ClassificationDataGenerator.generate(
            n_samples = 1000,
            n_features = 2,
            centers = 4,
            cluster_std = 1.5,
            random_state = 4)

    for label, s, c in zip(np.unique(y), ['o', '+', 'v', 'x'], ['b', 'g', 'r', 'c']):
        plt.scatter(X[y == label,0], X[y == label,1], marker=s, color=c)
    plt.show()

