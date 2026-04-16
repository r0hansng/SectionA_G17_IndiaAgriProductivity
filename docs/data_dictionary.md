# Data Dictionary

Use this file to document every important field in your dataset. A strong data dictionary makes your cleaning decisions, KPI logic, and dashboard filters much easier to review.

## How To Use This File

1. Add one row for each column used in analysis or dashboarding.
2. Explain what the field means in plain language.
3. Mention any cleaning or standardization applied.
4. Flag nullable columns, derived fields, and known quality issues.

## Dataset Summary

| Item | Details |
|---|---|
| Dataset name | Crop Production Statistics - India |
| Source | Kaggle - https://www.kaggle.com/datasets/nikhilmahajan29/crop-production-statistics-india |
| Raw file name | APY.csv |
| Last updated | April 16, 2026 |
| Granularity | One row per state-district-crop-year-season combination |
| Total Records | 345,336 rows |
| Coverage Period | 1997-2020 (23 years) |
| Geographic Scope | 37 states & union territories, 707 districts, 55+ crops |

## Column Definitions

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| State | string | Indian state or union territory name | "Punjab", "Maharashtra" | EDA / KPI / Tableau | Strip whitespace, verify against standard list of 37 states/UTs |
| District | string | Administrative district within state | "NICOBARS", "Ludhiana" | EDA / KPI / Tableau | **Important:** Column contains trailing spaces ("District "). Trim whitespace before analysis. Use for regional segmentation. |
| Crop | string | Name of crop cultivated (55+ varieties) | "Rice", "Wheat", "Cotton", "Sugarcane" | EDA / KPI / Tableau | Standardize capitalization, handle spelling variations (e.g., "Pulses" variants). 9 null values detected - drop rows with missing Crop. |
| Crop_Year | integer | Calendar year of cultivation | 2010, 2015, 2020 | EDA / KPI / Tableau / Forecasting | Range: 1997-2020. Use for time-series analysis and trend detection. Sort chronologically for YoY growth calculations. |
| Season | string | Agricultural season of cultivation | "Kharif", "Rabi", "Summer", "Autumn", "Winter", "Whole Year" | EDA / KPI / Tableau | **Important:** Column contains trailing spaces ("Kharif     "). Trim all whitespace. Standardize to 6 season categories. Use for seasonal pattern analysis. |
| Area | float | Cultivated area in hectares | 2439.6, 1626.4 | EDA / KPI / Tableau | **Important:** Column header has trailing space ("Area "). No null values detected. Use as denominator for Yield calculation. Validate positive values only. |
| Production | float | Total agricultural output in tonnes | 3415, 2277 | EDA / KPI / Tableau / Forecasting | **Data quality issue:** 4,948 null values (1.43% of data). Handle via: (a) drop rows with null Production, or (b) impute using state-crop-season median. Max outlier: 1.6 billion tonnes (verify data entry). |
| Yield | float | Agricultural Productivity: Production per hectare (tonnes/ha) | 1.4, 0.74, 1.59 | EDA / KPI / Tableau | **Primary KPI** - Calculated as Production ÷ Area. Max outlier: 43,958 tonnes/ha (data quality issue - requires outlier treatment or verification). Values of 0 indicate missing Production data. Use percentile capping (e.g., 99th percentile) for outlier removal. |

## Derived Columns

| Derived Column | Logic | Business Meaning |
|---|---|---|
| Yield_Efficiency_Rate | Production ÷ Area (in tonnes/hectare) | Primary KPI measuring agricultural productivity. Identifies high-performing and underperforming regions. Segmented by State, District, Crop, and Season. |
| YoY_Production_Growth_% | ((Production_Year_N - Production_Year_N-1) / Production_Year_N-1) × 100 | Year-over-year production growth percentage. Tracks whether India's agricultural output is accelerating or decelerating. Aggregated by Crop and State. |
| Area_Utilisation_Trend | Linear regression slope of Area over time by Crop-State | Identifies crops gaining or losing cultivation area over the 23-year period. Tracks shift from pulses to cash crops (sugarcane, cotton). |
| Season_Production_Share_% | (Season_Production / Total_Annual_Production) × 100 by State | Seasonal contribution to total production. Highlights Kharif dominance (~55-60% of annual production) and seasonal production concentration. |
| Underperforming_District_Index | District_Yield vs. National_Median_Yield (Percentile Rank) | Percentile ranking of district-level yields compared to national median for each crop. Identifies high-priority districts for intervention and resource allocation. |
| State_Yield_Ranking | Rank State by Average_Yield (descending) by Crop | Identifies best-performing states (Punjab, Haryana) vs. underperforming regions (Eastern & North-Eastern states). Used for best-practice benchmarking. |

## Data Quality Notes

### Missing Values
- **Production column:** 4,948 null values (1.43% of 345,336 records) - These represent missing production data and should be handled by either:
  - **Approach 1:** Drop rows with null Production values
  - **Approach 2:** Impute using state-crop-season median production
  - **Approach 3:** Flag as 0 yield when Area is available
- **Crop column:** 9 null values - These rows should be dropped as crop identification is essential for analysis

### Whitespace Issues
- **District column:** Contains trailing spaces ("District " with space) - Requires `.str.strip()` in pandas
- **Area column:** Header contains trailing space but values appear clean - Apply `.str.strip()` to headers
- **Season column:** Contains trailing spaces (e.g., "Kharif     ") - Requires trimming and standardization

### Outliers & Data Quality Issues
- **Yield maximum:** 43,958 tonnes/ha (extreme outlier, likely data entry error) - Recommend percentile-based capping (e.g., 99th percentile) or domain expert verification
- **Production maximum:** 1.6 billion tonnes (verify if realistic) - Cross-check with state-level production statistics
- **Yield = 0:** Multiple records where Yield = 0 due to missing Production values - These correspond to null values in Production column
- **Zero/negative values:** Ensure Area and Production are always positive; flag any negative values as errors

### Data Consistency Notes
- **Seasonal coverage:** Not all states/crops are recorded for all seasons - Some crops are only Kharif or Rabi specific (e.g., rice vs. wheat)
- **Year coverage:** Data spans 1997-2020, but not all state-district-crop combinations have records for every year - This is expected due to regional crop patterns
- **Geographic hierarchy:** Some records may have missing District data - Use State-level aggregation for these cases
- **Crop standardization:** Crop names may have minor spelling variations across years - Standardize using exact string matching or fuzzy matching with threshold

### Recommended Cleaning Pipeline
1. **Step 1 (Load & Format):** Trim all string columns (State, District, Crop, Season)
2. **Step 2 (Validation):** Drop rows with null Crop; verify Area > 0
3. **Step 3 (Missing Production):** Apply imputation strategy (median by state-crop-season or drop rows)
4. **Step 4 (Outlier Treatment):** Flag/cap Yield > 99th percentile; verify Production > 1 billion
5. **Step 5 (KPI Calculation):** Create derived columns (Yield, YoY Growth, etc.) on cleaned data
6. **Step 6 (Export):** Save cleaned dataset to `data/processed/APY_cleaned.csv` for analysis

### Known Limitations
- Production data quality varies by state; Southern and Western India typically have better data coverage
- Some older years (1997-2002) may have sparse district-level data
- Yield calculated from survey estimates; actual farmer yields may vary within districts
- Climate and soil data not included; external weather datasets may be needed for advanced analysis
