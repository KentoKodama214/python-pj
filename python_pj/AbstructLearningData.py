#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from sklearn.model_selection import train_test_split
from utils import NumpyUtil
from abc import abstractclassmethod
import numpy as np
import itertools as it
import logging
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

    def imputation(self, strategy):
        """
        列ごとに欠損値に対して方法を指定して補完する
        
        Parameters
        ----------
        strategy: string
            mean: 平均値   median:中央値  most_frequent:最頻出値
            補完方法。以下のURLを参照
            http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html

        """
        self.__X = NumpyUtil.NumpyUtil().imputation(self.__X, strategy)

    def split(self, rate):
        """
        学習データとテストデータに分割する
        
        Parameters
        ----------
        rate: float
            trainとtestの比率

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(self.__X, self.__y, test_size = rate, random_state = 0)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("学習データとテストデータに分割する際に予期しない例外が発生しました。")
            traceback.print_exc()
        
    def combine_features(self, dimension):
        """
        説明変数の組合せ列を追加した行列を生成する
        
        Parameters
        ----------
        dimension: int
            組合せの次数
        """
        self.__X, self.__features_name = NumpyUtil.NumpyUtil().combination_cols(self.__X, self.__features_name, dimension)
