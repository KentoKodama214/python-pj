# coding:utf-8
#
# ログ出力の基底クラス
# このクラスを継承してログを出力する
#
import logging

class LoggingUtil:
    """
    ロギングのUtilクラス
    """
    
    @staticmethod
    def set_config(filepath=None, level=logging.INFO):
        """
        コンストラクタ
        
        Parameters
        ----------
        filepath: string, default None
            ファイルパス。ログをファイル出力するときは指定する
        level: logging.{DEBUG, INFO, WARN, ERROR}
            ログレベル
        """

        formatter = '%(levelname)s\t %(asctime)s\t %(filename)s, line %(lineno)d\t %(message)s'
        logging.basicConfig(filename=filepath, encoding='utf-8', filemode='w', level=level, format=formatter)
