import sys
import json
import pandas as pd
from tqdm import tqdm

inpfile = sys.argv[1]
outfile = sys.argv[2]

def save_json_data(data, textfile):
    with open(textfile, "w", encoding="utf8") as outf:
        for line in tqdm(data):
            outf.write("{}\n".format(json.dumps(line, ensure_ascii=False)))

def main():
    data = None
    print("Loading data from {}...".format(inpfile))
    if inpfile.endswith("parquet"):
        data = pd.read_parquet(inpfile).to_dict(orient="records")
    parquet
    print("Saving data from {}...".format(outfile))
    save_json_data(data, outfile)
    
if "__main__" == __name__:
    main()
    