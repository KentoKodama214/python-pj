#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import traceback

class PlotUtil:
    """
    PlotのUtilクラス
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
    def plot_line_by_matplotlib(xdata_list, ydata_list, label_list, title="title", xlabel="x label", ylabel="y label", filename="liner_plot.png"):
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
            print("matplotlibでの年単位でのプロットで例外が発生しました。")
            traceback.print_exc()
    
    @staticmethod
    def plot_line_by_seaborn(title="title", xlabel="x label", ylabel="y label", filename="liner_plot.png"):
        """
        seabornでの年単位でのプロット
        
        Parameters
        ----------
        data: DataFrame
            pandasデータ
                title: string
            タイトル
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
            print()
        except ValueError:
            print("seabornでの年単位でのプロットで例外が発生しました。")
            traceback.print_exc()
    
    @staticmethod
    def plot_line_by_plotly(title="title", xlabel="x label", ylabel="y label", filename="liner_plot.png"):
        """
        plotlyでの年単位でのプロット
        
        Parameters
        ----------
        data: DataFrame
            pandasデータ
                title: string
            タイトル
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
            print()
        except ValueError:
            print("plotlyでの年単位でのプロットで例外が発生しました。")
            traceback.print_exc()