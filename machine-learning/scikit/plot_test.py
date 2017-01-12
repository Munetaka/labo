# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from classification_data_generator import ClassificationDataGenerator

X, y = ClassificationDataGenerator.generate(
            n_samples = 1000,
            n_features = 2,
            centers = 4,
            cluster_std = 1.5,
            random_state = 4)

# zip([0, 1, 2], ['o', '+', 'x'])
for label, s, c in zip(np.unique(y), ['o', '+', 'v', 'x'], ['b', 'g', 'r', 'c']):
    plt.scatter(X[y == label,0], X[y == label,1], marker=s, color=c)

plt.show()
