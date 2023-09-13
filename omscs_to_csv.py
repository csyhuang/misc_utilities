import re
import pandas as pd

with open("omscs.syllabus.txt", "r") as f:
    data = f.readlines()

to_csv_tuples = []

for str1 in data:
    try:
        match = re.match(r'(\*?)([a-zA-Z-?]+) (\d+?\s?O?\d+?):\s([a-zA-Z\s-]+)', str1)
        print(match.group(0))
    except:
        print("Skip {}".format(str1))
        continue
    if match.group(4).strip().endswith("A"):
        fifth = "A"
    elif match.group(4).strip().endswith("C"):
        fifth = "C"
    else:
        fifth = ""
    to_csv_tuples.append((
        match.group(0).strip(),
        match.group(1).strip(),
        match.group(2).strip(),
        match.group(3).strip(),
        match.group(4).strip().rstrip('A|C'),
        fifth
    ))

df = pd.DataFrame(to_csv_tuples)
print(df.head(50))
df.to_csv("omscs_syllabus.csv", sep=",")
