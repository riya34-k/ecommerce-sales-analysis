🛒 E-Commerce Sales Analysis (SQL + Python + Tableau)

Analysing 4 years of superstore sales data to uncover regional performance, category profitability, and growth trends.

📌 Problem Statement

A retail superstore wants to understand which regions, product categories, and sub-categories are driving profit — and which are causing losses. This project uses SQL for querying, Python for analysis and visualisation, and Tableau for an interactive dashboard to answer these business questions.

📂 Dataset

Source: Superstore Dataset — Kaggle
Size: 9,994 rows × 21 columns
Period: 2014 – 2017
Features include: Order ID, Order Date, Region, Category, Sub-Category, Sales, Profit, Quantity, Discount, Segment, Ship Mode

🛠️ Tools & Technologies
Category   Tools
Language   Python 3
Database   SQLite (via Python sqlite3)
Data Analysis Pandas, NumPy
Visualisation Matplotlib, Seaborn
Dashboard     Tableau Desktop
Environment   VS Code

🔍 Project Workflow
1. Data Loading & Cleaning

Loaded CSV using Pandas with latin-1 encoding
Converted Order Date and Ship Date to datetime format
Extracted Order Year and Order Month as new features
Zero null values found — no rows dropped

2. SQL Analysis (SQLite)

Loaded the cleaned dataframe into a SQLite database and wrote 5 business queries:
Query                      Business Question
Sales & Profit by Region   Which region generates the most revenue?
Sales & Profit by Category Which product category is most profitable?
Yearly Sales Trend         Is the business growing year over year?
Top 5 Profitable Sub-Categories Where should we focus our efforts?
Loss Making Sub-Categories  Which sub-categories are hurting profit?

3. Python Visualisations
Generated 5 charts using Matplotlib and Seaborn:

Total Sales by Region (bar chart)
Total Profit by Category (bar chart)
Yearly Sales & Profit Trend 2014–2017 (line chart)
Top 5 Most Profitable Sub-Categories (horizontal bar)
Loss Making Sub-Categories (horizontal bar)

4. Tableau Dashboard
Built an interactive 4-panel dashboard in Tableau showing all key insights in one view.

📊 Key Findings
Insight                      Finding
Top region                   West leads with $725,457 in sales
Most profitable category     Technology — $145,454 profit
Furniture problem            High sales ($741,999) but very low profit ($18,451) — discounts killing margins
Sales growth                 Business grew from $484K (2014) to $733K (2017) — 51% growth
Best sub-category            Copiers — $55,617 profit on $149,528 sales (37% margin)
Worst sub-category           Tables — losing $17,725 despite reasonable sales
2015 dip                     Sales dipped in 2015 before strong recovery — worth investigating

💡 Business Recommendations

Reduce discounts on Furniture — especially Tables and Bookcases which are loss-making despite decent sales volume
Push Copiers and Phones — highest profit margins, focus marketing here
Invest in West and East regions — top performing, more growth potential
Review Central region strategy — high sales but profit margin is lower than South
Investigate 2015 dip — understanding why sales dropped helps prevent recurrence

📁 Project Structure
ecommerce-sales-analysis/
│
├── data/
│   └── Sample - Superstore.csv
│
├── analysis.py
├── superstore.db
├── chart1_sales_by_region.png
├── chart2_profit_by_category.png
├── chart3_yearly_trend.png
├── chart4_top_subcategories.png
├── chart5_loss_subcategories.png
├── tableau_dashboard.png
└── README.md

🚀 How to Run
# 1. Clone the repo
git clone https://github.com/riya34-k/ecommerce-sales-analysis.git

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn

# 3. Run the analysis
python analysis.py
