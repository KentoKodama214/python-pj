#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import AnalysisData
import settings
import logging
from utils import LoggingUtil
from concurrent import futures

__author__ = "kodamakento"
argvs = sys.argv
argc = len(argvs)

def main():
    LoggingUtil.LoggingUtil().set_config(filepath=settings.LOG_PATH, level=settings.LOG_LEVEL)
    logging.debug("Start")
    # 分析データのインスタンス生成&読込
    analysisData = AnalysisData.AnalysisData()
    future_list = []
    with futures.ThreadPoolExecutor() as executor:
        # 各国の人口の推移
        future_list.append(executor.submit(analysisData.plot_world_map, target_dict = {"PopTotal": "総人口"}))
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "PopTotal": "総人口"}, extruct_target = "PopTotal", filename = "PopTotal_Top20"))

        # 各国の人口密度の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "PopDensity": "人口密度"}, extruct_target = "PopDensity", filename = "PopDensity_Top20"))

        # 総人口の上位20カ国の人口密度の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "PopDensity": "人口密度", "PopTotal": "総人口"}, extruct_target = "PopTotal", filename = "PopDensity_Top20_PopTotal"))

        # 上位20カ国の労働所得の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "LabourIncome": "労働所得"}, extruct_target = "LabourIncome", year = 2017, filename = "LabourIncome_Top20"))

        # 総人口の上位20カ国の労働所得の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "LabourIncome": "労働所得", "PopTotal": "総人口"}, extruct_target = "PopTotal", year = 2017, filename = "LabourIncome_Top20_PopTotal"))

        # 総人口・人口密度と労働所得の相関（特に相関は見られなかった）
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, filename = "LabourIncome_PopTotal_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopDensity": "人口密度", "LabourIncome": "労働所得"}, filename = "LabourIncome_PopDensity_corr"))

        # 各エリアでの総人口の推移
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Japan", "China"], filename = "PopTotal_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "PopTotal_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "PopTotal_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "PopTotal_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "PopTotal_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "PopTotal_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "PopTotal_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "PopTotal_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "PopTotal_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_line_countries, target_dict = {"Year": "年", "PopTotal": "総人口"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "PopTotal_East_Europa"))

        # 各エリアでの総人口と労働所得の推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Japan", "China"], filename = "LabourIncome_vs_PopTotal_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "LabourIncome_vs_PopTotal_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "LabourIncome_vs_PopTotal_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "LabourIncome_vs_PopTotal_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "LabourIncome_vs_PopTotal_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "LabourIncome_vs_PopTotal_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "LabourIncome_vs_PopTotal_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "LabourIncome_vs_PopTotal_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "LabourIncome_vs_PopTotal_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "LabourIncome": "労働所得"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "LabourIncome_vs_PopTotal_East_Europa"))

        # 上位20カ国の輸入額の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "Import": "輸入額"}, extruct_target = "Import", year = 2020, filename = "Import_Top20"))

        # 総人口の上位20カ国の輸入額の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "Import": "輸入額", "PopTotal": "総人口"}, extruct_target = "PopTotal", year = 2020, filename = "Import_Top20_PopTotal"))

        # 総人口・人口密度・労働所得と輸入額の相関（特に相関は見られなかった）
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, filename = "Import_PopTotal_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopDensity": "人口密度", "Import": "輸入額"}, filename = "Import_PopDensity_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, filename = "Import_LabourIncome_corr"))

        # 各エリアでの総人口と輸入額の推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Japan", "China"], filename = "Import_vs_PopTotal_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "Import_vs_PopTotal_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "Import_vs_PopTotal_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "Import_vs_PopTotal_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "Import_vs_PopTotal_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "Import_vs_PopTotal_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "Import_vs_PopTotal_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "Import_vs_PopTotal_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "Import_vs_PopTotal_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Import": "輸入額"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "Import_vs_PopTotal_East_Europa"))

        # 各エリアでの労働所得と輸入額の推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Japan", "China"], filename = "Import_vs_LabourIncome_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "Import_vs_LabourIncome_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "Import_vs_LabourIncome_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "Import_vs_LabourIncome_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "Import_vs_LabourIncome_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "Import_vs_LabourIncome_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "Import_vs_LabourIncome_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "Import_vs_LabourIncome_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "Import_vs_LabourIncome_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Import": "輸入額"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "Import_vs_LabourIncome_East_Europa"))

        # 上位20カ国の輸出の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "Export": "輸出額"}, extruct_target = "Export", year = 2020, filename = "Export_Top20"))

        # 総人口の上位20カ国の輸出額の推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "Export": "輸出額", "PopTotal": "総人口"}, extruct_target = "PopTotal", year = 2020, filename = "Export_Top20_PopTotal"))
        
        # 総人口・人口密度・労働所得と輸出額の相関（特に相関は見られなかった）
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, filename = "Export_PopTotal_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopDensity": "人口密度", "Export": "輸出額"}, filename = "Export_PopDensity_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, filename = "Export_LabourIncome_corr"))
        
        # 輸入額と輸出額の相関
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"Import": "輸入額", "Export": "輸出額"}, filename = "Export_Import_corr"))

        # 各エリアでの総人口と輸出額の推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Japan", "China"], filename = "Export_vs_PopTotal_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "Export_vs_PopTotal_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "Export_vs_PopTotal_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "Export_vs_PopTotal_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "Export_vs_PopTotal_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "Export_vs_PopTotal_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "Export_vs_PopTotal_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "Export_vs_PopTotal_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "Export_vs_PopTotal_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "Export": "輸出額"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "Export_vs_PopTotal_East_Europa"))
        
        # 各エリアでの労働所得と輸出額の推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Japan", "China"], filename = "Export_vs_LabourIncome_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "Export_vs_LabourIncome_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "Export_vs_LabourIncome_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "Export_vs_LabourIncome_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "Export_vs_LabourIncome_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "Export_vs_LabourIncome_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "Export_vs_LabourIncome_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "Export_vs_LabourIncome_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "Export_vs_LabourIncome_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "Export": "輸出額"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "Export_vs_LabourIncome_East_Europa"))

        # 各エリアでの輸入額と輸出額の推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Japan", "China"], filename = "Export_vs_Import_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "Export_vs_Import_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "Export_vs_Import_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "Export_vs_Import_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "Export_vs_Import_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "Export_vs_Import_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "Export_vs_Import_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "Export_vs_Import_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "Export_vs_Import_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Import": "輸入額", "Export": "輸出額"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "Export_vs_Import_East_Europa"))

        # GDPの上位20カ国のGDPの推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "NGDPD": "NGDPD"}, extruct_target = "NGDPD", filename = "NGDPD_Top20"))
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "PPPSH": "PPPSH"}, extruct_target = "PPPSH", filename = "PPPSH_TOP20"))

        # 総人口の上位20カ国のGDPの推移
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "NGDPD": "NGDPD", "PopTotal": "総人口"}, extruct_target = "PopTotal", filename = "NGDPD_Top20_PopTotal"))
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "PPPSH": "PPPSH", "PopTotal": "総人口"}, extruct_target = "PopTotal", filename = "PPPSH_TOP20_PopTotal"))

        # 総人口・人口密度・労働所得とNGDPDの相関（特に相関は見られなかった）
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, filename = "NGDPD_PopTotal_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopDensity": "人口密度", "NGDPD": "NGDPD"}, filename = "NGDPD_PopDensity_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, filename = "NGDPD_LabourIncome_corr"))

        # 輸入額・輸出額とNGDPDの相関
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"Import": "輸入額", "NGDPD": "NGDPD"}, filename = "NGDPD_Import_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, filename = "NGDPD_Export_corr"))

        # 総人口・人口密度・労働所得とPPPSHの相関（特に相関は見られなかった）
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, filename = "PPPSH_PopTotal_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"PopDensity": "人口密度", "PPPSH": "PPPSH"}, filename = "PPPSH_PopDensity_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, filename = "PPPSH_LabourIncome_corr"))

        # 輸入額・輸出額とPPPSHの相関
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"Import": "輸入額", "PPPSH": "PPPSH"}, filename = "PPPSH_Import_corr"))
        future_list.append(executor.submit(analysisData.plot_correlation, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, filename = "PPPSH_Export_corr"))
        
        # 各エリアでの総人口とNGDPDの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Japan", "China"], filename = "NGDPD_vs_PopTotal_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "NGDPD_vs_PopTotal_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "NGDPD_vs_PopTotal_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "NGDPD_vs_PopTotal_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "NGDPD_vs_PopTotal_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "NGDPD_vs_PopTotal_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "NGDPD_vs_PopTotal_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "NGDPD_vs_PopTotal_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "NGDPD_vs_PopTotal_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "NGDPD_vs_PopTotal_East_Europa"))
        
        # 各エリアでの労働所得とNGDPDの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Japan", "China"], filename = "NGDPD_vs_LabourIncome_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "NGDPD_vs_LabourIncome_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "NGDPD_vs_LabourIncome_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "NGDPD_vs_LabourIncome_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "NGDPD_vs_LabourIncome_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "NGDPD_vs_LabourIncome_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "NGDPD_vs_LabourIncome_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "NGDPD_vs_LabourIncome_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "NGDPD_vs_LabourIncome_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "NGDPD_vs_LabourIncome_East_Europa"))

        # 各エリアでの輸出額とNGDPDの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Japan", "China"], filename = "NGDPD_vs_Export_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "NGDPD_vs_Export_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "NGDPD_vs_Export_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "NGDPD_vs_Export_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "NGDPD_vs_Export_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "NGDPD_vs_Export_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "NGDPD_vs_Export_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "NGDPD_vs_Export_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "NGDPD_vs_Export_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "NGDPD": "NGDPD"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "NGDPD_vs_Export_East_Europa"))
        
        # 各エリアでの総人口とPPPSHの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Japan", "China"], filename = "PPPSH_vs_PopTotal_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "PPPSH_vs_PopTotal_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "PPPSH_vs_PopTotal_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "PPPSH_vs_PopTotal_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "PPPSH_vs_PopTotal_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "PPPSH_vs_PopTotal_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "PPPSH_vs_PopTotal_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "PPPSH_vs_PopTotal_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "PPPSH_vs_PopTotal_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"PopTotal": "総人口", "PPPSH": "PPPSH"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "PPPSH_vs_PopTotal_East_Europa"))
        
        # 各エリアでの労働所得とPPPSHの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Japan", "China"], filename = "PPPSH_vs_LabourIncome_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "PPPSH_vs_LabourIncome_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "PPPSH_vs_LabourIncome_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "PPPSH_vs_LabourIncome_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "PPPSH_vs_LabourIncome_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "PPPSH_vs_LabourIncome_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "PPPSH_vs_LabourIncome_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "PPPSH_vs_LabourIncome_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "PPPSH_vs_LabourIncome_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"LabourIncome": "労働所得", "PPPSH": "PPPSH"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "PPPSH_vs_LabourIncome_East_Europa"))

        # 各エリアでの輸出額とPPPSHの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Japan", "China"], filename = "PPPSH_vs_Export_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Indonesia", "Philippines", "Thailand", "Viet Nam", "Singapore", "Malaysia"], filename = "PPPSH_vs_Export_South_East_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Bangladesh", "India", "Pakistan", "Turkey"], filename = "PPPSH_vs_Export_South_and_West_Asia"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Egypt", "Ethiopia", "Nigeria", "Niger"], filename = "PPPSH_vs_Export_Africa_Northern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Kenya", "South Africa", "Democratic Republic of the Congo", "United Republic of Tanzania"], filename = "PPPSH_vs_Export_Africa_Southern_Hemisphere"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["United States of America", "Brazil", "Mexico", "Canada"], filename = "PPPSH_vs_Export_North_and_South_America"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Sweden", "United Kingdom", "Norway", "Iceland", "Ireland", "Denmark"], filename = "PPPSH_vs_Export_North_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Italy", "Spain", "Portugal", "Greece"], filename = "PPPSH_vs_Export_South_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Germany", "Belgium", "France", "Switzerland", "Netherlands"], filename = "PPPSH_vs_Export_West_Europa"))
        future_list.append(executor.submit(analysisData.plot_connected_scatter_countries, target_dict = {"Export": "輸出額", "PPPSH": "PPPSH"}, countries = ["Russian Federation", "Ukraine", "Poland", "Romania"], filename = "PPPSH_vs_Export_East_Europa"))

        _ = futures.as_completed(fs=future_list)

    logging.debug("End")

if __name__ == '__main__':
    main()
