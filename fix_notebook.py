import json

with open('notebooks/02_cleaning.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'][19]['source'] = [
    '### Convert Coconut Records\n',
    '\n',
    'Convert `Coconut` production to tonnes. It is typically recorded in counts (nuts). We assume an average weight of 1.44 kg per nut (multiply by 0.00144).'
]

nb['cells'][20]['source'] = [
    'df.loc[df["crop"] == "Coconut", "production"] = df.loc[df["crop"] == "Coconut", "production"] * 0.00144'
]

with open('notebooks/02_cleaning.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
