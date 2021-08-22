#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import AbstructAnalysisData
import settings
import pymysql.cursors
import pandas as pd

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
            conn = pymysql.connect(host=settings.host,
                    user=settings.user,
                    db=settings.db,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
        
            with conn.cursor() as cursor:
                cursor.execute(settings.select_analysis_data)
                results = cursor.fetchall()
        finally:
            conn.close()
            return(pd.DataFrame(results))