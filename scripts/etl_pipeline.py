"""Simple ETL Pipeline for India Agricultural Productivity Dataset"""

import pandas as pd
import numpy as np
import argparse
import sys
from pathlib import Path


def clean_data(df):
    # ---------------- COLUMN CLEANING ---------------- #
    df.columns = df.columns.str.strip().str.lower()
    
    if "crop_year" in df.columns:
        df = df.rename(columns={"crop_year": "year"})
    
    required_cols = ["state", "district", "crop", "season", "area", "production", "year"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # ---------------- BASIC CLEANING ---------------- #
    for col in ["state", "district", "crop", "season"]:
        df[col] = df[col].astype(str).str.strip()

    df = df.dropna(subset=["crop", "area", "production"])
    df = df[(df["area"] > 0) & (df["production"] >= 0)]

    df["season"] = df["season"].str.title()

    # ---------------- REMOVE INCOMPLETE YEARS ---------------- #
    year_counts = df["year"].value_counts()
    threshold = 0.8 * year_counts.max()
    valid_years = year_counts[year_counts >= threshold].index
    df = df[df["year"].isin(valid_years)]

    print("Valid years:", sorted(valid_years))

    # ---------------- REMOVE COCONUT (UNIT ISSUE) ---------------- #
    df = df[~df["crop"].str.lower().str.contains("coconut", na=False)]

    # ---------------- YIELD CALCULATION ---------------- #
    df["yield"] = df["production"] / df["area"]

    df["yield"].replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.dropna(subset=["yield"])

    # ---------------- OUTLIER HANDLING ---------------- #
    cap = df["yield"].quantile(0.99)
    df["yield"] = df["yield"].clip(upper=cap)

    # ---------------- FINAL CLEAN ---------------- #
    df = df.drop_duplicates().reset_index(drop=True)

    if df.empty:
        raise ValueError("Dataset is empty after cleaning")

    return df


def main():
    parser = argparse.ArgumentParser(description="Run ETL pipeline")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Output CSV path")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print("Input file not found")
        sys.exit(1)

    print("Reading data...")
    df = pd.read_csv(input_path)

    print("Cleaning data...")
    df = clean_data(df)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print("Saved cleaned data to:", output_path)
    print("Final shape:", df.shape)


if __name__ == "__main__":
    main()