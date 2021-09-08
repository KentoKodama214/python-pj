from sklearn.linear_model import LogisticRegressionCV
from sklearn.svm import SVC, NuSVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.neighbors._nearest_centroid import NearestCentroid
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score, explained_variance_score
import logging
import traceback

class ClassificationUtil:
    """
    機械学習の分類モデルのUtilクラス
    """
    
    def __classification_scores__(y, y_pred):
        """
        分類問題における各種スコアを計算する
        
        Parameters
        ----------
        y: ndarray
            目的変数の実測値
        y_pred: ndarray
            目的変数の予測値
            
        Returns
        ----------
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            confmat            = confusion_matrix(y, y_pred)
            precision          = precision_score(y, y_pred)
            recall             = recall_score(y, y_pred, average = 'macro')
            f1                 = f1_score(y, y_pred, average = 'macro')
            roc_auc            = roc_auc_score(y, y_pred, average = 'macro')
            explained_variance = explained_variance_score(y_pred, y)
            return confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("分類問題における各種スコアを計算する際に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    @staticmethod
    def exec_logistic_regression(X, y, num_cv):
        """
        ロジスティック回帰
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            logistic = LogisticRegressionCV(cv = num_cv, penalty = 'l2').fit(X, y)
            coef  = logistic.coef_
            score = logistic.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, logistic.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("ロジスティック回帰で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_lda(X, y):
        """
        LDA
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            lda = LinearDiscriminantAnalysis().fit(X, y)
            coef  = lda.coef_
            score = lda.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, lda.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("LDAで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_support_vector_classifier(X, y):
        """
        サポートベクター分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            svc = SVC(kernel = 'linear').fit(X, y)
            coef  = svc.coef_
            score = svc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, svc.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("サポートベクター分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_nu_support_vector_classifier(X, y):
        """
        Nuサポートベクター分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            nusvc = NuSVC(kernel = 'linear').fit(X, y)
            coef  = nusvc.coef_
            score = nusvc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, nusvc.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("Nuサポートベクター分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_k_nearest_neighbor_classifier(X, y):
        """
        k-NN分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            knnc = KNeighborsClassifier(n_neighbors = 2).fit(X, y)
            score = knnc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, knnc.predict(X))
            return None, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("k-NN分類で例外が予期しない発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_radius_nearest_neighbor_classifier(X, y):
        """
        Radius-Neighbor分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            rnnc = RadiusNeighborsClassifier(radius = 1.0).fit(X, y)
            score = rnnc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, rnnc.predict(X))
            return None, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("Radius-Neighbor分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_nearest_centroid(X, y):
        """
        Nearest-Centroid
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            nc = NearestCentroid().fit(X, y)
            score = nc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, nc.predict(X))
            return None, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("Nearest-Centroidで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_gaussian_naive_bayes(X, y):
        """
        ガウシアンナイーブベイズ
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            gnb = GaussianNB().fit(X, y)
            score = gnb.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, gnb.predict(X))
            return None, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("ガウシアンナイーブベイズで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_bernoulli_naive_bayes(X, y):
        """
        ベルヌーイナイーブベイズ
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            bnb = BernoulliNB().fit(X, y)
            coef  = bnb.coef_
            score = bnb.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, bnb.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("ベルヌーイナイーブベイズで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_decision_tree_classifier(X, y):
        """
        決定木分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            dtc = DecisionTreeClassifier(random_state = 0).fit(X, y)
            coef  = dtc.feature_importances_
            score = dtc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, dtc.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("決定木分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_extra_tree_classifier(X, y):
        """
        Extra決定木分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            etc = ExtraTreesClassifier(n_estimators = 10).fit(X, y)
            coef  = etc.feature_importances_
            score = etc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, etc.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("Extra決定木分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_random_forest_classifier(X, y):
        """
        ランダムフォレスト分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            rfc = RandomForestClassifier(n_estimators = 10).fit(X, y)
            coef  = rfc.feature_importances_
            score = rfc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, rfc.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("ランダムフォレスト分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_adaboost_classifier(X, y):
        """
        AdaBoost分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            adac = AdaBoostClassifier(n_estimators = 10).fit(X, y)
            coef  = adac.feature_importances_
            score = adac.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, adac.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("AdaBoost分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def exec_gradient_boosting_classifier(X, y):
        """
        勾配ブースティング分類
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
            
        Returns
        ----------
        coef: ndarray
            係数
        score: float
            スコア
        confmat: ndarray of shape (n_classes, n_classes)
            confusion matrix
        precision: float (if average is not None) or array of float of shape
            適合率
        recall: float (if average is not None) or array of float of shape
            再現率
        f1: float or array of float, shape = [n_unique_labels]
            F値
        roc_auc: float
            ROC-AUCスコア
        explained_variance: float or ndarray of floats
            説明変数分類スコア

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            gbc = GradientBoostingClassifier(n_estimators = 100, learning_rate = 1.0, max_depth = 1, random_state = 0).fit(X, y)
            coef  = gbc.feature_importances_
            score = gbc.score(X, y)
            confmat, precision, recall, f1, roc_auc, explained_variance = ClassificationUtil.__classification_scores__(y, gbc.predict(X))
            return coef, score, confmat, precision, recall, f1, roc_auc, explained_variance
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("勾配ブースティング分類で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
