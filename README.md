# python-pj
pythonでのデータ分析・機械学習を実践するためのリポジトリ

## このプロジェクトの背景・目的
[こちら](https://github.com/KentoKodama214/python-pj/wiki)にまとめています。

## 環境構築
### ライブラリ等のインストール
|名称|バージョン|
|---|---|
|python|3.9.6|
|MySQL|8.0.26|

### データベース&データ
1. 本リポジトリをチェックアウトしてください。
2. MySQLをインストール後、任意のデータベース・ユーザを作成してください。
3. python-pj/settings.pyにデータベースの接続情報を設定してください。
```
host = 'ホスト名'
db = 'データベース名'
user = 'ユーザ名'
password = 'パスワード'
```
4. readAndInsertData.pyを実行してください。実行後、3で指定したデータベースにテーブル・ビューなどが作成され、データがインポートされます。
```
python readAndInsertData.py
```