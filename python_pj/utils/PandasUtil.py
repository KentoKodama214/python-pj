import pandas as pd
import traceback
import StringUtil
import DateUtil
import logging


class PandasUtil:
    """
    PandasのUtilクラス
    """

    @staticmethod
    def slice_cols(pandas_data, col_num):
        """
        行列を1列sliceする
 
        Parameters
        ----------
        pandas_data: DataFrame
            pandasデータ
        col_num: int
            列番号
        
        Returns
        ----------
        X: DataFrame
            col_numを削除したpandasデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            rows, cols = pandas_data.shape
            if col_num == 0:
                X = pandas_data.iloc[range(0, rows), range(1, cols)]
                X = X.reset_index(drop=True)
            else:
                x1 = pandas_data.iloc[range(0, rows), range(0, col_num)]
                x2 = pandas_data.iloc[range(0, rows), range(col_num + 1, cols)]
                X = pd.concat([x1, x2], axis=1)
            return X
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("行列のslice中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def delete_imputed_y(X, y, col_num):
        """
        目的変数yが欠損しているデータは削除する
        Parameters
        ----------
        X: DataFrame
            説明変数
        y: DataFrame
            目的変数
        col_num: int
            列番号

        Returns
        ----------
        X: DataFrame
            欠損データを取り除いた説明変数
        y: DataFrame
            欠損データを取り除いた目的変数

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            y_tmp = y.isnull().reset_index()
            index = y_tmp[y_tmp[col_num] != True].index.tolist()
            X = X.iloc[index, :]
            X = X.reset_index(drop=True)
            y = y.iloc[index, :]
            y = y.reset_index(drop=True)
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
        X: DataFrame
            説明変数
        nan_rate: float, default 0.5
            列を削除するための欠損値の下限
        
        Returns
        ----------
        X: DataFrame
            欠損値が多い列を取り除いた説明変数

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            rows = len(X)
            if nan_rate >= 1.0:
                return
            else:
                for col_num in range(len(X.columns), 0, -1):
                    non_nan_count = X.iloc[:, col_num-1].isnull().sum()
                    if non_nan_count/rows > nan_rate:
                        X = X.drop(col_num, axis=1)
            return X
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("欠損値が多い列の削除で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def check_cols_and_convert(X):
        """
        各列のデータ型からデータを変換
        
        Parameters
        ----------
        X: DataFrame
            データ型の変換前のpandasデータ
        
        Returns
        ----------
        X: DataFrame
            データ型の変換後のpandasデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            x_after = pd.DataFrame()
            for col_num in range(0, len(X.columns)):
                string_type = []
                data_type = X.iloc[:, col_num].dtype
                if data_type == 'object':
                    # 列ごとにデータ型（日付型文字列、その他文字列）をチェック
                    for row_num in range(0, len(X)):
                        if X.iloc[row_num, col_num] == X.iloc[row_num, col_num]:
                            string_type.append(StringUtil.MyStringUtil().check_string_type(str(X.iloc[row_num, col_num])))

                    if all([x == "date" for x in string_type]):
                        # 日付型のデータを変換
                        df_new = pd.DataFrame(columns=['spring', 'summer', 'autumn', 'winter', 'moon_age', 'weekday'])
                        for row_num in range(0, len(X)):
                            if X.iloc[row_num, col_num] == X.iloc[row_num, col_num]:
                                dt = StringUtil.StringUtil().extract_date(str(X.iloc[row_num, col_num]))
                                x_col = [DateUtil.DateUtil().month_to_spring_by_sin(dt['month']),
                                         DateUtil.DateUtil().month_to_summer_by_sin(dt['month']),
                                         DateUtil.DateUtil().month_to_autumn_by_sin(dt['month']),
                                         DateUtil.DateUtil().month_to_winter_by_sin(dt['month']),
                                         DateUtil.DateUtil().date_to_moon_age(dt['year'], dt['month'], dt['day']),
                                         StringUtil.StringUtil().extract_weekday(str(X.iloc[row_num, col_num]))
                                         ]
                            else:
                                x_col = [0, 0, 0, 0, 0, None]

                            df_1 = pd.Series(x_col, index=['spring', 'summer', 'autumn',
                                                           'winter', 'moon_age', 'weekday'])
                            df_new = df_new.append(df_1, ignore_index=True)

                        df_weekday = pd.get_dummies(df_new['weekday'])
                        df_new = df_new.drop(columns='weekday')
                        df_new = pd.concat([df_new, df_weekday], axis=1)
                    else:
                        # その他の文字列をone-hot-encodingで変換
                        df_new = pd.get_dummies(X.iloc[:, col_num])
                        # 文字列を形態素解析し、追加 (TODO)
                        #features = []
                        #for row_num in range(0, len(X)):
                        #    if X.iloc[row_num, col_num] == X.iloc[row_num, col_num]:
                        #        norns = MyStringUtil.MyStringUtil.\
                        #            morphological_analysis_by_mecab(str(X.iloc[row_num, col_num]))
                        #        print(norns)
                        #        # TODO 重複排除してlistに追加
                        #        features.append(norns)
                        #print(features)
                        # TODO 名詞を持っていれば1、なければ0をつける
                else:
                    df_new = X.iloc[:, col_num]

                x_after = pd.concat([x_after, df_new], axis=1)
            X = x_after
            return X
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("各列のデータ型からデータを変換中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def interpolate(X, limit=None, limit_direction='forward', limit_area=None, method='linear'):
        """
        interpolateで欠損値を補完する

        Parameters
        ----------
        limit: int
            補間する連続欠損値の最大数
        limit_direction: string, default 'forward'
            'forward', 'backward', 'both'のいずれかの補間方向
        limit_area: string
            'inside', 'outside'のいずれかの補間対象領域
        method: string, default 'linear'
            補間方法。詳しくは公式ドキュメントを参照

        Returns
        ----------
        X: DataFrame
            欠損値を補完した後の説明変数
        """

        return X.interpolate(limit=limit, limit_direction=limit_direction, limit_area=limit_area, inplace=True, method=method)

    @staticmethod
    def combination_cols(X, dimension):
        """
        n次元の組合せ列の追加
        
        Parameters
        ----------
        X: DataFrame
            説明変数
        dimension: int
            組合せの次元
        
        Returns
        ----------
        X: DataFrame
            組合せを追加した説明変数
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            # TODO
            print()
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
        X: DataFrame
            説明変数

        Returns
        ----------
        X: DataFrame
            正規化した説明変数
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            # TODO
            print()
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("正規化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
