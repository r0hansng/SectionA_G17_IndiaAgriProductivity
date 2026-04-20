# Viva-Voce Preparation Guide: India Agricultural Productivity Analysis

This guide prepares you for the likely questions an instructor might ask during a viva-voce based on the project code, logic, and analytical outcomes.

### 1. Data Cleaning & ETL (The Script)
**Q: Why did you use a separate `.py` script for cleaning instead of doing it all in the notebook?**
*   **Answer:** "It follows industrial best practices for modularity. Keeping the ETL logic in a central script ensures that if we have new data in the future, we can clean it exactly the same way without manually re-running notebook cells. It also makes the code easier to test and maintain."

**Q: Explain your 'Three-Tier Imputation' strategy for missing values.**
*   **Answer:** "Data wasn't just missing at random. Yield varies by state, crop, and season.
    1.  First, we filled nulls using the median for that specific **State, Crop, and Season**.
    2.  If data was still missing, we used the **Crop-wide median** across India.
    3.  Finally, we used the **Global median** as a fallback.
    We used **median** instead of **mean** because agricultural data often contains extreme outliers which would skew the average."

**Q: Why did you cap the yield at the 99th percentile?**
*   **Answer:** "Agricultural data often has human entry errors (e.g., entering 1000 instead of 100). These outliers would make our statistical analysis and charts very misleading. Capping at the 99th percentile keeps the high performers but eliminates impossible extreme values."

---

### 2. Statistical Analysis & KPIs
**Q: What is the 'Underperforming District Index' (UDI) you created?**
*   **Answer:** "It’s a benchmark-based KPI. For every record, we compare that district’s yield to the **National Median Yield** for that specific crop. If the yield is lower, we flag it as underperforming (1). This allows policy makers to ignore state-level averages and zoom in on specific districts that need help."

**Q: How did you calculate Year-over-Year (YoY) growth?**
*   **Answer:** "We used the `pct_change()` function in Pandas on the aggregated annual production. This helps us see if agricultural outputs are keeping up with population growth or if there are specific years with systemic failures (like droughts)."

---

### 3. Exploratory Data Analysis (EDA)
**Q: Which season did you find to be the most productive in India?**
*   **Answer:** "Our analysis shows that the **Kharif** season is the major contributor to production. However, from a yield perspective, **Summer/Rabi** crops often show higher efficiency despite having less total land area."

**Q: Why did you use a horizontal bar chart for some crops?**
*   **Answer:** "We used horizontal bars for the top crops because the labels (crop names like 'Sugarcane', 'Arecanut') are long. Horizontal bars make them easier to read than vertical bars where text would overlap."

---

### 4. Technical Coding Details
**Q: What libraries did you rely on and why?**
*   **Answer:**
    *   **Pandas:** For data manipulation and the 'Split-Apply-Combine' (groupby) logic.
    *   **Seaborn/Matplotlib:** For professional-grade plotting.
    *   **Pathlib:** For robust file path management across different operating systems.

**Q: What was the most challenging part of the code to write?**
*   **Answer:** "Managing the `groupby().apply()` logic for imputation. We had to ensure that the grouping keys (State, Crop, Season) were consistently cleaned of whitespace first, otherwise, 'Rice ' and 'Rice' would be treated as different crops, leading to incorrect medians."

---

### 5. Final Recommendations (The "So What?")
**Q: If you were the Agriculture Minister, how would you use this project?**
*   **Answer:** "I would use the **UDI mapping** from the Tableau dashboard to identify top-priority districts. Instead of giving broad subsidies to an entire state, I would target specific soil health cards and irrigation projects only to those districts that are underperforming compared to the national median."

### Sudden "Pop Quiz" Questions:
*   **"What happens to your code if the CSV has a new column added?"** -> "The `normalize_columns` function will automatically handle it, converting it to snake_case and trimming it, but it won't affect our specific KPI logic unless the core column names change."
*   **"Is the data updated in 2024?"** -> "No, the dataset covers roughly 1997 to 2020. Our pipeline is designed to be 'future-proof' so we can just swap in a newer CSV later."
