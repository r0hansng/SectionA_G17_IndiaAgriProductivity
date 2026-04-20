"""ETL Pipeline for India Agricultural Productivity Analysis.

This module provides a robust, production-ready pipeline for ingesting raw 
agricultural statistics and transforming them into a standard format suitable 
for statistical modeling and dashboarding.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column headers to a clean snake_case format.
    
    Normalizing headers early prevents join failures and ensures consistent 
    attribute referencing throughout the analytical pipeline, especially when 
    source data contains trailing spaces or inconsistent casing.
    """
    df.columns = df.columns.astype(str).str.strip()
    
    cleaned = (
        df.columns.str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    result = df.copy()
    result.columns = cleaned
    return result


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Execute core cleaning transformations to ensure high-fidelity data.
    
    This process handles structural normalization, categorical stabilization, 
    missing value imputation, and outlier neutralization using domain-specific rules.
    """
    # Structural and Categorical Normalization:
    # Converting to snake_case simplifies downstream SQL-like operations, while 
    # trimming categorical strings prevents grouping logic failures caused by 
    # inconsistent padding in the raw survey data.
    df = normalize_columns(df)
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].astype(str).str.strip()
    
    # Dataset Integrity and Missing Value Imputation:
    # Records lacking a crop classification are non-recoverable and thus excluded.
    # For production metrics, we use a multi-tiered median imputation strategy 
    # (state-crop-season > crop-wide > global) to preserve local variances 
    # without introducing the bias common in mean-based approaches.
    df = df.dropna(subset=['crop'])
    
    def impute_production(group):
        group['production'] = group['production'].fillna(group['production'].median())
        return group
    
    if df['production'].isnull().any():
        df = df.groupby(['state', 'crop', 'season'], group_keys=False).apply(impute_production)
        df['production'] = df['production'].fillna(df.groupby('crop')['production'].transform('median'))
        df['production'] = df['production'].fillna(df['production'].median())

    # Metric Derivation and Outlier Stabilization:
    # Recalculating Yield from ground-truth attributes (Production/Area) ensures 
    # internal consistency. We then cap extreme values at the 99th percentile 
    # to stabilize distributions and prevent data entry errors from skewing 
    # regional benchmarks.
    df['yield'] = df['production'] / df['area']
    
    yield_cap = df['yield'].quantile(0.99)
    df['yield'] = df['yield'].clip(upper=yield_cap)
    
    # Final Deduplication:
    # Eliminating duplicate records prevents inflation of aggregate production figures 
    # across different levels of geographic analysis.
    df = df.drop_duplicates().reset_index(drop=True)
    
    return df


def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Read a raw CSV file and return a fully cleaned and validated DataFrame."""
    df = pd.read_csv(input_path)
    return basic_clean(df)


def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Write the cleaned DataFrame to disk, ensuring parent directories exist."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"Processed dataset successfully persisted to: {output_path}")
    print(f"Final Integrity Check: {len(df)} rows | {len(df.columns)} columns")


def parse_args() -> argparse.Namespace:
    """Handle command-line interface arguments for the ETL process."""
    parser = argparse.ArgumentParser(description="Run the Capstone 2 ETL pipeline.")
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the raw CSV file in data/raw/.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to the cleaned CSV file in data/processed/.",
    )
    return parser.parse_args()


def main() -> None:
    """Main execution entry point for the ETL pipeline."""
    args = parse_args()
    if not args.input.exists():
        print(f"Error: Source file {args.input} not found.")
        sys.exit(1)
        
    cleaned_df = build_clean_dataset(args.input)
    save_processed(cleaned_df, args.output)


if __name__ == "__main__":
    main()
