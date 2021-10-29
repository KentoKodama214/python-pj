# リポジトリ概要
pythonでのデータ分析・機械学習を実践するためのリポジトリ

# このプロジェクトの背景・目的
[こちら](https://github.com/KentoKodama214/python-pj/wiki)を参照ください。

# 使用するデータ
[こちら](https://github.com/KentoKodama214/python-pj/wiki/%E3%83%87%E3%83%BC%E3%82%BF)を参照ください。

# 結果・考察
[こちら](https://github.com/KentoKodama214/python-pj/wiki/%E7%B5%90%E6%9E%9C%E3%83%BB%E8%80%83%E5%AF%9F)を参照ください。

***
# ご自身で実行・カスタマイズしたい方へ
## 環境構築
### ライブラリ等のインストール
|名称|動作保証バージョン|インストールコマンド|
|---|---|---|
|python|3.9.6|```brew install python```|
|MySQL|8.0.26|```brew install mysql```|
|pandas|1.3.1|```pip install pandas```|
|PyMySQL|1.0.2|```pip install PyMySQL```|
|scikit-learn|0.24.2|```pip install scikit-learn```|
|plotly|5.2.2|```pip install plotly```|
|numpy|1.21.2|```pip install numpy```|
|seaborn|0.11.2|```pip install seaborn```|

### ディレクトリ構成
[こちら](https://github.com/KentoKodama214/python-pj/wiki/%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E6%A7%8B%E6%88%90)を参照ください。

### データベース&データ
1. 本リポジトリをクローンしてください。
```
$ git clone https://github.com/KentoKodama214/python-pj.git
```
2. MySQLをインストール後、任意のデータベース・ユーザを作成してください。
3. python-pj/settings.pyにデータベースの接続情報を設定してください。
```
host = 'ホスト名'
db = 'データベース名'
user = 'ユーザ名'
password = 'パスワード'
```
4. python-pjへ移動し、readAndInsertData.pyを実行してください。  
実行後、3で指定したデータベースにテーブル・ビューなどが作成され、データがインポートされます。
```
$ cd python-pj
$ python readAndInsertData.py
```