# coding:utf-8
#
# テキストの単語の出現数をベクトル/行列化する
# 詳しくは以下のUELを参照
# http://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
#
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

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
        ValueError
            TODO
        """
        try:
            count  = CountVectorizer()
            X      = count.fit_transform(word_list).toarray()
            Xnames = count.get_feature_names()
            return X, Xnames
        except ValueError:
            print("出現回数によるベクトル化の際に例外が発生しました。")
            traceback.print_exc()

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
        ValueError
            TODO

        """
        tfidf  = TfidfVectorizer()
        X      = tfidf.fit_transform(word_list).toarray()
        Xnames = tfidf.get_feature_names()
        return X, Xnames
