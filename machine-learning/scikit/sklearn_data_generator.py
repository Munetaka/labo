# -*- coding: utf-8 -*-

import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)

class SklearnDataGenerator():
    type_list = {
        "iris": "load_iris_data",
        "boston": "load_boston",
        "diabetes": "load_diabetes",
        "digits": "load_digits",
        "linnerud": "load_linnerud",
    }

    @staticmethod
    def get_type_list():
        return SklearnDataGenerator.type_list.keys()

    @staticmethod
    def generate(type=None):

        if type == None:
            print('plz select data type')
            exit()
        elif type in SklearnDataGenerator.type_list:
            method_name = SklearnDataGenerator.type_list[type]
        else:
            print('undefined type: ' + type)
            exit()

        method = getattr(SklearnDataGenerator, method_name)
        return method()

    @staticmethod
    def load_iris_data():
        from sklearn.datasets import load_iris
        iris = load_iris()
        # print(iris.DESCR)

        # print(iris.target_names)
        # ['setosa' 'versicolor' 'virginica']

        # print(iris.feature_names)
        # sepal length (cm) : がく片の長さ
        # sepal width (cm)  : がく片の幅
        # petal length (cm) : 花弁の長さ
        # petal width (cm)  : 花弁の幅

        # pp.pprint(iris.data)
        # pp.pprint(iris.target) # target value means target_name
        X = np.array(iris.data)
        y = np.array(iris.target)
        return SklearnDataGenerator.shuffle(X, y)

    @staticmethod
    def load_boston():
        from sklearn.datasets import load_boston
        boston = load_boston()
        # print(boston.DESCR)

        # print(boston.feature_names)
        # CRIM      : 人口1人当たりの犯罪発生数
        # ZN        : 25,000 平方フィート以上の住居区画の占める割合
        # INDUS     : 小売業以外の商業が占める面積の割合
        # CHAS      : チャールズ川によるダミー変数 (1: 川の周辺, 0: それ以外)
        # NOX       : NOx の濃度
        # RM        : 住居の平均部屋数
        # AGE       : 1940 年より前に建てられた物件の割合
        # DIS       : 5 つのボストン市の雇用施設からの距離 (重み付け済)
        # RAD       : 環状高速道路へのアクセスしやすさ
        # TAX       : $10,000 ドルあたりの不動産税率の総計
        # PTRATIO   : 町毎の児童と教師の比率
        # B         : 町毎の黒人 (Bk) の比率を次の式で表したもの。 1000(Bk – 0.63)^2
        # LSTAT     : 給与の低い職業に従事する人口の割合 (%)

        # pp.pprint(boston.data)
        # print(np.array(boston.data).shape)
        # pp.pprint(boston.target) # house prices
        X = boston.data
        y = boston.target
        return SklearnDataGenerator.shuffle(X, y)

    @staticmethod
    def load_diabetes():
        from sklearn.datasets import load_diabetes
        diabetes = load_diabetes()

        # feature names
        # AGE
        # SEX
        # BMI (body mass index)
        # BP (blood pressure)
        # S1 S2 S3 S4 S5 S6 (six blood serum measurements)

        # pp.pprint(diabetes.target) # target means 1年後の疾患進行状況
        X = diabetes.data
        y = diabetes.target
        return SklearnDataGenerator.shuffle(X, y)

    @staticmethod
    def load_digits():
        from sklearn.datasets import load_digits
        digits = load_digits()
        print(digits.keys())

        # print(digits.DESCR)

        # print(digits.target_names)
        # [0 1 2 3 4 5 6 7 8 9]

        # print(np.array(digits.data[0]).reshape(8,8))
        # print(digits.images[0])
        # print(np.array(digits.data[0]).reshape(8,8) == digits.images[0])
        # digits.images is 8x8 matrix
        # digits.data is 1 line 64 (= 8x8) data

        X = digits.data
        y = digits.target
        return SklearnDataGenerator.shuffle(X, y)

    @staticmethod
    def load_linnerud():
        from sklearn.datasets import load_linnerud
        linnerud = load_linnerud()

        # print(linnerud.DESCR)

        print(linnerud.keys())

        # print(linnerud.feature_names)
        # Chins     : 懸垂の回数
        # Situps    : 腹筋の回数
        # Jumps     : 跳躍

        # print(linnerud.target_names)
        # ['Weight', 'Waist', 'Pulse']

        X = linnerud.data
        y = linnerud.target
        return SklearnDataGenerator.shuffle(X, y)

    @staticmethod
    def shuffle(X, y):
        rng = np.random.RandomState(0)
        permutation = rng.permutation(len(X))
        return X[permutation], y[permutation]

    @staticmethod
    def train_test_split(X, y):
        from sklearn.cross_validation import train_test_split
        train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.5, random_state=1999)
        return train_X, test_X, train_y, test_y

if __name__ == '__main__':
    generator = SklearnDataGenerator()
    X, y = generator.generate('iris')
    # X, y = generator.generate('boston')
    # X, y = generator.generate('diabetes')
    # X, y = generator.generate('digits')
    # X, y = generator.generate('linnerud')
    print(np.array(X).shape)
    print(np.array(y).shape)
