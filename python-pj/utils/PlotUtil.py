#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import traceback

class SeabornUtil:
    """
    SeabornでのPlotのUtilクラス
    """

    @staticmethod
    def plot_statistical_1d(matrix, filename, xlabel):
        """
        Seabornでの1次元ヒストグラムプロット
        
        Parameters
        ----------
        matrix: ndarray
            numpyデータ
        filename: string
            プロットの画像出力ファイル名
        xlabel: string
            x軸のラベル名
        
        Raises
        ----------
        ValueError
            TODO
        """
        
        try:
            n      = len(matrix)
            mean   = np.mean(matrix)
            median = np.median(matrix)
            var    = np.var(matrix)
            min    = np.min(matrix)
            max    = np.max(matrix)
    
            n_text      = "$\it{n}$=" + str(n)
            min_text    = "min=" + str(round(min, 3))
            max_text    = "max=" + str(round(max, 3))
            mean_text   = "mean($\mu$)=" + str(round(mean, 3))
            median_text = "median($\it{Q_{1/2}}$)=" + str(round(median, 3))
            var_text    = "variance($\sigma^2$)=" + str(round(var, 3))

            # Histgram Plot
            fig = plt.figure()
            ax  = fig.add_subplot(111)
            sns.distplot(matrix, rug = False)
            ax.set_title("histgram", fontsize = 20, fontname = 'serif')
            ax.set_xlabel(xlabel,    fontsize = 15, fontname = 'serif')
            ax.set_ylabel("% count", fontsize = 15, fontname = 'serif')
            plt.text(0.05, 0.95, n_text,      transform = ax.transAxes, fontname = 'serif')
            plt.text(0.05, 0.9,  min_text,    transform = ax.transAxes, fontname = 'serif')
            plt.text(0.05, 0.85, max_text,    transform = ax.transAxes, fontname = 'serif')
            plt.text(0.05, 0.8,  mean_text,   transform = ax.transAxes, fontname = 'serif')
            plt.text(0.05, 0.75, median_text, transform = ax.transAxes, fontname = 'serif')
            plt.text(0.05, 0.7,  var_text,    transform = ax.transAxes, fontname = 'serif')
            plt.savefig(filename)
            plt.close()
        except ValueError:
            print("Seabornでの1次元ヒストグラムのプロットで例外が発生しました。")
            traceback.print_exc()
    
    @staticmethod
    def plot_statistical_2d(matrix1, matrix2, filename, xlabel, ylabel):
        """
        Seabornでの散布図
        
        Parameters
        ----------
        matrix1: ndarray
            numpyデータ
        matrix2: ndarray
            numpyデータ        
        filename: string
            プロットの画像出力ファイル名
        xlabel: string
            x軸のラベル名
        ylabel: string
            y軸のラベル名

        Raises
        ----------
        ValueError
            TODO
        """
        
        # Scatter Plot
        try:
            g = sns.jointplot(matrix1, matrix2, kind = 'kde').plot_joint(plt.scatter, s = 30, marker = 'o', c = 'r')
            g.ax_joint.collections[0].set_alpha(0)
            g.set_axis_labels(xlabel, ylabel, fontsize = 15, fontname = 'serif')
            g.savefig(filename)
            plt.close()
        except ValueError:
            print("Seabornでの散布図のプロットで例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def plot_line(data, title="title", xlabel="x label", ylabel="y label", filename="liner_plot.png"):
        """
        seabornでの年単位でのプロット
        
        Parameters
        ----------
        data: DataFrame
            pandasデータ
        title: string
            タイトル
        xlabel: string
            x軸のラベル名
        ylabel: string
            y軸のラベル名
        filename: string
            プロットの画像出力ファイル名

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            label_list = data.columns.values
            fig = plt.figure()
            fig.set_size_inches(5 * int(len(label_list)/10), 5)
            sns.set_theme(style="whitegrid")
            sns.set(font='Hiragino Sans')
            sns.lineplot(data=data, linewidth=1.5)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=10, ncol=int(len(label_list)/10))
            plt.savefig(filename, bbox_inches='tight')
            plt.close()
        except ValueError:
            print("seabornでの年単位でのプロットで例外が発生しました。")
            traceback.print_exc()

 
class MatplotlibUtil:
    """
    MatplotlibでのPlotのUtilクラス
    """
    
    @staticmethod
    def plot_line(xdata_list, ydata_list, label_list, title="title", xlabel="x label", ylabel="y label", filename="liner_plot.png"):
        """
        matplotlibでの年単位でのプロット
        
        Parameters
        ----------
        xdata_list: list
            x軸のlistデータ
        ydata_list: list
            y軸のlistデータ
        label_list: list
            x,yデータのlistデータ。凡例に表示する
        title: string
            タイトル
        xlabel: string
            x軸のラベル名
        ylabel: string
            y軸のラベル名
        filename: string
            プロットの画像出力ファイル名

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            plt.rcParams['font.family'] = 'Hiragino Sans'
            cmap = plt.get_cmap("tab20")
            fig = plt.figure()
            fig.set_size_inches(5 * int(len(label_list)/10), 5)
            for i in range(0, len(xdata_list)):
                plt.plot(xdata_list[i], ydata_list[i], label=label_list[i], color=cmap(i/len(xdata_list)))
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid(True)
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=10, ncol=int(len(label_list)/10))
            plt.savefig(filename, bbox_inches='tight')
            plt.close()
        except ValueError:
            print("matplotlibでのプロットで例外が発生しました。")
            traceback.print_exc()


