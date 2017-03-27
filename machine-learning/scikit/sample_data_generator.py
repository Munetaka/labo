# -*- coding: utf-8 -*-

import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt


"""
パラメータ名    説明
n_samples               生成するサンプルの数。
n_features              生成する特徴量の数。
n_informative           目的変数のラベルと相関が強い特徴量(Informative fearture)の数。
n_redundant             Informative featureの線形結合から作られる特徴量(Redundant fearture)の数。
n_repeated              Infomative、Redundant featureのコピーからなる特長量の数(Repeated feature)。
n_classes               分類するクラス数。2なら2値分類問題、3以上なら多値分類問題のデータが作られる。
n_clusters_per_class    1クラスあたりのクラスタ数。後述する生成アルゴリズムを参照。
weights                 クラスの比率。不均衡データを作りたい場合に指定する。例えば、2値分類問題の場合、Noneとすると0と1が50%ずつだが、[0.9, 0.1] と与えると0が90%、1が10%になる。
flip_y                  クラスのフリップ率。例えば0.01とすると各クラスの1%の符号がランダムに変更される。
class_sep               生成アルゴリズムに関係するパラメータ。後述する生成アルゴリズムにおける超立法体の頂点の距離。
hypercube               生成アルゴリズムに関係するパラメータ。Trueにすると後述する生成アルゴリズムにおいて、超立方体の頂点にクラスタを配置する。
shift                   全ての特徴量にshiftを加算する。Noneが指定された場合、[-class_sep, class_sep]の一様乱数を加算する。
scale                   全ての特徴量にscaleを乗算する。Noneが指定された場合、 [1, 100]の一様乱数を乗算する。(scaleはshift後に行われる)
shuffle                 Trueにすると行と列をシャッフルする。
random_state            乱数を制御するパラメータ。Noneにすると毎回違うデータが生成されが、整数をシードとして渡すと毎回同じデータが生成される。乱数オブジェクトを渡すことも可能。
"""

def make_sample_data():
    data = make_classification(
            n_samples               = 100,
            n_features              = 2,
            n_informative           = 2,
            n_redundant             = 0,
            n_repeated              = 0,
            n_classes               = 2,
            n_clusters_per_class    = 1,
            weights                 = None,
            flip_y                  = 0,
            class_sep               = 0,
            hypercube               = False,
            shift                   = 0,
            scale                   = 1,
            shuffle                 = True,
            random_state            = True)
    X = data[0]
    y = data[1]
    return X, y

if __name__ == '__main__':
    X, y = make_sample_data()
    for label, s, c in zip(np.unique(y), ['o', '+'], ['b', 'g']):
        plt.scatter(X[y == label,0], X[y == label,1], marker=s, color=c)
    plt.show()
