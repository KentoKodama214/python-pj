#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from abc import abstractclassmethod
import numpy as np
import itertools as it
import traceback

class AbstructLearningData:
    """
    機械学習データの抽象クラス
    
    Attributes
    ----------
    __X: ndarray
        説明変数
    __X_train: ndarray
        学習データの説明変数
    __X_test: ndarray
        テストデータの説明変数
    __y: ndarray
        目的変数
    __y_train: ndarray
        学習データの目的変数
    __y_test: ndarray
        テストデータの目的変数
    __features_name: ndarray
        説明変数の名称のベクトル
    """
    
    def __init__(self, X, y):
        """
        コンストラクタ
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        """
        self.__X = X
        self.__y = y
        self.__features_name = []

    @abstractclassmethod
    def learning(self):
        """
        学習の抽象publicメソッド
        """
        pass

    def imputation(self, st):
        """
        列ごとに欠損値に対して方法を指定して補完する
        
        Parameters
        ----------
        st: string
            補完方法。以下のURLを参照
            http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            imp = Imputer(missing_values = 'NaN', strategy = st, axis = 0)
            imp.fit(self.__X)
            self.__X = imp.transform(self.__X)
        except ValueError:
            print("列ごとに欠損値に対して方法を指定して補完する際に例外が発生しました。")
            traceback.print_exc()

    def split(self, rate):
        """
        学習データとテストデータに分割する
        
        Parameters
        ----------
        rate: float
            trainとtestの比率

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(self.__X, self.__y, test_size = rate, random_state = 0)
        except ValueError:
            print("学習データとテストデータに分割する際に例外が発生しました。")
            traceback.print_exc()
        
    def combine_features(self, d):
        """
        説明変数の組合せ列を追加した行列を生成する
        
        Parameters
        ----------
        d: int
            組合せの次数

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            n = len(self.__X)
            p = len(self.__X[0])
            col_num = np.array(range(0, p))
    
            for i in range(2, d+1):
                comb = np.array(list(it.combinations_with_replacement(col_num, i)))
                for j in range(0, len(comb)):
                    x   = np.ones(n)
                    str = ""
                    for k in range(0, i):
                        num = comb[j, k]
                        x   = x * self.__X[:, comb[j, k]]
                        if(k != 0):
                            str = str + "x" + self.__features_name[num]
                        else:
                            str = self.__features_name[num]
                    self.__X = np.hstack((self.__X, x.reshape(n, 1)))
                    self.__features_name = np.append(self.__features_name, str)
        except ValueError:
            print("説明変数の組合せ列を追加した行列を生成する際に例外が発生しました。")
            traceback.print_exc()
