from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, LarsCV, LassoLarsCV, BayesianRidge
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.metrics import explained_variance_score, mean_squared_error
import numpy as np
import traceback

class RegressionUtil:
    """
    機械学習の回帰モデルのUtilクラス
    """
    
    def __mean_squared_error__(y, y_pred):
        """
        平均二条誤差(mean squared error)を計算する
        
        Parameters
        ----------
        y: ndarray
            目的変数の実測値
        y_pred: ndarray
            目的変数の予測値
        
        Returns
        ----------
        mean_squared_error: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            return mean_squared_error(y_pred, y)
        except ValueError:
            print("mean_squared_errorを計算中に例外が発生しました。")
            traceback.print_exc()
    
    def __explained_variance_score__(y, y_pred):
        """
        説明変数回帰スコア(explained variance score)を計算する
        
        Parameters
        ----------
        y: ndarray
            目的変数の実測値
        y_pred: ndarray
            目的変数の予測値
        
        Returns
        ----------
        explained_variance_score: float
            説明変数回帰スコア

        Raises
        ----------
        ValueError
            TODO
        """
        
        try:
            return explained_variance_score(y_pred, y, multioutput = 'variance_weighted')
        except ValueError:
            print("explained_variance_scoreを計算中に例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_ordinary_least_square(X, y):
        """
        OLS
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """
        
        try:
            ols   = LinearRegression().fit(X, y)
            coef  = ols.coef_
            score = ols.score(X, y)
            evs   = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse   = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("OLSで例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_ridge_regression(X, y, num_cv = 10):
        """
        リッジ回帰
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num_cv: int
            Cross-Validation数。デフォルト値=10
        
        Returns
        ----------        
        coef: ndarray
            係数
        score: float
            スコア
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            rr    = RidgeCV(alphas = [0.001, 0.01, 0.1, 1.0, 10.0], cv = num_cv).fit(X, y)
            coef  = rr.coef_
            score = rr.score(X, y)
            evs   = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse   = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("リッジ回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_linear_regression(X, y, num_cv = 10):
        """
        線形回帰
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num_cv: int
            Cross-Validation数。デフォルト値=10
        
        Returns
        ----------        
        coef: ndarray
            係数
        score: float
            スコア
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            lr    = LassoCV(alphas = [0.001, 0.01, 0.1, 1.0, 10.0], cv = num_cv, max_iter = 50).fit(X, y)
            coef  = lr.coef_
            score = lr.score(X, y)
            evs   = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse   = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("線形回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_lars(X, y, num_cv = 10):
        """
        LARS
        
        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num_cv: int
            Cross-Validation数。デフォルト値=10
        
        Returns
        ----------        
        coef: ndarray
            係数
        score: float
            スコア
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            lars  = LarsCV(cv = num_cv, max_iter = 10).fit(X, y)
            coef  = lars.coef_
            score = lars.score(X, y)
            evs   = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse   = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("LARSで例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_llars(X, y, num_cv = 10):
        """
        LLARS

        Parameters
        ----------
        X: ndarray
            説明変数
        y: ndarray
            目的変数
        num_cv: int
            Cross-Validation数。デフォルト値=10
        
        Returns
        ----------        
        coef: ndarray
            係数
        score: float
            スコア
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            llars = LassoLarsCV(cv = num_cv, max_iter = 10).fit(X, y)
            coef  = llars.coef_
            score = llars.score(X, y)
            evs   = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse   = RegressionUtil.__mean_squared_error__(np.dot(X, llars.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("LLARSで例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_kernel_ridge_regression(X, y):
        """
        カーネルリッジ回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            alphas     = [0.001, 0.01, 0.1, 1, 10]
            score      = 0.0
            best_alpha = 0.0
            for alpha in alphas:
                krr = KernelRidge(alpha = alpha, degree = 1).fit(X, y)
                if(score < krr.score(X, y)):
                    score      = krr.score(X, y)
                    coef       = np.dot(X.transpose(), krr.dual_coef_)
                    evs        = RegressionUtil.__explained_variance_score__(np.dot(X, coef), y)
                    mse        = RegressionUtil.__mean_squared_error__(np.dot(X, coef), y)
                    best_alpha = alpha
            return coef, score, evs, mse
        except ValueError:
            print("カーネルリッジ回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_bayesian_ridge_regression(X, y):
        """
        ベイジアンリッジ回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            br  = BayesianRidge().fit(X, y)
            coef  = br.coef_
            score = br.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("ベイジアンリッジ回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_support_vector_regression(X, y):
        """
        サポートベクター回帰

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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            svr = SVR(degree = 1, kernel = 'linear').fit(X, y)
            coef  = svr.coef_
            score = svr.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("サポートベクター回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_gaussian_process(X, y):
        """
        ガウス過程回帰

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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            gp  = GaussianProcessRegressor(theta0 = 1e-2, thetaL = 1e-4, thetaU = 1e-1).fit(X, y)
            coef  = gp.coef_
            score = gp.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("ガウス過程回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_decision_tree_regressor(X, y):
        """
        決定木回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            dtr = DecisionTreeRegressor(random_state = 0).fit(X, y)
            coef = dtr.feature_importances_
            score = dtr.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("決定木回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_extra_tree_regressor(X, y):
        """
        エクストラツリー回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            etr = ExtraTreesRegressor(n_estimators = 10, bootstrap = True).fit(X, y)
            coef = etr.feature_importances_
            score = etr.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("エクストラツリー回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_random_forest_regressor(X, y):
        """
        ランダムフォレスト回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            rfr = RandomForestRegressor(n_estimators = 10, bootstrap = True).fit(X, y)
            coef = rfr.feature_importances_
            score = rfr.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("ランダムフォレスト回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_k_nearest_neighbors_regressor(X, y):
        """
        K-NN回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            knnr = KNeighborsRegressor(n_neighbors = 2).fit(X, y)
            coef = knnr.feature_importances_
            score = knnr.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("K-NN回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_radius_neighbors_regressor(X, y):
        """
        Radius Neighbor回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            rnnr = RadiusNeighborsRegressor(radius = 1.0).fit(X, y)
            coef = rnnr.feature_importances_
            score = rnnr.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("Radius Neighbor回帰で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def exec_gradient_boosting_regressor(X, y):
        """
        勾配ブースティング回帰
        
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
        evs: float
            説明変数回帰スコア
        mse: float
            平均二条誤差

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            gbr = GradientBoostingRegressor(n_estimators = 100, learning_rate = 1.0, max_depth = 1, random_state = 0).fit(X, y)
            coef = gbr.feature_importances_
            score = gbr.score(X, y)
            evs = RegressionUtil.__explained_variance_score__(np.dot(X, coef.transpose()), y)
            mse = RegressionUtil.__mean_squared_error__(np.dot(X, coef.transpose()), y)
            return coef, score, evs, mse
        except ValueError:
            print("勾配ブースティング回帰で例外が発生しました。")
            traceback.print_exc()
