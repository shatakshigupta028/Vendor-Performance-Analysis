# Vendor Performance Analysis

This project is an end-to-end Data Analytics case study that simulates a real-world business scenario. It focuses on analyzing vendor data using SQL, Python, and Power BI to optimize inventory, improve profitability and enhance sales performance.

---

## Tech Stack

- SQL (SQLite)
- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)
- Power BI

---

## Project Workflow

### 1. Data Engineering (SQL)
- Ingested raw CSV datasets into a database
- Cleaned and transformed data using SQL queries
- Merged multiple tables
- Created an aggregated **vendor summary table**

---

### 2. Exploratory Data Analysis (Python)
- Performed EDA using Pandas
- Visualized data using Matplotlib & Seaborn:
  - Histograms
  - Box plots (outlier detection)
  - Correlation heatmap
- Answered key business questions:
  - Identified underperforming brands
  - Found top-performing vendors

---

### 3. Statistical Analysis
- Calculated **confidence intervals** for profit margins
- Performed **hypothesis testing** to compare top vs low vendors

---

### 4. Dashboard (Power BI)
- Built an interactive dashboard showing:
  - Total Sales
  - Gross Profit
  - Inventory Turnover
  - Vendor Performance Rankings
 
  Screenshot-
  <img width="847" height="537" alt="image" src="https://github.com/user-attachments/assets/3e3a5e2a-2691-4b09-9bfa-84a9286e548e" />


---

## Key Insights

- Identified vendors contributing most to revenue (Pareto Analysis)
- Detected brands with high margins but low sales (promotion targets)
- Found statistically significant differences in vendor performance

---

## Dataset Note

The original dataset is ~2GB and cannot be uploaded to GitHub due to size limits.

A **sample dataset** is included for demonstration purposes.  

---

## Learnings

- Handling large datasets efficiently using chunking
- Writing optimized SQL queries for data aggregation
- Applying statistical analysis in business context
- Building end-to-end analytics pipelines

