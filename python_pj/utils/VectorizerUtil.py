# coding:utf-8
#
# テキストの単語の出現数をベクトル/行列化する
# 詳しくは以下のUELを参照
# http://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
#
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import logging
import traceback
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

class VectorizerUtil:
    """
    ベクトル化のUtilクラス
    """
    
    @staticmethod
    def count_vectorizer(word_list):
        """
        出現回数によるベクトル化

        Parameters
        ----------
        word_list: list
            単語のリスト
        
        Returns
        ----------
        X: ndarray
            ベクトル化したnumpyデータ
        Xnames: ndarray
            ベクトル化したときに特徴としたキーワードデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            count  = CountVectorizer()
            X      = count.fit_transform(word_list).toarray()
            Xnames = count.get_feature_names()
            return X, Xnames
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("出現回数によるベクトル化の際に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

    @staticmethod
    def tfidf_vectorizer(word_list):
        """
        TF-IDF特徴によるベクトル化
        
        Parameters
        ----------
        word_list: list
            単語のリスト
        
        Returns
        ----------
        X: ndarray
            ベクトル化したnumpyデータ
        Xnames: ndarray
            ベクトル化したときに特徴としたキーワードデータ

        Raises
        ----------
        TypeError
            誤った引数の型が指定された場合
        Exception
            その他例外が発生した場合
        """
        try:
            tfidf  = TfidfVectorizer()
            X      = tfidf.fit_transform(word_list).toarray()
            Xnames = tfidf.get_feature_names()
            return X, Xnames
        except TypeError:
            logging.error("引数の型が間違っています。")
            raise TypeError
        except:
            logging.error("TF-IDF特徴によるベクトル化の際に予期しない例外が発生しました。")
            traceback.print_exc()
            raise Exception

