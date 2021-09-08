# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
from sklearn.feature_selection import SelectKBest, SelectPercentile, SelectFpr, SelectFdr, SelectFwe, RFECV, SelectFromModel, f_regression, f_classif
from sklearn.svm import SVR, SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LassoCV, LogisticRegressionCV
import logging
import traceback

class FeatureSelectionUtil:
    """
    特徴選択のUtilクラス
    """

    def __calc_score__(X, y, model):
        """
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        model: 
            モデル
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            X     = model.fit_transform(X, y)
            score = model.scores_
            return X, score
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("スコアの計算で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def k_best_for_regression(X, y, num):
        """
        method: Best
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectKBest(f_regression, k = num)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("k_best_for_regressionで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def k_best_for_classification(X, y, num):
        """
        method: Best
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectKBest(f_classif, k = num)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("k_best_for_classificationで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    
    @staticmethod
    def percentile_for_regression(X, y, num):
        """
        method: Percentile
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            pst   = int(num / len(X[0]))
            model = SelectPercentile(f_regression, percentile = pst)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("percentile_for_regressionで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    @staticmethod
    def percentile_for_classification(X, y, num):
        """
        method: Percentile
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            pst   = int(num / len(X[0]))
            model = SelectPercentile(f_classif, percentile = pst)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("percentile_for_classificationで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    @staticmethod
    def fpr_for_regression(X, y, num):
        """
        method: Fpr
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectFpr(SelectKBest(f_regression, k = num), alpha = 0.05)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("fpr_for_regressionで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
 
    @staticmethod
    def fpr_for_classification(X, y, num):
        """
        method: Fdr
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectFpr(SelectKBest(f_classif, k = num), alpha = 0.05)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("fpr_for_classificationで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def fwe_for_regression(X, y, num):
        """
        method: Fwe
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectFwe(SelectKBest(f_regression, k = num), alpha = 0.05)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("fwe_for_regressionで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def fwe_for_classification(X, y, num):
        """
        method: Fwe
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectFwe(SelectKBest(f_classif, k = num), alpha = 0.05)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("fwe_for_classificationで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def fdr_for_regression(X, y, num):
        """
        method: Fdr
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectFdr(SelectKBest(f_regression, k = num), alpha = 0.05)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("fdr_for_regressionで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def fdr_for_classification(X, y, num):
        """
        method: Fdr
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num: int
            特徴選択数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            model = SelectFdr(SelectKBest(f_classif, k = num), alpha = 0.05)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("fdr_for_classificationで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def rfecv(X, y, kernel, step, cv):
        """
        method: RFECV
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        kernel: string, {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf'
            カーネルタイプ
        step: int
            ステップ数
        cv: int
            Cross-Validation数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            estimator = SVR(kernel = kernel)
            model     = RFECV(estimator, step = step, cv = cv)
            return FeatureSelectionUtil.__calc_score__(X, y, model)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("rfecvで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def select_from_lasso(X, y, cv, max_iter):
        """
        method: SelectFromLasso
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        cv: int
            Cross-Validation数
        max_iter: int
            最大繰り返し数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            clf = LassoCV(alphas=[0.001, 0.01, 0.1, 1.0, 10.0], cv = cv, max_iter = max_iter).fit(X, y)
            model = SelectFromModel(clf, prefit = True)
            X     = model.transform(X)
            score = model.get_support(True)
            return X, score
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("select_from_lassoで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def select_from_decision_tree(X, y):
        """
        method: SelectFromDecisionTree
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            clf   = ExtraTreesClassifier().fit(X, y)
            model = SelectFromModel(clf, prefit = True)
            X     = model.transform(X)
            score = model.get_support(True)
            return X, score
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("select_from_decision_treeで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    @staticmethod
    def select_from_logistic_regression(X, y, cv):
        """
        method: SelectFromLogisticRegression
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        cv: int
            Cross-Validation数
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            clf   = LogisticRegressionCV(penalty = "l1", dual = False, cv = cv).fit(X, y)
            model = SelectFromModel(clf, prefit = True)
            X     = model.transform(X)
            score = model.get_support(True)
            return X, score
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("select_from_logistic_regressionで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    @staticmethod
    def select_from_svc(X, y, kernel):
        """
        method: SelectFromSVC
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        kernel: string, {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf'
            カーネルタイプ
        
        Returns
        ----------
        X: ndarray
            特徴選択後の説明変数
        score: float
            スコア
            
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            clf   = SVC(kernel = kernel).fit(X, y)
            model = SelectFromModel(clf, prefit = True)
            X     = model.transform(X)
            score = model.get_support(True)
            return X, score
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("select_from_svcで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
