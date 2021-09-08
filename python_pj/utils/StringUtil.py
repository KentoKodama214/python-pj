import re
import traceback
import datetime as dt
import logging

class StringUtil:
    """
    文字列のUtilクラス
    """
    
    @staticmethod
    def check_string_type(check_str):
        """
        文字列からdate文字列か、dateteime文字列かを判定する
        
        Parameters
        ----------
        check_str: string
            チェック対象の文字列

        Returns
        ----------
        date/datetime/other

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        
        try:
            date_pattern1 = re.compile('(\d{4})/(\d{1,2})/(\d{1,2})')
            date_pattern2 = re.compile('(\d{4})-(\d{1,2})-(\d{1,2})')
            date_pattern3 = re.compile('(\d{4}):(\d{1,2}):(\d{1,2})')
            datetime_pattern1 = re.compile('(\d{4})/(\d{1,2})/(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            datetime_pattern2 = re.compile('(\d{4})-(\d{1,2})-(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            datetime_pattern3 = re.compile('(\d{4}):(\d{1,2}):(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            result1 = date_pattern1.search(check_str)
            result2 = date_pattern2.search(check_str)
            result3 = date_pattern3.search(check_str)
            result4 = datetime_pattern1.search(check_str)
            result5 = datetime_pattern2.search(check_str)
            result6 = datetime_pattern3.search(check_str)

            if result1:
                return "date"
            elif result2:
                return "date"
            elif result3:
                return "date"
            elif result4:
                return "datetime"
            elif result5:
                return "datetime"
            elif result6:
                return "datetime"
            else:
                return "other"
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("文字列の種類をチェック中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def convert_string_to_date(date_str):
        """
        文字列から年月日（date型）に変換
        
        Parameters
        ----------
        date_str: string
            変換する文字列
        
        Returns
        ----------
        date: date
            日付

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            date_pattern1 = re.compile('(\d{4})/(\d{1,2})/(\d{1,2})')
            date_pattern2 = re.compile('(\d{4})-(\d{1,2})-(\d{1,2})')
            date_pattern3 = re.compile('(\d{4}):(\d{1,2}):(\d{1,2})')
            result1 = date_pattern1.search(date_str)
            result2 = date_pattern2.search(date_str)
            result3 = date_pattern3.search(date_str)

            if result1:
                return dt.datetime.strptime(date_str, '%Y/%m/%d')
            elif result2:
                return dt.datetime.strptime(date_str, '%Y-%m-%d')
            elif result3:
                return dt.datetime.strptime(date_str, '%Y:%m:%d')
            else:
                return None
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("文字列から年月日（date型）に変換中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def convert_string_to_datetime(datetime_str):
        """
        文字列から年月日時分秒（date型）に変換
        
        Parameters
        ----------
        datetime_str: string
            変換する文字列
        
        Returns
        ----------
        datetime: datetime
            日時

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            date_pattern1 = re.compile('(\d{4})/(\d{1,2})/(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            date_pattern2 = re.compile('(\d{4})-(\d{1,2})-(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            date_pattern3 = re.compile('(\d{4}):(\d{1,2}):(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            result1 = date_pattern1.search(datetime_str)
            result2 = date_pattern2.search(datetime_str)
            result3 = date_pattern3.search(datetime_str)

            if result1:
                return dt.datetime.strptime(datetime_str, '%Y/%m/%d %h:%m:%s')
            elif result2:
                return dt.datetime.strptime(datetime_str, '%Y-%m-%d %h:%m:%s')
            elif result3:
                return dt.datetime.strptime(datetime_str, '%Y:%m:%d %h:%m:%s')
            else:
                return None
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("文字列から年月日時分秒（date型）に変換中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def extract_date(date_str):
        """
        文字列から年・月・日を抽出
        
        Parameters
        ----------
        date_str: string
            変換する文字列
        
        Returns
        ----------
        year: int
            年
        month: int
            月
        day: int
            日

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            date_pattern1 = re.compile('(\d{4})/(\d{1,2})/(\d{1,2})')
            date_pattern2 = re.compile('(\d{4})-(\d{1,2})-(\d{1,2})')
            date_pattern3 = re.compile('(\d{4}):(\d{1,2}):(\d{1,2})')
            result1 = date_pattern1.search(date_str)
            result2 = date_pattern2.search(date_str)
            result3 = date_pattern3.search(date_str)

            if result1:
                y, m, d = result1.groups()
                return {'year': int(y), 'month': int(m), 'day': int(d)}
            elif result2:
                y, m, d = result2.groups()
                return {'year': int(y), 'month': int(m), 'day': int(d)}
            elif result3:
                y, m, d = result3.groups()
                return {'year': int(y), 'month': int(m), 'day': int(d)}
            else:
                return None
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("文字列から年月日を抽出中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def extract_datetime(datetime_str):
        """
        文字列から年・月・日と時刻を抽出
        
        Parameters
        ----------
        datetime_str: string
            変換する文字列
        
        Returns
        ----------
        year: int
            年
        month: int
            月
        day: int
            日
        hour: int
            時
        minute: int
            分
        second: int
            秒

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            date_pattern1 = re.compile('(\d{4})/(\d{1,2})/(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            date_pattern2 = re.compile('(\d{4})-(\d{1,2})-(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            date_pattern3 = re.compile('(\d{4}):(\d{1,2}):(\d{1,2}) (\d{2}):(\d{2}):(\d{2})')
            result1 = date_pattern1.search(datetime_str)
            result2 = date_pattern2.search(datetime_str)
            result3 = date_pattern3.search(datetime_str)

            if result1:
                year, month, day, hour, minutes, second = result1.groups()
                return {'year': year, 'month': month, 'day': day, 'hour': hour, 'minutes': minutes, 'second': second}
            elif result2:
                year, month, day, hour, minutes, second = result2.groups()
                return {'year': year, 'month': month, 'day': day, 'hour': hour, 'minutes': minutes, 'second': second}
            elif result3:
                year, month, day, hour, minutes, second = result3.groups()
                return {'year': year, 'month': month, 'day': day, 'hour': hour, 'minutes': minutes, 'second': second}
            else:
                return None
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("文字列から年月日時分秒を抽出中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def extract_weekday(date_str):
        """
        文字列から曜日を計算
        
        Parameters
        ----------
        date_str: string
            変換する文字列
        
        Returns
        ----------
        weekday: string
            曜日

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            weekday = ["月", "火", "水", "木", "金", "土", "日"]
            a = StringUtil.convert_string_to_date(date_str)
            return weekday[a.weekday()]
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("文字列から曜日を計算中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
