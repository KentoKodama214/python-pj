import unittest
import os
import numpy as np
import pandas as pd
import seaborn as sns
from python_pj.utils import PlotUtil

class TestSeabornUtilPlotStatistical1d(unittest.TestCase):
    def test_plot(self):
        """
        正常系
        """
        try:
            matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
            filename = "filename.png"
            xlabel = "x label"
            PlotUtil.SeabornUtil().plot_statistical_1d(matrix, filename, xlabel)
        except:
            print("例外が発生しました")
        finally:
            os.remove(filename)
    
    def test_type_error(self):
        """
        異常系（型エラー）
        """
        matrix = 1
        filename = "filename.png"
        xlabel = "x label"
        with self.assertRaises(TypeError):
            PlotUtil.SeabornUtil().plot_statistical_1d(matrix, filename, xlabel)

    def test_attribute_error(self):
        """
        異常系（属性エラー）
        """
        matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
        filename = 1
        xlabel = "x label"
        with self.assertRaises(AttributeError):
            PlotUtil.SeabornUtil().plot_statistical_1d(matrix, filename, xlabel)

    def test_value_error(self):
        """
        異常系（値エラー）
        """
        matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
        filename = "filename.png"
        xlabel = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            PlotUtil.SeabornUtil().plot_statistical_1d(matrix, filename, xlabel)

class TestSeabornUtilPlotLine(unittest.TestCase):
    def test_plot(self):
        """
        正常系
        """
        try:
            data = pd.DataFrame({'a': [1, 4], 'b': [2, 5], 'c': [3, 6]})
            title = "title"
            xlabel = "a"
            ylabel = "b"
            filename = "liner_plot.png"
            PlotUtil.SeabornUtil().plot_line(data, title, xlabel, ylabel, filename)
        except:
            print("例外が発生しました。")
        finally:
            os.remove(filename)
    
    def test_attribute_error(self):
        """
        異常系（属性エラー）
        """
        data = "1"
        title = "title"
        xlabel = "a"
        ylabel = "b"
        filename = "liner_plot.png"
        with self.assertRaises(AttributeError):
            PlotUtil.SeabornUtil().plot_line(data, title, xlabel, ylabel, filename)
    
    def test_value_error(self):
        """
        異常系（値エラー）
        """
        data = pd.DataFrame({'a': [1, 4], 'b': [2, 5], 'c': [3, 6]})
        title = "title"
        xlabel = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
        ylabel = "b"
        filename = "liner_plot.png"
        with self.assertRaises(ValueError):
            PlotUtil.SeabornUtil().plot_line(data, title, xlabel, ylabel, filename)

class TestMatplotlibUtilPlotLine(unittest.TestCase):
    def test_plot(self):
        """
        正常系
        """
        try:
            xdata_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
            ydata_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
            label_list = np.array(["a", "b", "c"])
            title = "title"
            xlabel = "x label"
            ylabel = "y label"
            filename = "liner_plot.png"
            PlotUtil.MatplotlibUtil().plot_line(xdata_list, ydata_list, label_list, title, xlabel, ylabel, filename)
        except:
            print("例外が発生しました")
        finally:
            os.remove(filename)

    def test_attribute_error(self):
        """
        異常系（属性エラー）
        """
        xdata_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
        ydata_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
        label_list = np.array(["a", "b", "c"])
        title = "title"
        xlabel = "x label"
        ylabel = "y label"
        filename = 1
        with self.assertRaises(AttributeError):
            PlotUtil.MatplotlibUtil().plot_line(xdata_list, ydata_list, label_list, title, xlabel, ylabel, filename)
                
    def test_index_error(self):
        """
        異常系（インデックスエラー）
        """
        xdata_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
        ydata_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
        label_list = "a"
        title = "title"
        xlabel = "x label"
        ylabel = "y label"
        filename = "liner_plot.png"
        with self.assertRaises(IndexError):
            PlotUtil.MatplotlibUtil().plot_line(xdata_list, ydata_list, label_list, title, xlabel, ylabel, filename)

    def test_value_error(self):
        """
        異常系（値エラー）
        """
        xdata_list = "a"
        ydata_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
        label_list = np.array(["a", "b", "c"])
        title = "title"
        xlabel = "x label"
        ylabel = "y label"
        filename = "liner_plot.png"
        with self.assertRaises(ValueError):
            PlotUtil.MatplotlibUtil().plot_line(xdata_list, ydata_list, label_list, title, xlabel, ylabel, filename)

