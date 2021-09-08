import os
import csv
import zipfile
import numpy as np
import pandas as pd
import logging
import traceback


class FileUtil:
    """
    ファイルのUtilクラス
    """
    
    @staticmethod
    def check_file_exist(filepath):
        """
        ファイル/フォルダの存在を確認
        
        Parameters
        ----------
        filepath: string
            ファイルパス
        
        Returns
        ----------
        TRUE/FALSE

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            if os.path.isfile(filepath):
                return True
            else:
                return False
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("ファイル/フォルダのチェック中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    @staticmethod
    def read_csv_file_by_std(filepath):
        """
        標準ライブラリでcsvファイルから読み込み
        
        Parameters
        ----------
        filepath: string
            ファイルパス
        
        Returns
        ----------
        numpy_data: ndarray
            numpyデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            with open(filepath, newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in csv_reader:
                    numpy_data = np.array(row)
                return numpy_data
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("標準ライブラリでcsvファイルを読み込み中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
    
    @staticmethod
    def read_csv_file_by_numpy(filepath, value=None):
        """
        numpyでcsvファイルから読み込み
        
        Parameters
        ----------
        filepath: string
            ファイルパス
        value: variable
            補完値
            
        Returns
        ----------
        numpy_data: ndarray
            numpyデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            numpy_data = np.genfromtxt(filepath, delimiter=",", filling_values=value)
            return numpy_data
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("numpyでcsvファイルを読み込み中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def read_csv_file_by_pandas(filepath):
        """
        pandasでcsvファイルから読み込み
        
        Parameters
        ----------
        filepath: string
            ファイルパス
        
        Returns
        ----------
        pandas_data: DataFrame
            pandasデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            pandas_data = pd.read_csv(filepath, delimiter=",", header=None)
            return pandas_data
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("pandasでcsvファイルを読み込み中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def read_zip_file_by_std(execPath, filename):
        """
        標準ライブラリでzipファイルから解凍せずに読み込む
        
        Parameters
        ----------
        execPath: string
            実行パス
        filename: string
            ファイル名
        
        Returns
        ----------
        numpy_data: ndarray
            numpyデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            with zipfile.ZipFile(execPath + '/' + filename, 'r') as post:
                for info in post.infolist():
                    # ファイルパスでスキップ判定
                    if not os.path.isfile(execPath + '/' + info.filename):
                        continue

                    file_data = post.read(info.filename).decode('utf-8')
                    for row in file_data.split('\n'):
                        if numpy_data is None:
                            numpy_data = np.array(row)
                        else:
                            numpy_data = np.vstack((numpy_data, np.array(row)))
                return numpy_data
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("zipファイルから読み込み中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
   
    @staticmethod
    def write_csv_file_by_std(numpy_data, filepath):
        """
        標準ライブラリでcsvファイルへ書き込み
        
        Parameters
        ----------
        numpy_data: ndarray
            numpyデータ
        filepath: string
            ファイルパス

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            with open(filepath, 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')  # 改行コード（\n）を指定しておく
                writer.writerows(numpy_data)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("標準ライブラリでcsvファイルへ書き込み中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def write_csv_file_by_numpy(numpy_data, filepath):
        """
        numpyでcsvファイルへ書き込み

        Parameters
        ----------
        numpy_data: ndarray
            numpyデータ
        filepath: string
            ファイルパス

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            np.savetxt(filepath, numpy_data, delimiter=",")
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("numpyでcsvファイルへ書き込み中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def write_csv_file_by_pandas(pandas_data, filepath):
        """
        pandasでcsvファイルへ書き込み

        Parameters
        ----------
        pandas_data: DataFrame
            pandas出力データ
        filepath: string
            ファイルパス

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """

        try:
            pandas_data.pandas_data.to_csv(filepath)
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("pandasでcsvファイルへ書き込み中に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception
