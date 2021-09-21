#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import AbstructAnalysisData
import settings
import logging
import pymysql.cursors
import pandas as pd
import datetime
import traceback
from utils import PlotUtil

class AnalysisData(AbstructAnalysisData.AbstructAnalysisData):
    """
    分析データの実体クラス
    """

    def __load__(self):
        """
        データ読込のprivateメソッド
        コンストラクタでのみ呼び出す
        
        Attributes
        ----------
        __data: DataFrame/ndarray
            分析データ
        __countries: DataFrame/ndarray
            国名・地域データ
            
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            conn = pymysql.connect(host=settings.HOST,
                    user=settings.USER,
                    db=settings.DB,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
            with conn.cursor() as cursor:
                cursor.execute(settings.SELECT_ANALYSIS_DATA)
                results = cursor.fetchall()
                self.__data = pd.DataFrame(results)
                
                cursor.execute(settings.SELECT_COUNTRY_VIEW)
                results = cursor.fetchall()
                self.__countries = pd.DataFrame(results)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("データの読込で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
        finally:
            conn.close()
   
    def __extruct_top_n__(self, target_list, target, year, top_n):
        """
        対象データがある年で上位N位の国のデータを抽出する
        
        Parameters
        ----------
        target_list: list
            対象データのカラム名のリスト
        target: string
            対象データのうち、上位N位を判定するカラム
        year: int
            上位N位を判定する年
        top_n: int
            上位N位まで抽出する
        
        Returns
        ----------
        top_n_df: DataFrame
            対象年で上位N位の国のデータ
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            countries = self.__countries[self.__countries['LocID']<900]['Country'].values.tolist()
            df = self.__data[['Country', 'Year'] + target_list]
            df_by_country = df[df['Country'].isin(countries)]
            top_n_countries = df_by_country[df_by_country['Year']==year].sort_values(by=target, ascending=False).head(top_n)['Country'].values.tolist()
            return df_by_country[df_by_country['Country'].isin(top_n_countries)].dropna(subset=target_list, how='all')
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("対象データがある年で上位N位の国のデータの抽出で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def __extruct_countries__(self, target_list, countries):
        """
        対象データがある年で指定した国のデータを抽出する
        
        Parameters
        ----------
        target_list: list
            対象データのカラム名のリスト
        countries: list
            抽出する国名のリスト

        Returns
        ----------
        top_n_df: DataFrame
            対象年で上位N位の国のデータ
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            df = self.__data[['Country', 'Year'] + target_list]
            df_by_country = df[df['Country'].isin(countries)]
            return df_by_country[df_by_country['Country'].isin(countries)].dropna(subset=target_list, how='all')
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("対象データがある年で指定した国のデータの抽出で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def __extruct_for_world_map__(self, target):
        """
        対象データを抽出する
        
        Parameters
        ----------
        target: string
            抽出対象のデータ
        
        Returns
        ----------
        df: DataFrame
            抽出したデータ
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            countries = self.__countries[self.__countries['LocID']<900]['Country'].values.tolist()
            df = self.__data[['Country', 'Year', target]]
            df_by_country = df[df['Country'].isin(countries)]
            return df_by_country.set_index('Year')
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("対象データを抽出で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def __convert_for_matplitlib__(self, df, target):
        """
        MatplotlibのプロットのDataへ変換する
        
        Parameters
        ----------
        df: DataFrame
            pandasのDataFrameデータ
        target: string
            対象データ
        
        Returns
        ----------
        year_list: list
            年のリスト
        target_list: list
            対象データのリスト
        coutry_list: list
            国名のリスト
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = []
            year_list = []
            coutry_list = []
            
            for country in set(df['Country'].values.tolist()):
                df_of_country = df[df['Country']==country]
                coutry_list.append(country)
                year_list.append(df_of_country['Year'].values.tolist())
                target_list.append(df_of_country[target].values.tolist())
            
            return year_list, target_list, coutry_list
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("対象データを抽出で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
   
    def __convert_for_seaborn__(self, df):
        """
        seabornのプロットのDataFrameへ変換する
        
        Parameters
        ----------
        df: DataFrame
            pandasのDataFrameデータ
        
        Returns
        ----------
        converted_data: DataFrame
            pandasのDataFrameデータ
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            data = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
            coutry_list = []
            for country in set(df['Country'].values.tolist()):
                coutry_list.append(country)
                country_df = df[df['Country']==country]
                df_by_year = country_df.set_index('Year')
                seaborn_df = df_by_year.set_axis(['Country', country], axis=1)[country]
                data = data.append(seaborn_df)
            return data.T
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("seabornのプロットのDataFrameへ変換する際に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def __plot_line__(self, df, target_dict, mode="plotly", title="プロット", filepath=settings.OUTPUT_PATH+"filename"):
        """
        年単位での各国のデータの推移をプロットするprivateメソッド
        
        Parameters
        ----------
        df: DataFrame
            プロット対象のデータ
        target_dict: dictionary
            対象データとラベル名の辞書
        mode: string, default plotly
            プロットのモード（plotly / seaborn / matplotlib）
        title: string
            グラフのタイトル
        filepath: string
            ファイルパス（拡張子は除く）
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = list(target_dict.keys())
            label_list = list(target_dict.values())
            target_x = target_list[0]
            target_y = target_list[1]
            x_label = label_list[0]
            y_label = label_list[1]

            if(mode=="plotly"):
                PlotUtil.PlotlyUtil().plot_line(
                    df,
                    title,
                    target_x,
                    target_y,
                    {target_x: x_label, target_y: y_label},
                    "Country",
                    filepath + ".html"
                )
            elif(mode=="seaborn"):
                top_n_seaborn_df = self.__convert_for_seaborn__(df)
                PlotUtil.SeabornUtil().plot_line(
                    top_n_seaborn_df, 
                    title,
                    x_label,
                    y_label,
                    filepath + ".png"
                )
            elif(mode=="matplotlib"):
                year_list, pop_total_list, coutry_list = self.__convert_for_matplitlib__(df, target_y)
                PlotUtil.MatplotlibUtil().plot_line(
                    year_list, 
                    pop_total_list, 
                    coutry_list,
                    title,
                    x_label,
                    y_label,
                    filepath + ".png"
                )
            else:
                logging.warning("モードが間違っています。")
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error(title + "のプロットで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def __plot_connected_scatter__(self, df, target_dict, title="プロット", filepath=settings.OUTPUT_PATH+"filename"):
        """
        各国の2つのデータの推移をプロットするprivateメソッド
        
        Parameters
        ----------
        target_dict: dictionary
            対象データとラベル名の辞書
        title: string
            プロットのタイトル
        filepath: string
            ファイルパス（拡張子なし）
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = list(target_dict.keys())

            PlotUtil.PlotlyUtil().plot_connected_scatter(
                df, 
                title,
                target_list[0],
                target_list[1],
                target_dict,
                "Country",
                filepath + ".html"
            )
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error(title + "のプロットで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def plot_line_top_n(self, target_dict, extruct_target, mode="plotly", top_n=20, year=datetime.datetime.now().year, filename="filename"):
        """
        年単位での上位N国のデータの推移をプロットするpublicメソッド
        
        Parameters
        ----------
        target_dict: dictionary
            対象データとラベル名の辞書
        extruct_target: string
            上位Nカ国の抽出に使用するデータ
        mode: string, default plotly
            プロットのモード（plotly / seaborn / matplotlib）
        top_n: int, default 20
            抽出する国数
        year: int, default current year
            上位Nカ国を選択する対象年（デフォルトは現在年）
        filename: string
            ファイル名
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = list(target_dict.keys())
            title = "上位" + str(top_n) + "カ国の" + target_dict[extruct_target] + "の推移"
            target_y = target_list[1]
            filepath = settings.OUTPUT_PATH + filename
            top_n_df = self.__extruct_top_n__([target_y], extruct_target, year, top_n)
            self.__plot_line__(top_n_df, target_dict, mode, title, filepath)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error(title + "のプロットで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
 
    def plot_line_countries(self, target_dict, countries, mode="plotly", filename="filename"):
        """
        年単位での指定した国のデータの推移をプロットするpublicメソッド
        
        Parameters
        ----------
        target_dict: dictionary
            対象データとラベル名の辞書
        countries: list
            国のリスト
        mode: string, default plotly
            プロットのモード（plotly / seaborn / matplotlib）
        filename: string
            ファイル名
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = list(target_dict.keys())
            label_list = list(target_dict.values())
            title = label_list[1] + "の推移"
            target_y = target_list[1]
            filepath = settings.OUTPUT_PATH + filename
            df = self.__extruct_countries__([target_y], countries)
            self.__plot_line__(df, target_dict, mode, title, filepath)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error(title + "のプロットで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def plot_connected_scatter_top_n(self, target_dict, extruct_target, top_n=5, year=datetime.datetime.now().year, filename="filename"):
        """
        各国の2つのデータの推移をプロットするpublicメソッド
        
        Parameters
        ----------
        target_dict: dictionary
            対象データとラベル名の辞書
        extruct_target: string
            上位Nカ国の抽出に使用するデータ
        top_n: int, default 5
            抽出する国数
        year: int, default current year
            上位Nカ国を選択する対象年（デフォルトは現在年）
        filename: string
            ファイル名

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = list(target_dict.keys())
            label_list = list(target_dict.values())
            title = target_dict[extruct_target] + "の上位" + str(top_n) + "カ国の" + label_list[0] + "と" + label_list[1] + "の推移"
            filepath = settings.OUTPUT_PATH + filename
            top_n_df = self.__extruct_top_n__(target_list, extruct_target, year, top_n)
            self.__plot_connected_scatter__(top_n_df, target_dict, title, filepath)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error(title + "のプロットで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def plot_connected_scatter_countries(self, target_dict, countries, filename="filename"):
        """
        各国の2つのデータの推移をプロットするpublicメソッド
        
        Parameters
        ----------
        target_dict: dictionary
            対象データとラベル名の辞書
        countries: list
            国のリスト
        filename: string
            ファイル名
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = list(target_dict.keys())
            label_list = list(target_dict.values())
            title = label_list[0] + "と" + label_list[1] + "の推移"
            filepath = settings.OUTPUT_PATH + filename
            top_n_df = self.__extruct_countries__(target_list, countries)
            self.__plot_connected_scatter__(top_n_df, target_dict, title, filepath)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error(title + "のプロットで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    def plot_world_map(self, target_dict):
        """
        年単位での各国のデータの推移を世界地図にプロットするpublicメソッド
        
        Parameters
        ----------
        target_dict: dictionary
            対象データとラベル名の辞書
        
        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            target_list = list(target_dict.keys())
            label_list = list(target_dict.values())
            data = self.__extruct_for_world_map__(target_list[0])
            PlotUtil.PlotlyUtil().plot_world_map(
                data,
                locations="Country",
                locationmode='country names',
                color=target_list[0],
                filename=settings.OUTPUT_PATH + target_list[0] + "_world_map.html",
                title="世界の" + label_list[0] + "の推移"
            )
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error(label_list[0] + "の世界地図へのプロットで予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception