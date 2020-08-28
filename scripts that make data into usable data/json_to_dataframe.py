import pandas as pd

file = "H:/Vietnamese word representations/Category_classification_data/generalize_category/g_category_json/_g_category.json"

df = pd.read_json(file, lines=True)

print(df.head())

print(df.iloc[2,1])
