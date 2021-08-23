#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import traceback

class PlotUtil:
    """
    PlotのUtilクラス
    """

    @staticmethod
    def Statistical1DPlot(matrix, filename, xlabel):
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
    def Statistical2DPlot(matrix1, matrix2, filename, xlabel, ylabel):
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
