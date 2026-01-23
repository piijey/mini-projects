#!/usr/bin/env python3
import json
import random
random.seed(42)

if __name__ == "__main__":
    input_jsonl = "./data/wikisource_小倉百人一首_extracted.jsonl"
    output_jsonl = "./data/hyakunin_isshu_mc.jsonl"
    mc_records = []
    shimoku_set = set()

    with open(input_jsonl, "r", encoding="utf-8") as infile, open(output_jsonl, "w", encoding="utf-8") as outfile:
        ku_i = 1
        for line in infile:
            record = json.loads(line)
            mc_record = {
                "poem_id": ku_i,
                "kamiku": record.get("上句"),
                "shimoku": record.get("下句"),
                "kamiku_reading": record.get("上句読み"),
                "shimoku_reading": record.get("下句読み"),
                "decisive_character": record.get("決まり字"),
                "poet": record.get("作者 （括弧内は歴史的仮名遣による読み）").split(" （")[0].strip(),
            }
            shimoku_set.add(mc_record["shimoku"])
            ku_i += 1
            mc_records.append(mc_record)

    # create multiple choice options for shimoku
    with open(output_jsonl, "w", encoding="utf-8") as outfile:
        for mc_record in mc_records:
            answer_index = random.randint(0, 4)
            choices = random.sample(sorted(shimoku_set - {mc_record["shimoku"]}), 4)
            choices.insert(answer_index, mc_record["shimoku"])
            for i in range(5):
                mc_record[f"choice_{i}"] = choices[i]
            mc_record["answer_index"] = answer_index
            outfile.write(json.dumps(mc_record, ensure_ascii=False) + "\n")
    print(f"✓ Created multiple-choice dataset with {len(mc_records)} records")

