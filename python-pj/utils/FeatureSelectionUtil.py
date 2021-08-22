# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
from sklearn.feature_selection import SelectKBest, SelectPercentile, SelectFpr, SelectFdr, SelectFwe, RFECV, SelectFromModel, f_regression, f_classif
from sklearn.svm import SVR, SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LassoCV, LogisticRegressionCV

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
        """
        X     = model.fit_transform(X, y)
        score = model.scores_
        return X, score        

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
        """
        model = SelectKBest(f_regression, k = num)
        return FeatureSelectionUtil.__calc_score__(X, y, model)

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
        """
        model = SelectKBest(f_classif, k = num)
        return FeatureSelectionUtil.__calc_score__(X, y, model)
    
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
        """
        pst   = int(num / len(X[0]))
        model = SelectPercentile(f_regression, percentile = pst)
        return FeatureSelectionUtil.__calc_score__(X, y, model)
    
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
        """
        pst   = int(num / len(X[0]))
        model = SelectPercentile(f_classif, percentile = pst)
        return FeatureSelectionUtil.__calc_score__(X, y, model)
    
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
        """
        model = SelectFpr(SelectKBest(f_regression, k = num), alpha = 0.05)
        return FeatureSelectionUtil.__calc_score__(X, y, model)
    
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
        """
        model = SelectFpr(SelectKBest(f_classif, k = num), alpha = 0.05)
        return FeatureSelectionUtil.__calc_score__(X, y, model)
    
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
        """
        model = SelectFwe(SelectKBest(f_regression, k = num), alpha = 0.05)
        return FeatureSelectionUtil.__calc_score__(X, y, model)

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
        """
        model = SelectFwe(SelectKBest(f_classif, k = num), alpha = 0.05)
        return FeatureSelectionUtil.__calc_score__(X, y, model)

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
        """
        model = SelectFdr(SelectKBest(f_regression, k = num), alpha = 0.05)
        return FeatureSelectionUtil.__calc_score__(X, y, model)

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
        """
        model = SelectFdr(SelectKBest(f_classif, k = num), alpha = 0.05)
        return FeatureSelectionUtil.__calc_score__(X, y, model)

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
        """
        estimator = SVR(kernel = kernel)
        model     = RFECV(estimator, step = step, cv = cv)
        return FeatureSelectionUtil.__calc_score__(X, y, model)

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
        """
        clf = LassoCV(alphas=[0.001, 0.01, 0.1, 1.0, 10.0], cv = cv, max_iter = max_iter).fit(X, y)
        model = SelectFromModel(clf, prefit = True)
        X     = model.transform(X)
        score = model.get_support(True)
        return X, score

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
        """
        clf   = ExtraTreesClassifier().fit(X, y)
        model = SelectFromModel(clf, prefit = True)
        X     = model.transform(X)
        score = model.get_support(True)
        return X, score
    
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
        """
        clf   = LogisticRegressionCV(penalty = "l1", dual = False, cv = cv).fit(X, y)
        model = SelectFromModel(clf, prefit = True)
        X     = model.transform(X)
        score = model.get_support(True)
        return X, score
    
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
        """
        clf   = SVC(kernel = kernel).fit(X, y)
        model = SelectFromModel(clf, prefit = True)
        X     = model.transform(X)
        score = model.get_support(True)
        return X, score