class PlotlyUtil:
    """
    PlotlyでのPlotのUtilクラス
    """
    
    @staticmethod
    def plot_line(data, title="title", x="x", y="y", labels={"x": "x", "y": "y"}, color="color", filename="liner_plot.png"):
        """
        Plotlyでのlineプロット
        
        Parameters
        ----------
        data: DataFrame
            pandasデータ
        title: string
            タイトル
        x: string
            x軸に使用するdataのカラム名
        y: string
            y軸に使用するdataのカラム名
        labels: dist
            x軸とy軸のラベル名のdictionary
        color: string
            lineプロットのcolorに使用するdataのカラム名
        filename: string
            プロットのhtml出力ファイル名

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            fig = px.line(
                data,
                x,
                y,
                color=color,
                labels=labels,
                color_discrete_sequence=px.colors.qualitative.Light24,
                title=title
            )
            fig.write_html(filename)
        except ValueError:
            print("Plotlyでのlineプロットで例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def plot_connected_scatter(data, title="title", x="x",y="y", labels={"x": "x", "y": "y"}, color="color", filename="connected_scatter_plot.png"):
        """
        Plotlyでの年単位のConnected Scatterプロット
        データが多すぎると、markerごとの年のtextが表示されなくなる
        
        Parameters
        ----------
        data: DataFrame
            pandasデータ
        title: string
            タイトル
        x: string
            x軸に使用するdataのカラム名
        y: string
            y軸に使用するdataのカラム名
        labels: dist
            x軸とy軸のラベル名のdictionary
        color: string
            lineプロットのcolorに使用するdataのカラム名
        filename: string
            プロットのhtml出力ファイル名

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            fig = px.line(
                data,
                x,
                y,
                color=color,
                text="Year",
                labels=labels,
                color_discrete_sequence=px.colors.qualitative.Light24,
                title=title
            )
            fig.update_traces(textposition="bottom right")
            fig.write_html(filename)
        except ValueError:
            print("Plotlyでの年単位のConnected Scatterプロットで例外が発生しました。")
            traceback.print_exc()

    @staticmethod
    def plot_world_map(data, title="title", locations="Country", locationmode='country names', color="color", filename="world_map_plot.html"):
        """
        Plotlyでの年単位のConnected Scatterプロット
        データが多すぎると、markerごとの年のtextが表示されなくなる
        
        Parameters
        ----------
        data: DataFrame
            pandasデータ
        title: string
            タイトル
        locations: string
            locationsを指定するカラム名
        locationmode: string
            locationmode(‘ISO-3’, ‘USA-states’, or ‘country names’)
        color: string
            プロットのcolorに使用するdataのカラム名
        filename: string
            プロットのhtml出力ファイル名

        Raises
        ----------
        ValueError
            TODO
        """
        try:
            range_max=data[color].max()*1.2
            fig = px.choropleth(
                data,
                locations=locations,
                locationmode=locationmode,
                color=color,
                color_continuous_scale=px.colors.sequential.Rainbow,
                animation_frame=data.index,
                range_color=[0,range_max],
                title=title
            )
            fig.write_html(filename)
        except ValueError:
            print("PlotlyでのWorldMapプロットで例外が発生しました。")
            traceback.print_exc()
