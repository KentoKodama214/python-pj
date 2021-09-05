#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from abc import abstractclassmethod

class AbstructAnalysisData:
    """
    分析データの抽象クラス
    """
    
    def __init__(self):
        """
        コンストラクタ
        """
        self.__load__()
   
    @abstractclassmethod
    def __load__(self):
        """
        データ読込の抽象privateメソッド
        読み込むデータに合わせて実装する
        コンストラクタでのみ呼び出す
        """
        pass