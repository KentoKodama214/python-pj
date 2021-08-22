import math
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
            TODO
        """

        try:
            return math.sin((month - 1) * math.pi / 6)
        except ValueError:
            print("月から春（3〜5月）を数値化で例外が発生しました。")
            traceback.print_exc()

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
            TODO
        """

        try:
            return math.sin((month - 4) * math.pi / 6)
        except ValueError:
            print("月から夏（6〜8月）を数値化で例外が発生しました。")
            traceback.print_exc()

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
            TODO
        """

        try:
            return math.sin((month - 7) * math.pi / 6)
        except ValueError:
            print("月から秋（9〜11月）を数値化で例外が発生しました。")
            traceback.print_exc()

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
            TODO
        """

        try:
            return math.sin((month - 10) * math.pi / 6)
        except ValueError:
            print("月から冬（12〜2月）を数値化で例外が発生しました。")
            traceback.print_exc()

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
            TODO
        """

        try:
            if 2 < month < 6:
                return "春"
            elif 5 < month < 9:
                return "夏"
            elif 8 < month < 12:
                return "秋"
            else:
                return "冬"
        except ValueError:
            print("月から季節を文字列化で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def day_to_weekday(date):
        """
        日から曜日を文字列化
        
        Parameters
        ----------
        date: date
            日付
            
        Returns
        ----------
        day of week: string
            曜日

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            weekday = ["月", "火", "水", "木", "金", "土", "日"]
            return weekday[date.weekday()]
        except ValueError:
            print("日から曜日を文字列化で例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def date_to_moon_age(year, month, day):
        """
        グレゴリオ暦から月齢を計算（15が満月、0/30が新月）
        
        Parameters
        ----------
        year: int
            年
        month: int 
            月
        day: int
            日
        
        Returns
        ----------
        math.sin(): float
            sin変換した月齢

        Raises
        ----------
        ValueError
            TODO
        """

        try:
            if month == 1 or month == 3:
                c = 0
            elif month == 2 or month == 4 or month == 5:
                c = 2
            else:
                c = month - 2
            return math.sin(((((year - 11) % 19) * 11 + c + day) % 30) * math.pi / 30)
        except ValueError:
            print("グレゴリオ暦から月齢を計算中に例外が発生しました。")
            traceback.print_exc()
