# JANOG45

## 作成物

YAMLからネットワーク図を生成するツールを利用した
configからトポ図を生成するツール

## 完成参考URL

http://103.131.194.3:8082/

## 実行方法

### 必要なもの

- Python 3.8
- pipenv

### ライブラリのインストール

```bash
pipenv sync
```

### 実行

```bash
pipenv run main
```

### アウトプット

`templates`にあるjinja2ファイルからYAMLが`output`に生成されます
