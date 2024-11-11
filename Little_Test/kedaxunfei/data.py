import json
from tqdm import tqdm

def load_jsonl_file(textfile):
    out = []
    with open(textfile, "r", encoding="utf8") as inpf:
        for line in tqdm(inpf, desc="Load"):
            out.append(json.loads(line))
    return out

def save_json_data(data, textfile):
    with open(textfile, "w", encoding="utf8") as outf:
        for line in tqdm(data, "Save"):
            outf.write("{}\n".format(json.dumps(line, ensure_ascii=False)))