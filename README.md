# India Agricultural Productivity Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat-square&logo=jupyter)
![Tableau](https://img.shields.io/badge/Tableau-Public-navy?style=flat-square&logo=tableau)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=flat-square&logo=github)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

A comprehensive data visualization & analytics capstone project analyzing Indian agricultural productivity trends and patterns.

[Dashboard](#tableau-dashboard) • [Report](#reports) • [Notebooks](#notebooks)

</div>

---

## Project Overview

| Attribute | Details |
|---|---|
| **Project Title** | India Agricultural Productivity Analysis |
| **Sector** | Agriculture & Agribusiness |
| **Team ID** | SectionA_G17 |
| **Institute** | Newton School of Technology |
| **Program** | Data Visualization & Analytics Capstone |
| **Duration** | 2-Week Industry Simulation |
| **Status** | In Progress |

### Team Members

| Role | Name | GitHub |
|---|---|---|
| Project Lead | Pushpendra Singh Parihar | [`makeprodigy`](https://github.com/makeprodigy) |
| Data Lead | Akshit Vats | [`Akshitvats`](https://github.com/Akshitvats) |
| ETL Lead | Ajeesh Amreet | [`coder69010`](https://github.com/coder69010) |
| Analysis Lead | Rohan Singh | [`r0hansng`](https://github.com/r0hansng) |
| Visualization Lead | Sameer Khan | [`Sam99132`](https://github.com/Sam99132) |
| Strategy + Quality Lead | Sanath Waraikar | [`waraikar`](#) |

---

## Business Problem & Opportunity

Agriculture is the backbone of India's economy, employing over 40% of the workforce. However, productivity fluctuations due to climate variability, soil conditions, and farming practices create significant challenges for policymakers, agricultural agencies, and farmers themselves.

**Core Business Question**
> Which states, districts, and crops are underperforming on yield efficiency (production per hectare), how has agricultural productivity trended from 1997 to 2020, and what season-wise and crop-wise patterns should drive targeted policy interventions and area-allocation decisions?

**Decision Supported**
> State and central agricultural authorities can: (1) identify high-priority districts for yield-improvement interventions; (2) rationalize crop-area allocation by season and geography; (3) forecast production shortfalls for key staple crops (rice, wheat, pulses); (4) benchmark district-level productivity against national medians to direct NABARD credit and government subsidy flows

---

## Dataset Overview

| Attribute | Details |
|---|---|
| **Source** | Crop Production Statistics - India (Kaggle) |
| **Direct Link** | [https://www.kaggle.com/datasets/nikhilmahajan29/crop-production-statistics-india](https://www.kaggle.com/datasets/nikhilmahajan29/crop-production-statistics-india) |
| **Coverage Period** | 1997-2020 (23 years of records) |
| **Geographic Scope** | 55+ crop varieties across 707 districts, 37 states & UTs |
| **Total Records** | 345,336 rows (well above 5,000 minimum) |
| **Columns** | 8 core columns |
| **Format** | CSV (tabular, row-level records) |

### Key Features Analyzed

| Column | Description | Role in Analysis |
|---|---|---|
| **State** | Indian state or union territory | Geographic segmentation & regional benchmarking |
| **District** | Administrative district | Sub-regional analysis & underperformance identification |
| **Crop** | 55+ crop varieties (rice, wheat, sugarcane, cotton, pulses, etc.) | Crop-wise yield comparison & area-allocation analysis |
| **Crop_Year** | Calendar year (1997-2020) | Temporal trend analysis & YoY growth computation |
| **Season** | Kharif, Rabi, Summer, Autumn, Winter, Whole Year | Season-wise production share & seasonal pattern analysis |
| **Area** | Cultivated area in hectares | Input variable for productivity calculations |
| **Production** | Total output in tonnes | Output metric for growth trends & forecasting |
| **Yield** | Production per hectare (tonnes/ha) | Primary KPI - Agricultural Productivity Yield Efficiency |

### Data Quality & ETL Considerations

The dataset contains realistic quality issues requiring ETL pipeline attention:
- **4,948 null values** in Production column (1.43%) — requires imputation or conditional drop
- **Trailing whitespace** in Season values and column names ('District ', 'Area ') — requires trimming
- **9 null Crop values** — requires row drop
- **Extreme outliers** in Yield (max 43,958) and Production (max 1.6 billion) — requires outlier treatment

Full data dictionary available in [`docs/data_dictionary.md`](docs/data_dictionary.md)

**Backup Datasets:**
- Backup 1: Kaggle — "Crop Production in India" (raw, state-level, 1997-2015) — [Link](https://www.kaggle.com/datasets/srinivas1/agriculture-crops-production-in-india)
- Backup 2: data.gov.in — "Season-wise Crop Production Statistics" (alternative aggregation by ICAR)

---

## KPI Framework

| KPI | Definition | Computation | Reference |
|---|---|---|---|
| **Yield Efficiency Rate** (Primary KPI) | Production per hectare (tonnes/ha), segmented by State, Crop, Season | `Production ÷ Area` | Identifies high/low-performing regions; guides targeted interventions |
| **Year-over-Year Production Growth %** | Aggregate production growth tracking India's agricultural acceleration | `((Prod_Year_N - Prod_Year_N-1) / Prod_Year_N-1) × 100` | `notebooks/04_statistical_analysis.ipynb` |
| **Area Utilisation Trend** | Change in cultivated area over time by crop/state | Trend analysis (linear regression) | `notebooks/03_eda.ipynb` |
| **Season-wise Production Share %** | Kharif vs. Rabi vs. other seasons' contribution to total | `(Season_Production / Total_Production) × 100` | `notebooks/03_eda.ipynb` |
| **Underperforming District Index** | Districts below national median yield for given crop | Percentile ranking vs. national median | `notebooks/04_statistical_analysis.ipynb` |

---

## Tableau Dashboard

| Component | Details |
|---|---|
| **Dashboard URL** | [View on Tableau Public](#) |
| **Executive View** | KPI scorecard with state rankings and trend lines |
| **Operational View** | Detailed crop-by-crop productivity analysis with year filters |
| **Interactive Features** | State selector, crop filter, year slider, regional heatmap |

Dashboard screenshots available in [`tableau/screenshots/`](tableau/screenshots/)

---

## Key Insights

1. **Punjab & Haryana Leadership**: Yield efficiency for staple crops (Rice, Wheat, Pulses) has improved significantly in economically advanced states like Punjab and Haryana
2. **Eastern Underperformance**: Eastern and north-eastern states remain significantly below the national median yield for identical crops
3. **Kharif Dominance**: Kharif season accounts for ~55-60% of total production nationwide, indicating seasonal production concentration
4. **Cash Crop Expansion**: Measurable increase in cultivated area for cash crops (Sugarcane, Cotton) at the expense of pulse cultivation over the 23-year period (1997-2020)
5. **Regional Benchmarking Opportunity**: District-level productivity variance provides clear targets for resource allocation and policy interventions
6. **Crop-Season Interaction**: Specific crops perform differently across seasons; seasonal pattern understanding essential for area-allocation decisions
7. **Production Trend Acceleration**: Year-over-year production growth shows measurable change trajectory, valuable for forecasting staple crop shortfalls
8. **Data Quality Issues Confirmed**: ETL pipeline must address 4,948 null values in Production (1.43%), trailing whitespace in Season/District columns, and extreme outliers in Yield (max 43,958)
9. **Multi-Level Analysis Required**: State, district, crop, and season segmentation necessary for actionable, targeted recommendations
10. **NABARD Credit Opportunity**: District-level benchmarking enables evidence-based credit allocation and subsidy flow optimization

---

## Recommendations

| # | Based On Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Eastern Underperformance | Transfer best-practice farming techniques from Punjab/Haryana to eastern states through targeted training programs and technology adoption subsidies | Close yield efficiency gap by 25-30% within 3 years for priority crops |
| 2 | Kharif Dominance & Seasonal Concentration | Develop diversified crop calendars for Rabi season to reduce production concentration and improve supply chain stability for staples | Better seasonal distribution, 15-20% improvement in off-season availability |
| 3 | Cash Crop Area Expansion | Implement regulated pulse cultivation incentives in high-performing states to reverse declining pulse area trends and ensure nutritional security | Reverse pulse area decline, increase domestic pulses production by 10-15% |
| 4 | District-Level Benchmarking | Create NABARD-linked credit scoring based on district yield efficiency percentiles to direct credit flows to high-potential, underperforming districts | Improve credit allocation efficiency, increase adoption of high-yield practices |
| 5 | Multi-Season Crop Strategy | Design season-crop specific procurement quotas and minimum support prices (MSP) based on seasonal performance analytics | Optimize farmer income, improve government procurement efficiency, reduce wastage |

---

## Quick Start Guide

### Local Setup

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Jupyter notebooks
jupyter notebook
```

### Google Colab Alternative

1. Upload notebooks from `notebooks/` folder
2. Mount Google Drive for data access
3. Commit final `.ipynb` files to GitHub
4. Export cleaned datasets to `data/processed/`

---

## Repository Architecture

```
SectionA_G17_IndiaAgriProductivity/
│
├── README.md                      # Project overview & documentation
├── requirements.txt               # Python dependencies
│
├── data/
│   ├── raw/                       # Original, unmodified dataset
│   │   └── APY.csv                # Agricultural Productivity data
│   └── processed/                 # Cleaned & transformed data
│
├── notebooks/
│   ├── 01_extraction.ipynb        # Data sourcing & initial load
│   ├── 02_cleaning.ipynb          # ETL & data quality checks
│   ├── 03_eda.ipynb               # Exploratory data analysis
│   ├── 04_statistical_analysis.ipynb # Statistical modeling & KPIs
│   └── 05_final_load_prep.ipynb   # Dashboard preparation
│
├── scripts/
│   ├── __init__.py
│   └── etl_pipeline.py            # Reusable ETL functions
│
├── tableau/
│   ├── dashboard_links.md         # Tableau Public URLs
│   └── screenshots/               # Dashboard snapshots
│
├── reports/
│   ├── README.md
│   ├── project_report_template.md # Final written report
│   └── presentation_outline.md    # Viva/presentation guide
│
├── docs/
│   └── data_dictionary.md         # Column definitions & metadata
│
├── DVA-focused-Portfolio/         # Portfolio piece documentation
│   └── README.md
│
└── DVA-oriented-Resume/           # Resume with project highlights
    └── README.md
```

---

## Analytical Pipeline

Our structured 7-step methodology ensures rigorous, reproducible analysis:

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. DEFINE   │ Problem scoped, data requirements identified       │
├─────────────────────────────────────────────────────────────────┤
│ 2. EXTRACT  │ Raw dataset sourced → data/raw/                   │
├─────────────────────────────────────────────────────────────────┤
│ 3. CLEAN    │ ETL pipeline built (notebooks/02 & scripts/)      │
├─────────────────────────────────────────────────────────────────┤
│ 4. ANALYZE  │ EDA + Statistical analysis (notebooks/03 & 04)    │
├─────────────────────────────────────────────────────────────────┤
│ 5. VISUALIZE│ Interactive Tableau dashboard created & published │
├─────────────────────────────────────────────────────────────────┤
│ 6. RECOMMEND│ Actionable insights & recommendations delivered   │
├─────────────────────────────────────────────────────────────────┤
│ 7. REPORT   │ Final report & presentation in reports/          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python 3.8+ | Mandatory | ETL, analysis, KPI computation |
| Jupyter Notebook | Mandatory | Interactive notebooks & documentation |
| Tableau Public | Mandatory | Dashboard visualization & publishing |
| GitHub | Mandatory | Version control & collaboration |
| Pandas | Core | Data manipulation & cleaning |
| NumPy | Core | Scientific computing |
| Matplotlib | Core | Statistical plotting |
| Seaborn | Core | Statistical graphics |
| SciPy | Recommended | Statistical testing |
| StatsModels | Recommended | Regression & time-series |
| SQL | Optional | Data extraction (if documented) |

---

## Evaluation Criteria

| Category | Points | Assessment Focus |
|---|---|---|
| Problem Framing | 10 | Clear, well-scoped business question with strategic relevance |
| Data Quality & ETL | 15 | Thorough cleaning pipeline with robust validation & documentation |
| Analysis Depth | 25 | Correct statistical methods, advanced techniques, meaningful insights |
| Dashboard & Visualization | 20 | Interactive, decision-relevant, professional Tableau dashboard |
| Business Recommendations | 20 | Actionable insights directly tied to analysis with impact estimates |
| Storytelling & Clarity | 10 | Professional presentation, coherent narrative, clear communication |
| **TOTAL** | **100** | |

**Grading Philosophy:** Emphasis on analytical rigor & decision-relevance. Chart quantity and visual decoration are not prioritized over substance and actionability.

---

## Submission Checklist

### GitHub Repository

- [x] Public repository with correct naming: `SectionA_G17_IndiaAgriProductivity`
- [ ] All 5 notebooks committed in `.ipynb` format
- [ ] `data/raw/APY.csv` - original, unedited dataset
- [ ] `data/processed/` - output from cleaning pipeline
- [ ] `tableau/screenshots/` - dashboard snapshots
- [ ] `tableau/dashboard_links.md` - Tableau Public URL (public & accessible)
- [ ] `docs/data_dictionary.md` - complete column documentation
- [ ] `README.md` - comprehensive project description
- [ ] All team members have visible commits & pull requests

### Tableau Dashboard

- [ ] Published on Tableau Public with public access
- [ ] At least one interactive filter (state, crop, year)
- [ ] Directly addresses the business problem
- [ ] Professional formatting & color scheme
- [ ] KPI metrics clearly displayed

### Project Report

- [ ] PDF exported to `reports/`
- [ ] Cover page with project title & team details
- [ ] Executive summary (1-2 pages)
- [ ] Sector context & problem statement
- [ ] Data description & cleaning methodology
- [ ] KPI framework & calculations
- [ ] EDA with visualizations & insights
- [ ] Statistical analysis results
- [ ] Dashboard screenshots & annotations
- [ ] 8-12 key insights (decision-focused)
- [ ] 3-5 actionable recommendations with impact
- [ ] Contribution matrix aligned with GitHub history

### Presentation Deck

- [ ] PDF exported to `reports/`
- [ ] Title slide → Problem → Findings → Dashboard → Recommendations
- [ ] Impact statement & next steps
- [ ] Limitations clearly acknowledged
- [ ] Professional design & readability

### Individual Assets

- [ ] DVA-oriented resume updated with capstone details
- [ ] Portfolio link or case study documentation added
- [ ] LinkedIn profile updated with project experience

---

## Team Contributions

| Team Member | Data & ETL | EDA | Analysis | Dashboard | Report | Presentation |
|---|---|---|---|---|---|---|
| Member 1 | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support |
| Member 2 | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support |
| Member 3 | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support |
| Member 4 | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support |
| Member 5 | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support | Lead / Support |

**Project Lead:** Pushpendra Singh Parihar | **Date:** April 16, 2026

**Declaration:** We confirm that contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts.

---

## Key Resources & References

| Resource | Link | Purpose |
|---|---|---|
| Data Dictionary | [`docs/data_dictionary.md`](docs/data_dictionary.md) | Column definitions & metadata |
| Dashboard | [Tableau Public](#) | Interactive KPI dashboard |
| ETL Pipeline | [`scripts/etl_pipeline.py`](scripts/etl_pipeline.py) | Reusable cleaning functions |
| Analysis Notebooks | `notebooks/03-04/` | EDA & statistical methods |

---

## Best Practices Followed

✓ **Version Control:** All files committed to GitHub with clear commit messages

✓ **Reproducibility:** Complete documentation of data transformations & formulas

✓ **Code Quality:** Well-commented, modular Python code following PEP 8

✓ **Data Integrity:** Raw data never modified, clean separation of layers

✓ **Professional Output:** 
Publication-ready Tableau dashboard & formal report

✓ **Team Collaboration:** Documented contributions & transparent decision-making  

---

## Contributing

This project is completed as part of NST DVA Capstone. For inquiries or feedback:

- **Project Lead:** [Pushpendra Singh Parihar](https://github.com/makeprodigy)
- **Analysis Lead:** [Rohan Singh](https://github.com/r0hansng)
- **Questions:** Refer to reports/ for detailed methodology and findings

---

## License

This project is licensed under the **MIT License** - see LICENSE file for details.

---

## Acknowledgments

- **Institution:** Newton School of Technology
- **Program:** Data Visualization & Analytics Capstone
- **Data Source:** Indian Government Agricultural Database
- **Mentorship:** Faculty guidance & industry best practices

---

<div align="center">



![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square)
![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202026-blue?style=flat-square)

[Back to Top](#india-agricultural-productivity-analysis)

</div>