class TestPlotlyUtilPlotLine(unittest.TestCase):
    def test_plot(self):
        """
        正常系
        """
        try:
            data = pd.DataFrame({'x': [1, 4], 'y': [2, 5], 'z': [3, 6]})
            title = "title"
            x = "x"
            y = "y"
            labels = {"x": "x", "y": "y"}
            color = "z"
            filename = "liner_plot.html"
            PlotUtil.PlotlyUtil().plot_line(data, title, x, y, labels, color, filename)
        except:
            print("例外が発生しました")
        finally:
            os.remove(filename)
    
    def test_attribute_error(self):
        """
        異常系（属性エラー）
        """ 
        data = pd.DataFrame({'x': [1, 4], 'y': [2, 5], 'z': [3, 6]})
        title = "title"
        x = "x"
        y = "y"
        labels = {"x": "x", "y": "y"}
        color = "z"
        filename = 1
        with self.assertRaises(AttributeError):
            PlotUtil.PlotlyUtil().plot_line(data, title, x, y, labels, color, filename)

    def test_value_error(self):
        """
        異常系（値エラー）
        """ 
        data = 1
        title = "title"
        x = "x"
        y = "y"
        labels = {"x": "x", "y": "y"}
        color = "z"
        filename = "liner_plot.html"
        with self.assertRaises(ValueError):
            PlotUtil.PlotlyUtil().plot_line(data, title, x, y, labels, color, filename)

class TestPlotlyUtilPlotConnectedScatter(unittest.TestCase):
    def test_plot(self):
        """
        正常系
        """
        try:
            data = pd.DataFrame({'x': [1, 4], 'y': [2, 5], 'z': [3, 6], 'Year': [1999, 2000]})
            title = "title"
            x = "x"
            y = "y"
            labels = {"x": "x", "y": "y"}
            color = "z"
            filename = "connected_scatter_plot.html"
            PlotUtil.PlotlyUtil().plot_connected_scatter(data, title, x, y, labels, color, filename)
        except:
            print("例外が発生しました")
        finally:
            os.remove(filename)
    
    def test_attribute_error(self):
        """
        異常系（属性エラー）
        """ 
        data = pd.DataFrame({'x': [1, 4], 'y': [2, 5], 'z': [3, 6], 'Year': [1999, 2000]})
        title = "title"
        x = "x"
        y = "y"
        labels = {"x": "x", "y": "y"}
        color = "z"
        filename = 1
        with self.assertRaises(AttributeError):
            PlotUtil.PlotlyUtil().plot_connected_scatter(data, title, x, y, labels, color, filename)

    def test_value_error(self):
        """
        異常系（値エラー）
        """
        data = 1
        title = "title"
        x = "x"
        y = "y"
        labels = {"x": "x", "y": "y"}
        color = "z"
        filename = "connected_scatter_plot.html"
        with self.assertRaises(ValueError):
            PlotUtil.PlotlyUtil().plot_connected_scatter(data, title, x, y, labels, color, filename)

class TestPlotlyUtilPlotWorldMap(unittest.TestCase):
    def test_plot(self):
        """
        正常系
        """
        try:
            data = pd.DataFrame({'Country': ['Japan', 'China'], 'y': [2, 5]})
            title = "title"
            locations = "Country"
            locationmode = "country names"
            color = "y"
            filename = "world_map_plot.html"
            PlotUtil.PlotlyUtil().plot_world_map(data, title, locations, locationmode, color, filename)
        except:
            print("例外が発生しました")
        finally:
            os.remove(filename)

    def test_type_error(self):
        """
        異常系（型エラー）
        """
        data = 1
        title = "title"
        locations = "Country"
        locationmode = "country names"
        color = "y"
        filename = "connected_scatter_plot.html"
        with self.assertRaises(TypeError):
            PlotUtil.PlotlyUtil().plot_world_map(data, title, locations, locationmode, color, filename) 

    def test_attribute_error(self):
        """
        異常系（属性エラー）
        """
        data = pd.DataFrame({'Country': ['Japan', 'China'], 'y': [2, 5]})
        title = "title"
        locations = "Country"
        locationmode = "country names"
        color = "y"
        filename = 1
        with self.assertRaises(AttributeError):
            PlotUtil.PlotlyUtil().plot_world_map(data, title, locations, locationmode, color, filename)

    def test_value_error(self):
        """
        異常系（値エラー）
        """
        data = pd.DataFrame({'Country': ['Japan', 'China'], 'y': [2, 5]})
        title = "title"
        locations = "Country"
        locationmode = "a"
        color = "y"
        filename = "world_map_plot.html"
        with self.assertRaises(ValueError):
            PlotUtil.PlotlyUtil().plot_world_map(data, title, locations, locationmode, color, filename)

if __name__ == '__main__':
    unittest.main()