import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

for file in csv_files:
    print("=" * 80)
    print(f"FILE: {file.name}")
    
    df = pd.read_csv(file)

    print("\nShape")
    print(df.shape)

    print("\nDtypes")
    print(df.dtypes)

    print("\nHead")
    print(df.head())

    print("=" * 80)

    