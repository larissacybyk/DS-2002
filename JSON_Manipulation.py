import json
import pandas as pd

# Loading into dataframe
f = open('bb_SortByConf.json')
json_data = f.read()
data = json.loads(json_data)
df = pd.DataFrame(data['teams'])

# first 100 rows
print(df.head(100), "\n")

# answering questions
num_teams = df.shape[0]
virginia_teams = (df["state"] == "VA").sum()

print("There are " + str(num_teams) + " teams.")
print("There are " + str(virginia_teams) + " teams in Virginia.")
print("Duplicate mascots:")

grouped = df.groupby("name")

duplicates = df['name'].value_counts()
duplicates = duplicates[duplicates > 1]
print(duplicates)
