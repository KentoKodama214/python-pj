#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import AnalysisData
import settings
import logging
from utils import LoggingUtil

__author__ = "kodamakento"
argvs = sys.argv
argc = len(argvs)

def main():
    LoggingUtil.LoggingUtil().set_config(filepath=settings.LOG_PATH, level=settings.LOG_LEVEL)
    logging.debug("Start")
    # 分析データのインスタンス生成&読込
    analysisData = AnalysisData.AnalysisData()

    # 年単位での各国の人口の推移
    # この値が増えていると、人口の伸び、世界に対する影響力がわかる
    analysisData.plot_line({"Year": "年", "PopTotal": "総人口"}, "PopTotal")
    
    # 年単位での各国（上位20カ国）のGDPの推移
    # GDP値として使うのは、NGDPDやPPPGDP
    # この値が増えていると、経済成長の傾向がわかる
    analysisData.plot_line({"Year": "年", "NGDPD": "NGDPD"}, "NGDPD")
    analysisData.plot_line({"Year": "年", "PPPGDP": "PPPGDP"}, "PPPGDP")
    
    # 年単位での各国（上位20カ国）の労働所得の推移
    # この値が増えていると、国が発展していたり経済成長していることがわかる
    analysisData.plot_line({"Year": "年", "LabourIncome": "労働所得"}, "LabourIncome", year=2017)
    
    # 年単位での各国（上位20カ国）の輸出入の推移
    # この値が増えていると、経済成長して他国との貿易が盛んになっていることがわかる
    analysisData.plot_line({"Year": "年", "Import": "輸入額"}, "Import", year=2020)
    analysisData.plot_line({"Year": "年", "Export": "輸出額"}, "Export", year=2020)

    # 各国の総人口とNGDPDの推移
    analysisData.plot_connected_scatter({"PopTotal": "総人口", "NGDPD": "NGDPD"}, "NGDPD")
    analysisData.plot_connected_scatter({"LabourIncome": "労働所得", "NGDPD": "NGDPD"}, "NGDPD")
    
    # 年単位での全世界の総人口・総輸出入(・GDPの上位20カ国平均・労働所得の上位20カ国平均)の推移
    # この値の傾向で世界的な動向がわかる
    analysisData.plot_world_map({"PopTotal": "総人口"})
    
    logging.debug("End")

if __name__ == '__main__':
    main()