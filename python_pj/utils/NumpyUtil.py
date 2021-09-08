import numpy as np
import traceback
import itertools as it
from sklearn.preprocessing import Imputer
import logging

class NumpyUtil:
    """
    NumpyのUtilクラス
    """

    @staticmethod
    def slice_cols(numpy_data, col_num):
        """
        行列を1列sliceする
        
        Parameters
        ----------
        numpy_data: ndarray
            numpyデータ
        col_num: int
            列番号
        
        Returns
        ----------
        X: ndarray
            col_numを削除したnumpyデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if col_num == 0:
                X = numpy_data[:, 1:].copy()
            else:
                X = np.hstack((numpy_data[:, 0:col_num], numpy_data[:, col_num + 1:])).copy()
            return X
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("行列のslice中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def delete_imputed_y(X, y):
        """
        目的変数が欠損している行を削除する
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        
        Returns
        ----------
        X: ndarray
            欠損データを取り除いた説明変数
        y: ndarray
            欠損データを取り除いた目的変数

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            index = ~np.isnan(y[:, 0])
            X = X[index, :].copy()
            y = y[index, 0:1].copy()
            return X, y
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("目的変数が欠損しているデータの削除で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def check_cols_and_delete(X, nan_rate=0.5):
        """
        欠損値が多い列を削除する
        
        Parameters
        ----------
        X: ndarray
            説明変数
        nan_rate: float, default 0.5
            列を削除するための欠損値の下限
        
        Returns
        ----------
        X: ndarray
            欠損値が多い列を取り除いた説明変数

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            rows = np.size(X, axis=0)
            cols = np.size(X, axis=1)
            x = None
            if nan_rate >= 1.0:
                return
            else:
                for col_num in range(0, cols):
                    non_nan_count = np.count_nonzero(~np.isnan(X[:, col_num]))
                    if non_nan_count/rows > nan_rate:
                        if x is None:
                            x = X[:, col_num].reshape(rows, 1)
                        else:
                            x = np.hstack((x, X[:, col_num].reshape(rows, 1))).copy()

                X = x.copy()
            return X
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("欠損値が多い列の削除で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def imputation(X, strategy='mean'):
        """
        scikit-learnのImputerでnumpy欠損値を保管する
        
        Parameters
        ----------
        strategy: string, default mean
            mean: 平均値   median:中央値  most_frequent:最頻出値
            補完方法。以下のURLを参照
                http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html
        
        Returns
        ----------
        X: ndarray
            欠損値が多い列を取り除いた説明変数
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            imp = Imputer(missing_values='NaN', strategy=strategy, axis=0)
            imp.fit(X)
            X = imp.transform(X)
            return X
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("scikit-learnのImputerで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def combination_cols(X, features_name, dimension):
        """
        n次元の組合せ列の追加
        
        Parameters
        ----------
        X: ndarray
            説明変数
        features_name: ndarray
            説明変数の名称のベクトル
        dimension: int
            組合せの次元
        
        Returns
        ----------
        X: ndarray
            組合せを追加した説明変数
        features_name: ndarray
            組合せを追加した説明変数の名称のベクトル
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            n = len(X)
            p = len(X[0])
            col_num = np.array(range(0, p))
    
            for i in range(2, dimension+1):
                comb = np.array(list(it.combinations_with_replacement(col_num, i)))
                for j in range(0, len(comb)):
                    x   = np.ones(n)
                    str = ""
                    for k in range(0, i):
                        num = comb[j, k]
                        x   = x * X[:, comb[j, k]]
                        if(k != 0):
                            str = str + "x" + features_name[num]
                        else:
                            str = features_name[num]
                    X = np.hstack((X, x.reshape(n, 1)))
                    features_name = np.append(features_name, str)
            return X, features_name
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("n次元の組合せ列の追加で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def normalize(X):
        """
        正規化

        Parameters
        ----------
        X: ndarray
            説明変数

        Returns
        ----------
        X: ndarray
            正規化した説明変数
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            for i in range(0, len(X[0])):
                mean = np.mean(X[:, i])
                var = np.std(X[:, i])
                X[:, i] = (X[:, i] - mean)/var
            return X
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("正規化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
