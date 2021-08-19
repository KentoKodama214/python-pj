# リポジトリ概要
pythonでのデータ分析・機械学習を実践するためのリポジトリ

# このプロジェクトの背景・目的
[こちら](https://github.com/KentoKodama214/python-pj/wiki)を参照ください。

# 使用するデータ
[こちら](https://github.com/KentoKodama214/python-pj/wiki/%E3%83%87%E3%83%BC%E3%82%BF)を参照ください。

# 分析・機械学習の結果
[こちら]()を参照ください。

***
# ご自身で実行・カスタマイズしたい方へ
## 環境構築
### ライブラリ等のインストール
|名称|バージョン|
|---|---|
|python|3.9.6|
|MySQL|8.0.26|

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