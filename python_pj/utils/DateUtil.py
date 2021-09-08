import math
import datetime
import logging
import traceback

class DateUtil:
    """
    日付のUtilクラス
    """
    
    @staticmethod
    def month_to_spring_by_sin(month):
        """
        月から春（3〜5月）を数値化
        
        Parameters
        ----------
        month: int
            月
            
        Returns
        ----------
        math.sin(): float
            sin変換した春

        Raises
        ----------
        ValueError
            monthが1未満13以上で指定された場合
        TypeError
            monthにint以外の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if (not isinstance(month, int)):
                raise TypeError
            elif month < 1 or month > 12:
                raise ValueError
            
            return math.sin((month - 1) * math.pi / 6)
        except ValueError:
            logging.error("月は1~12の整数を指定してください。")
            raise ValueError
        except TypeError:
            logging.error("月は1~12の整数を指定してください。")
            raise TypeError
        except:
            logging.error("月から春（3〜5月）を数値化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def month_to_summer_by_sin(month):
        """
        月から夏（6〜8月）を数値化
        
        Parameters
        ----------
        month: int
            月
            
        Returns
        ----------
        math.sin(): float
            sin変換した夏

        Raises
        ----------
        ValueError
            monthが1未満13以上で指定された場合
        TypeError
            monthにint以外の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if (not isinstance(month, int)):
                raise TypeError
            elif month < 1 or month > 12:
                raise ValueError
            
            return math.sin((month - 4) * math.pi / 6)
        except ValueError:
            logging.error("月は1~12の整数を指定してください。")
            raise ValueError
        except TypeError:
            logging.error("月は1~12の整数を指定してください。")
            raise TypeError
        except:
            logging.error("月から夏（6〜8月）を数値化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def month_to_autumn_by_sin(month):
        """
        月から秋（9〜11月）を数値化
        
        Parameters
        ----------
        month: int
            月
            
        Returns
        ----------
        math.sin(): float
            sin変換した秋

        Raises
        ----------
        ValueError
            monthが1未満13以上で指定された場合
        TypeError
            monthにint以外の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if (not isinstance(month, int)):
                raise TypeError
            elif month < 1 or month > 12:
                raise ValueError
            
            return math.sin((month - 7) * math.pi / 6)
        except ValueError:
            logging.error("月は1~12の整数を指定してください。")
            raise ValueError
        except TypeError:
            logging.error("月は1~12の整数を指定してください。")
            raise TypeError
        except:
            logging.error("月から秋（9〜11月）を数値化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def month_to_winter_by_sin(month):
        """
        月から冬（12〜2月）を数値化
        
        Parameters
        ----------
        month: int
            月
            
        Returns
        ----------
        math.sin(): float
            sin変換した冬

        Raises
        ----------
        ValueError
            monthが1未満13以上で指定された場合
        TypeError
            monthにint以外の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if (not isinstance(month, int)):
                raise TypeError
            elif month < 1 or month > 12:
                raise ValueError
            
            return math.sin((month - 10) * math.pi / 6)
        except ValueError:
            logging.error("月は1~12の整数を指定してください。")
            raise ValueError
        except TypeError:
            logging.error("月は1~12の整数を指定してください。")
            raise TypeError
        except:
            logging.error("月から冬（12〜2月）を数値化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def month_to_season(month):
        """
        月から季節を文字列化
        
        Parameters
        ----------
        month: int
            月
            
        Returns
        ----------
        season: string
            季節

        Raises
        ----------
        ValueError
            monthが1未満13以上で指定された場合
        TypeError
            monthにint以外の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if (not isinstance(month, int)):
                raise TypeError
            elif month < 1 or month > 12:
                raise ValueError
            elif 2 < month < 6:
                return "春"
            elif 5 < month < 9:
                return "夏"
            elif 8 < month < 12:
                return "秋"
            else:
                return "冬"
        except ValueError:
            logging.error("月は1~12の整数を指定してください。")
            raise ValueError
        except TypeError:
            logging.error("月は1~12の整数を指定してください。")
            raise TypeError
        except:
            logging.error("月から季節を文字列化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def day_to_weekday(date):
        """
        日から曜日を文字列化
        
        Parameters
        ----------
        date: datetime.date
            日付
            
        Returns
        ----------
        day of week: string
            曜日

        Raises
        ----------
        TypeError
            dateにdatetime.date以外の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if (not isinstance(date, datetime.date)):
                raise TypeError
            
            weekday = ["月", "火", "水", "木", "金", "土", "日"]
            return weekday[date.weekday()]
        except TypeError:
            logging.error("日付を指定してください。")
            raise TypeError
        except:
            logging.error("日から曜日を文字列化で予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def date_to_moon_age(date):
        """
        グレゴリオ暦から月齢を計算（15が満月、0/30が新月）
        
        Parameters
        ----------
        date: datetime.date
            日付
        
        Returns
        ----------
        math.sin(): float
            sin変換した月齢

        Raises
        ----------
        TypeError
            dateにdatetime.date以外の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if (not isinstance(date, datetime.date)):
                raise TypeError
            
            if date.month == 1 or date.month == 3:
                c = 0
            elif date.month == 2 or date.month == 4 or date.month == 5:
                c = 2
            else:
                c = date.month - 2
            return math.sin(((((date.year - 11) % 19) * 11 + c + date.day) % 30) * math.pi / 30)
        except TypeError:
            logging.error("日付を指定してください。")
            raise TypeError
        except:
            logging.error("グレゴリオ暦から月齢を計算中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
