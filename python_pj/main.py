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
import time

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
        # 年単位での全世界の総人口・総輸出入(・GDPの上位20カ国平均・労働所得の上位20カ国平均)の推移
        # この値の傾向で世界的な動向がわかる
        future_list.append(executor.submit(analysisData.plot_world_map, target_dict = {"PopTotal": "総人口"}))
        
        # 年単位での各国の人口の推移
        # この値が増えていると、人口の伸び、世界に対する影響力がわかる
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "PopTotal": "総人口"}, extruct_target = "PopTotal", filename = "PopTotal_Top20"))
        
        # 年単位での各国（上位20カ国）のGDPの推移
        # GDP値として使うのは、NGDPDやPPPGDP
        # この値が増えていると、経済成長の傾向がわかる
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "NGDPD": "NGDPD"}, extruct_target = "NGDPD", filename = "NGDPD_Top20"))
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "PPPGDP": "PPPGDP"}, extruct_target = "PPPGDP", filename = "PPPGDP_TOP20"))
        
        # 年単位での各国（上位20カ国）の労働所得の推移
        # この値が増えていると、国が発展していたり経済成長していることがわかる
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "LabourIncome": "労働所得"}, extruct_target = "LabourIncome", year = 2017, filename = "LabourIncome_Top20"))
        
        # 年単位での各国（上位20カ国）の輸出入の推移
        # この値が増えていると、経済成長して他国との貿易が盛んになっていることがわかる
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "Import": "輸入額"}, extruct_target = "Import", year = 2020, filename = "Import_Top20"))
        future_list.append(executor.submit(analysisData.plot_line_top_n, target_dict = {"Year": "年", "Export": "輸出額"}, extruct_target = "Export", year = 2020, filename = "Export_Top20"))
        
        # 各国の総人口とNGDPDの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_top_n, target_dict = {"PopTotal": "総人口", "NGDPD": "NGDPD"}, extruct_target = "NGDPD", filename = "NGDPD_vs_PopTotal_Top5"))
        
        # 各国の労働所得とNGDPDの推移
        future_list.append(executor.submit(analysisData.plot_connected_scatter_top_n, target_dict = {"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, extruct_target = "NGDPD", filename = "NGDPD_vs_LabourIncome_Top5"))
        
        _ = futures.as_completed(fs=future_list)

    logging.debug("End")

if __name__ == '__main__':
    main()
