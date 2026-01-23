# Hyakunin-Isshu
2026/01/20

「小倉百人一首」を基に多肢選択問題のベンチマークデータセットを作成する

- Wikisource 「小倉百人一首」のページをダウンロード
```sh
curl https://ja.wikisource.org/wiki/%E5%B0%8F%E5%80%89%E7%99%BE%E4%BA%BA%E4%B8%80%E9%A6%96 -o data/wikisource_小倉百人一首.html
```
- html ファイルから表を抜き出して jsonl で保存する
    - 句の列からは、上句・下句・上句読み・下句読み・決まり字を抽出
```sh
python extract_table_to_jsonl.py
```
- 選択肢の作成：各歌について、全ての下句のセットからランダムに4つを取り出して、不正解選択肢として加える
```sh
python scripts/create_mc_dataset.py
```

### データセットを　HuggingFace にアップロード
- HuggingFace CLI をインストール、Access Token を登録
```sh
brew install huggingface-cli
hf auth login
```
- データセットをアップロード
```sh
python scripts/upload_dataset.py
```
