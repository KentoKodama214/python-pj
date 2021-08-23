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
    LoggingUtil.LoggingUtil().set_config(filepath=settings.log_path, level=settings.log_level)
    logging.debug("Start")
    # 分析データのインスタンス生成&読込
    analysisData = AnalysisData.AnalysisData()
    logging.debug("End")

if __name__ == '__main__':
    main()