import unittest
import math
import datetime
from python_pj.utils import DateUtil

class TestMonthToSpringBySin(unittest.TestCase):
    """
    DateUtilのmonth_to_spring_by_sinメソッドのユニットテストクラス
    """
    def test_january(self):
        """
        正常系（1月）
        """
        actual = DateUtil.DateUtil().month_to_spring_by_sin(1)
        expected = math.sin(0 * math.pi / 6)
        self.assertEqual(actual, expected)
    
    def test_march(self):
        """
        正常系（3月）
        """
        actual = DateUtil.DateUtil().month_to_spring_by_sin(3)
        expected = math.sin(2 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_december(self):
        """
        正常系（12月）
        """
        actual = DateUtil.DateUtil().month_to_spring_by_sin(12)
        expected = math.sin(11 * math.pi / 6)
        self.assertEqual(actual, expected)
        
    def test_value_range_error(self):
        """
        異常系（月が1〜12月ではない）
        """
        with self.assertRaises(ValueError):
            DateUtil.DateUtil().month_to_spring_by_sin(0)

    def test_type_error_float(self):
        """
        異常系（月がfloat型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_spring_by_sin(1.5)
            
    def test_type_error_str(self):
        """
        異常系（月がstr型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_spring_by_sin('1')

class TestMonthToSummerBySin(unittest.TestCase):
    """
    DateUtilのmonth_to_summer_by_sinメソッドのユニットテストクラス
    """
    def test_january(self):
        """
        正常系（1月）
        """
        actual = DateUtil.DateUtil().month_to_summer_by_sin(1)
        expected = math.sin(-3 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_june(self):
        """
        正常系（6月）
        """
        actual = DateUtil.DateUtil().month_to_summer_by_sin(6)
        expected = math.sin(2 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_december(self):
        """
        正常系（12月）
        """
        actual = DateUtil.DateUtil().month_to_summer_by_sin(12)
        expected = math.sin(8 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_value_range_error(self):
        """
        異常系（月が1〜12月ではない）
        """
        with self.assertRaises(ValueError):
            DateUtil.DateUtil().month_to_summer_by_sin(0)

    def test_type_error_float(self):
        """
        異常系（月がfloat型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_summer_by_sin(1.5)
            
    def test_type_error_str(self):
        """
        異常系（月がstr型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_summer_by_sin('1')

class TestMonthToAutumnBySin(unittest.TestCase):
    """
    DateUtilのmonth_to_autumn_by_sinメソッドのユニットテストクラス
    """
    def test_january(self):
        """
        正常系（1月）
        """
        actual = DateUtil.DateUtil().month_to_autumn_by_sin(1)
        expected = math.sin(-6 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_september(self):
        """
        正常系（9月）
        """
        actual = DateUtil.DateUtil().month_to_autumn_by_sin(9)
        expected = math.sin(2 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_december(self):
        """
        正常系（12月）
        """
        actual = DateUtil.DateUtil().month_to_autumn_by_sin(12)
        expected = math.sin(5 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_value_range_error(self):
        """
        異常系（月が1〜12月ではない）
        """
        with self.assertRaises(ValueError):
            DateUtil.DateUtil().month_to_autumn_by_sin(0)

    def test_type_error_float(self):
        """
        異常系（月がfloat型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_autumn_by_sin(1.5)
            
    def test_type_error_str(self):
        """
        異常系（月がstr型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_autumn_by_sin('1')

class TestMonthToWinterBySin(unittest.TestCase):
    """
    DateUtilのmonth_to_winter_by_sinメソッドのユニットテストクラス
    """
    def test_january(self):
        """
        正常系（1月）
        """
        actual = DateUtil.DateUtil().month_to_winter_by_sin(1)
        expected = math.sin(-9 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_september(self):
        """
        正常系（9月）
        """
        actual = DateUtil.DateUtil().month_to_winter_by_sin(9)
        expected = math.sin(-1 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_december(self):
        """
        正常系（12月）
        """
        actual = DateUtil.DateUtil().month_to_winter_by_sin(12)
        expected = math.sin(2 * math.pi / 6)
        self.assertEqual(actual, expected)

    def test_value_range_error(self):
        """
        異常系（月が1〜12月ではない）
        """
        with self.assertRaises(ValueError):
            DateUtil.DateUtil().month_to_winter_by_sin(0)

    def test_type_error_float(self):
        """
        異常系（月がfloat型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_winter_by_sin(1.5)
            
    def test_type_error_str(self):
        """
        異常系（月がstr型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_autumn_by_sin('1')

class TestMonthToSeason(unittest.TestCase):
    """
    DateUtilのmonth_to_seasonメソッドのユニットテストクラス
    """
    def test_spring(self):
        """
        正常系（春）
        """
        actual = DateUtil.DateUtil().month_to_season(3)
        expected = "春"
        self.assertEqual(actual, expected)

    def test_summer(self):
        """
        正常系（夏）
        """
        actual = DateUtil.DateUtil().month_to_season(8)
        expected = "夏"
        self.assertEqual(actual, expected)

    def test_autumn(self):
        """
        正常系（秋）
        """
        actual = DateUtil.DateUtil().month_to_season(9)
        expected = "秋"
        self.assertEqual(actual, expected)
        
    def test_winter(self):
        """
        正常系（冬）
        """
        actual = DateUtil.DateUtil().month_to_season(2)
        expected = "冬"
        self.assertEqual(actual, expected)

    def test_value_range_error(self):
        """
        異常系（月が1〜12月ではない）
        """
        with self.assertRaises(ValueError):
            DateUtil.DateUtil().month_to_season(0)

    def test_type_error_float(self):
        """
        異常系（月がfloat型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_season(1.5)
            
    def test_type_error_str(self):
        """
        異常系（月がstr型）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().month_to_season('1')

class TestDayToWeekday(unittest.TestCase):
    """
    DateUtilのday_to_weekdayメソッドのユニットテストクラス
    """
    def test_sunday(self):
        """
        正常系（日曜日）
        """
        actual = DateUtil.DateUtil().day_to_weekday(datetime.date(2021, 9, 12))
        expected = "日"
        self.assertEqual(actual, expected)
    
    def test_saturday(self):
        """
        正常系（土曜日）
        """
        actual = DateUtil.DateUtil().day_to_weekday(datetime.date(2021, 9, 11))
        expected = "土"
        self.assertEqual(actual, expected)
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().day_to_weekday(1.5)

class TestDateToMoonAge(unittest.TestCase):
    """
    DateUtilのdate_to_moon_ageメソッドのユニットテストクラス
    """
    def test_january(self):
        """
        正常系（1月）
        """
        actual = DateUtil.DateUtil().date_to_moon_age(datetime.date(2021, 1, 1))
        expected = math.sin(((((2021 - 11) % 19) * 11 + 1) % 30) * math.pi / 30)
        self.assertEqual(actual, expected)
    
    def test_february(self):
        """
        正常系（2月）
        """
        actual = DateUtil.DateUtil().date_to_moon_age(datetime.date(2021, 2, 1))
        expected = math.sin(((((2021 - 11) % 19) * 11 + 2 + 1) % 30) * math.pi / 30)
        self.assertEqual(actual, expected)

    def test_december(self):
        """
        正常系（12月）
        """
        actual = DateUtil.DateUtil().date_to_moon_age(datetime.date(2021, 12, 1))
        expected = math.sin(((((2021 - 11) % 19) * 11 + 10 + 1) % 30) * math.pi / 30)
        self.assertEqual(actual, expected)
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """
        with self.assertRaises(TypeError):
            DateUtil.DateUtil().date_to_moon_age(1.5)

if __name__ == '__main__':
    unittest.main()