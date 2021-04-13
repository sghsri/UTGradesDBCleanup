import csv
import json
with open('old_agg.csv') as f:
    a = [{k: v for k, v in row.items()}
         for row in csv.DictReader(f, skipinitialspace=True)]
    with open('result.json', 'w') as fp:
        json.dump(a, fp, indent=4)
