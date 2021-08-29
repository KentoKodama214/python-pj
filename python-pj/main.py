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

    # 年単位での総人口に対する各国（上位20カ国）の人口の割合の推移
    # この割合が増えていると、人口の伸び率、世界に対する影響力がわかる
    analysisData.plot_population_ratio()
    
    # 年単位での各国（上位20カ国）のGDPの推移
    # GDP値として使うのは、NGDPDやPPPGDP
    # この値が増えていると、経済成長の傾向がわかる
    analysisData.plot_ngdpd()
    analysisData.plot_pppgdp()
    
    # 年単位での各国（上位20カ国）の労働所得の推移
    # この値が増えていると、国が発展していたり経済成長していることがわかる
    analysisData.plot_labour_income(2017)
    
    # 年単位での各国（上位20カ国）の輸出入の推移
    # この値が増えていると、経済成長して他国との貿易が盛んになっていることがわかる
    analysisData.plot_import(2020)
    analysisData.plot_export(2020)
    
    # 年単位での全世界の総人口・総輸出入(・GDPの上位20カ国平均・労働所得の上位20カ国平均)の推移
    # この値の傾向で世界的な動向がわかる
    
    logging.debug("End")

if __name__ == '__main__':
    main()