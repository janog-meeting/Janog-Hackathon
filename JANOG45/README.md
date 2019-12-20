# JANOG45

## 作成物

YAMLからネットワーク図を生成するツールを利用した
configからトポ図を生成するツール

## 完成参考URL

https://github.com/cidrblock/drawthe.net

http://go.drawthe.net/


## 実行方法

### ライブラリのインストール

```bash
pipenv sync
```

### 実行

```bash
pipenv run python -m src.main
```

### アウトプット

`templates`にあるjinja2ファイルからYAMLが`output`に生成されます
