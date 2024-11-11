import sys
import json
from tqdm import tqdm

from data import (
    load_jsonl_file,
    save_json_data,
)

from prompts import (
    anli_prompt
)

task = "anli"
inpfile = "./json/11_anli.train_r1-00000-of-00001.json"
outfile = "./sft-data/11_anli.train_r1-00000-of-00001.json"

def anli_process_fn(data):
    out = []
    for line in tqdm(data, desc="anli process"):
        newline = {}
        newline["input"] = anli_prompt.format_map({"Premise": line["premise"], "Hypothesis": line["hypothesis"]})
        newline["target"] = str(line["label"])
        out.append(newline)
    return out

task2process_fn = {
    "anli": anli_process_fn,
}

def main():
    print("Loading data from {}...".format(inpfile))
    data = load_jsonl_file(inpfile)
    
    print("Processing...")
    out = task2process_fn[task](data)
    
    print("Saving data into {}...".format(outfile))
    save_json_data(out, outfile)
    
if "__main__" == __name__:
    main()
