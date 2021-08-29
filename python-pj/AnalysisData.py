#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import AbstructAnalysisData
import settings
import pymysql.cursors
import numpy as np
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
        finally:
            conn.close()
            self.__data = pd.DataFrame(results)

    def extruct_top_n(self, target, year, top_n):
        """
        対象データがある年で上位N位の国のデータを抽出する
        
        Parameters
        ----------
        target: string
            対象データ
        year: int
            上位N位を判定する年
        top_n: int
            上位N位まで抽出する
            
        Raises
        ----------
        ValueError
            TODO
        """
        try:
            conn = pymysql.connect(host=settings.HOST,
                    user=settings.USER,
                    db=settings.DB,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
            with conn.cursor() as cursor:
                cursor.execute(settings.SELECT_COUNTRY_VIEW)
                results = cursor.fetchall()
                self.__countries = pd.DataFrame(results)
            
            countries = self.__countries[self.__countries['LocID']<900]['Country'].values.tolist()
            df = self.__data[['Country', 'Year', target]]
            df2 = df[df['Country'].isin(countries)]
            top_n_countries = df2[df2['Year']==year].sort_values(by=target, ascending=False).head(top_n)['Country'].values.tolist()
            return df2[df2['Country'].isin(top_n_countries)]
        except ValueError:
            print("データからTopNの抽出で例外が発生しました。")
            traceback.print_exc()
    
    def plot_population_ratio(self, year=datetime.datetime.now().year):
        """
        年単位での総人口に対する各国（上位20カ国）の人口の割合の推移をプロットするpublicメソッド
        この値が増えていると、人口の伸び率、世界に対する影響力がわかる
        """
        try:
            top_20_df = self.extruct_top_n('PopTotal', year, 20)
            pop_total_list = []
            year_list = []
            coutry_list = []
            
            for country in set(top_20_df['Country'].values.tolist()):
                df = top_20_df[top_20_df['Country']==country]
                coutry_list.append(country)
                year_list.append(df['Year'].values.tolist())
                pop_total_list.append(df['PopTotal'].values.tolist())
            
            PlotUtil.PlotUtil().plot_line_by_matplotlib(
                year_list, 
                pop_total_list, 
                coutry_list,
                "総人口に対する各国（上位20カ国）の人口の割合の推移",
                "年",
                "総人口",
                settings.OUTPUT_PATH + "population_ratio.png"
            )
        except ValueError:
            print("年単位での総人口に対する各国（上位20カ国）の人口の割合の推移のプロットで例外が発生しました。")
            traceback.print_exc()
    
    def plot_ngdpd(self, year=datetime.datetime.now().year):
        """
        年単位での各国（上位20カ国）のNGDPDの推移をプロットするpublicメソッド
        この割合が増えていると、経済成長の傾向がわかる
        """
        try:
            top_20_df = self.extruct_top_n('NGDPD', year, 20)
            pop_total_list = []
            year_list = []
            coutry_list = []
            
            for country in set(top_20_df['Country'].values.tolist()):
                df = top_20_df[top_20_df['Country']==country]
                coutry_list.append(country)
                year_list.append(df['Year'].values.tolist())
                pop_total_list.append(df['NGDPD'].values.tolist())
            
            PlotUtil.PlotUtil().plot_line_by_matplotlib(
                year_list, 
                pop_total_list, 
                coutry_list,
                "各国（上位20カ国）のNGDPDの推移",
                "年",
                "NGDPD",
                settings.OUTPUT_PATH + "NGDPD.png"
            )
        except ValueError:
            print("年単位での各国（上位20カ国）のNGDPDの推移のプロットで例外が発生しました。")
            traceback.print_exc()
    
    def plot_pppgdp(self, year=datetime.datetime.now().year):
        """
        年単位での各国（上位20カ国）のPPPGDPの推移をプロットするpublicメソッド
        この値が増えていると、経済成長の傾向がわかる
        """
        try:
            top_20_df = self.extruct_top_n('PPPGDP', year, 20)
            pop_total_list = []
            year_list = []
            coutry_list = []
            
            for country in set(top_20_df['Country'].values.tolist()):
                df = top_20_df[top_20_df['Country']==country]
                coutry_list.append(country)
                year_list.append(df['Year'].values.tolist())
                pop_total_list.append(df['PPPGDP'].values.tolist())
            
            PlotUtil.PlotUtil().plot_line_by_matplotlib(
                year_list, 
                pop_total_list, 
                coutry_list,
                "各国（上位20カ国）のPPPGDPの推移",
                "年",
                "PPPGDP",
                settings.OUTPUT_PATH + "PPPGDP.png"
            )
        except ValueError:
            print("年単位での各国（上位20カ国）のPPPGDPの推移のプロットで例外が発生しました。")
            traceback.print_exc()
    
    def plot_labour_income(self, year=datetime.datetime.now().year):
        """
        年単位での各国（上位20カ国）の労働所得の推移をプロットするpublicメソッド
        この値が増えていると、国が発展していたり経済成長していることがわかる
        """
        try:
            top_20_df = self.extruct_top_n('LabourIncome', year, 20)
            pop_total_list = []
            year_list = []
            coutry_list = []
            
            for country in set(top_20_df['Country'].values.tolist()):
                df = top_20_df[top_20_df['Country']==country]
                coutry_list.append(country)
                year_list.append(df['Year'].values.tolist())
                pop_total_list.append(df['LabourIncome'].values.tolist())
            
            PlotUtil.PlotUtil().plot_line_by_matplotlib(
                year_list, 
                pop_total_list, 
                coutry_list,
                "各国（上位20カ国）の労働所得の推移",
                "年",
                "労働所得",
                settings.OUTPUT_PATH + "LabourIncome.png"
            )
        except ValueError:
            print("年単位での各国（上位20カ国）の労働所得の推移のプロットで例外が発生しました。")
            traceback.print_exc()
    
    def plot_import(self, year=datetime.datetime.now().year):
        """
        年単位での各国（上位20カ国）の輸入額の推移をプロットするpublicメソッド
        この値が増えていると、他国との貿易が盛んになっていることがわかる
        """
        try:
            top_20_df = self.extruct_top_n('Import', year, 20)
            pop_total_list = []
            year_list = []
            coutry_list = []
            
            for country in set(top_20_df['Country'].values.tolist()):
                df = top_20_df[top_20_df['Country']==country]
                coutry_list.append(country)
                year_list.append(df['Year'].values.tolist())
                pop_total_list.append(df['Import'].values.tolist())
            
            PlotUtil.PlotUtil().plot_line_by_matplotlib(
                year_list, 
                pop_total_list, 
                coutry_list,
                "各国（上位20カ国）の輸入額の推移",
                "年",
                "輸入額",
                settings.OUTPUT_PATH + "Import.png"
            )
        except ValueError:
            print("年単位での各国（上位20カ国）の輸入額の推移のプロットで例外が発生しました。")
            traceback.print_exc()
    
    def plot_export(self, year=datetime.datetime.now().year):
        """
        年単位での各国（上位20カ国）の輸出額の推移をプロットするpublicメソッド
        この値が増えていると、他国との貿易が盛んになっていることがわかる
        """
        try:
            top_20_df = self.extruct_top_n('Export', year, 20)
            pop_total_list = []
            year_list = []
            coutry_list = []
            
            for country in set(top_20_df['Country'].values.tolist()):
                df = top_20_df[top_20_df['Country']==country]
                coutry_list.append(country)
                year_list.append(df['Year'].values.tolist())
                pop_total_list.append(df['Export'].values.tolist())
            
            PlotUtil.PlotUtil().plot_line_by_matplotlib(
                year_list, 
                pop_total_list, 
                coutry_list,
                "各国（上位20カ国）の輸出額の推移",
                "年",
                "輸出額",
                settings.OUTPUT_PATH + "Export.png"
            )
        except ValueError:
            print("年単位での各国（上位20カ国）の輸出額の推移のプロットで例外が発生しました。")
            traceback.print_exc()