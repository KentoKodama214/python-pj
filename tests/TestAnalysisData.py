import unittest
from unittest import mock
from python_pj import AnalysisData
from python_pj.utils import PlotUtil

class TestLoad(unittest.TestCase):
    """
    AnalysisDataの__load__メソッドのユニットテストクラス
    """
    def test_load(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestExtructTopN(unittest.TestCase):
    """
    AnalysisDataの__extruct_top_n__メソッドのユニットテストクラス
    """
    def test_extruct_top_n(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestExtructCountries(unittest.TestCase):
    """
    AnalysisDataの__extruct_countries__メソッドのユニットテストクラス
    """
    def test_extruct_countries(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestExtructForWorldMap(unittest.TestCase):
    """
    AnalysisDataの__extruct_for_world_map__メソッドのユニットテストクラス
    """
    def test_extruct_for_world_map(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestConvertForMatplitlib(unittest.TestCase):
    """
    AnalysisDataの__convert_for_matplitlib__メソッドのユニットテストクラス
    """
    def test_convert_for_matplotlib(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestConvertForSeaborn(unittest.TestCase):
    """
    AnalysisDataの__convert_for_seaborn__メソッドのユニットテストクラス
    """
    def test_convert_for_seaborn(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestPlotLine(unittest.TestCase):
    """
    AnalysisDataの__plot_line__メソッドのユニットテストクラス    
    """
    def _mock_plot_line_plotly(self):
        """
        plotlyのplot_lineのmock
        """
    
    @mock.patch(PlotUtil.PlotlyUtil().plot_line, new=_mock_plot_line_plotly)
    def test_plotly(self):
        """
        正常系（plotly）
        """

    def test_seaborn(self):
        """
        正常系（seaborn）
        """

    def test_matplotlib(self):
        """
        正常系（matplotlib）
        """

class TestPlotConnectedScatter(unittest.TestCase):
    """
    AnalysisDataの__plot_connected_scatter__メソッドのユニットテストクラス    
    """
    def test_plot_connected_scatter(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestPlotLineTopN(unittest.TestCase):
    """
    AnalysisDataのplot_line_top_nメソッドのユニットテストクラス    
    """
    def test_plot_line_top_n(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestPlotLineCountries(unittest.TestCase):
    """
    AnalysisDataのplot_line_countriesメソッドのユニットテストクラス    
    """
    def test_plot_line_countries(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestPlotConnectedScatterTopN(unittest.TestCase):
    """
    AnalysisDataのplot_connected_scatter_top_nメソッドのユニットテストクラス    
    """
    def test_plot_connected_scatter_top_n(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestPlotConnectedScatterCountries(unittest.TestCase):
    """
    AnalysisDataのplot_connected_scatter_countriesメソッドのユニットテストクラス    
    """
    def test_plot_connected_scatter_countries(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

class TestPlotWorldMap(unittest.TestCase):
    """
    AnalysisDataのplot_world_mapメソッドのユニットテストクラス    
    """
    def test_plot_world_map(self):
        """
        正常系
        """
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """ 

if __name__ == '__main__':
    unittest.main()