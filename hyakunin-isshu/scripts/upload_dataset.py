#!/usr/bin/env python3
from datasets import load_dataset
from huggingface_hub import HfApi, RepoUrl
import json

# Load with "test" as the split name
dataset = load_dataset("json", data_files={"test": "./data/hyakunin_isshu_mc.jsonl"})

# Count records for size category
num_records = len(dataset["test"])
if num_records < 1000:
    size_category = "n<1K"
elif num_records < 10000:
    size_category = "1K<n<10K"
else:
    size_category = "10K<n<100K"

# Create README.md
readme_content = f"""---
license: cc-by-sa-4.0
language:
  - ja
task_categories:
  - question-answering
  - multiple-choice
tags:
  - hyakunin-isshu
  - japanese-literature
  - benchmark
pretty_name: "Hyakunin Isshu Multiple Choice"
size_categories:
  - {size_category}
---

# Hyakunin Isshu Multiple Choice Dataset

日本の古典文学「小倉百人一首」を基にした多肢選択問題のベンチマークデータセット

## Dataset Description

### Dataset Summary
百人一首の上の句が与えられた時に、正しい下の句を5択から選ぶタスクです。LLMの日本語理解力や古典知識の評価に使用できます。

### Dataset Statistics
- **Total Records**: {num_records}
- **Split**: test

### Dataset Structure

#### Data Instances
```json
{{
  "poem_id": 1,
  "kamiku": "秋の田の かりほの庵の とまをあらみ",
  "shimoku": "わが衣手は 露にぬれつつ",
  "kamiku_reading": "あきのたの かりほのいほの とまをあらみ",
  "shimoku_reading": "わがころもでは つゆにぬれつつ",
  "decisive_character": "あきの",
  "poet": "天智天皇",
  "choice_0": "わが衣手は 露にぬれつつ",
  "choice_1": "あまりてなどか 人の戀しき",
  "choice_2": "雲がくれにし 夜半の月かな",
  "choice_3": "もれ出づる月の 影のさやけさ",
  "choice_4": "みだれ初めにし 我ならなくに",
  "answer_index": 0
}}
```

#### Data Fields
- `poem_id`: 百人一首の番号（1-100）
- `kamiku`: 上の句
- `shimoku`: 下の句
- `kamiku_reading`: 上の句の読み（歴史的仮名遣）
- `shimoku_reading`: 下の句の読み（歴史的仮名遣）
- `decisive_character`: 決まり字
- `poet`: 作者名
- `choice_0-4`: 5つの選択肢（ランダムに並べられている）
- `answer_index`: 正解のインデックス（0-4）

## Dataset Usage

```python
from datasets import load_dataset

dataset = load_dataset("piijey/hyakunin-isshu-mc")
```

## License
CC-BY-SA-4.0（Wikisource のライセンスに準拠）
"""

# Upload dataset
dataset.push_to_hub("piijey/hyakunin-isshu-mc", private=True)

# Upload README
api = HfApi()
api.upload_file(
    path_or_fileobj=readme_content.encode('utf-8'),
    path_in_repo="README.md",
    repo_id="piijey/hyakunin-isshu-mc",
    repo_type="dataset",
)

print(f"✓ Dataset uploaded ({num_records} records)")
print("✓ README.md uploaded")

