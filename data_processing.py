"""
data_processing.py

This file handles all data modeling and transmoration logic such as
-Loading Dataset
-Cleaning Dataset
-Valadeting numeric fields
-Computing metrics
-Sorting Data
-Returning clean Data Frames to API layer
"""

import pandas as pd
from config import DATA_PATH

#Loads and prepares master dataset.
def build_master_table():
    df = pd.read_csv(DATA_PATH)

    # Normalize ISO3 , Prevents Merge issues
    df["ISO3"] = df["ISO3"].str.strip().str.upper()

    # Drop rows missing critical data
    df = df.dropna(subset=["ISO3", "total_funding", "Population"])

    # Ensure numeric types
    df["total_funding"] = pd.to_numeric(df["total_funding"], errors="coerce")
    df["Population"] = pd.to_numeric(df["Population"], errors="coerce")

    # Remove impossible values
    df = df[df["Population"] > 0]
    df = df[df["total_funding"] >= 0]

    # Recalculate funding per capita (safety)
    df["funding_per_capita"] = (
        df["total_funding"] / df["Population"]
    )

    # Sort by funding descending
    df = df.sort_values(by="total_funding", ascending=False)

    return df


def get_top_countries(df, n=10):
    return df.head(n)


def get_country(df, iso3):
    iso3 = iso3.strip().upper()
    return df[df["ISO3"] == iso3]