import pandas as pd
df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nNull values:")
print(df.isnull().sum())
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
print("Date range:", df["Order Date"].min(), "to", df["Order Date"].max())
print("Years in data:", df["Order Year"].unique())
print("\nSample after cleaning:")
print(df[["Order Date", "Order Year", "Order Month"]].head())
import sqlite3
conn = sqlite3.connect("superstore.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
print("Data loaded into SQLite successfully!")
cursor = conn.cursor()
print("\n=== Total Sales & Profit by Region ===")
query1 = """
    SELECT Region, 
           ROUND(SUM(Sales), 2) AS Total_Sales,
           ROUND(SUM(Profit), 2) AS Total_Profit
    FROM sales
    GROUP BY Region
    ORDER BY Total_Sales DESC
"""
result1 = pd.read_sql_query(query1, conn)
print(result1)
print("\n=== Sales by Category ===")
query2 = """
    SELECT Category,
           ROUND(SUM(Sales), 2) AS Total_Sales,
           ROUND(SUM(Profit), 2) AS Total_Profit,
           ROUND(AVG(Discount)*100, 1) AS Avg_Discount_Pct
    FROM sales
    GROUP BY Category
    ORDER BY Total_Sales DESC
"""
result2 = pd.read_sql_query(query2, conn)
print(result2)
print("\n=== Yearly Sales Trend ===")
query3 = """
    SELECT [Order Year],
           ROUND(SUM(Sales), 2) AS Total_Sales,
           ROUND(SUM(Profit), 2) AS Total_Profit
    FROM sales
    GROUP BY [Order Year]
    ORDER BY [Order Year]
"""
result3 = pd.read_sql_query(query3, conn)
print(result3)
print("\n=== Top 5 Profitable Sub-Categories ===")
query4 = """
    SELECT [Sub-Category],
           ROUND(SUM(Profit), 2) AS Total_Profit,
           ROUND(SUM(Sales), 2) AS Total_Sales
    FROM sales
    GROUP BY [Sub-Category]
    ORDER BY Total_Profit DESC
    LIMIT 5
"""
result4 = pd.read_sql_query(query4, conn)
print(result4)
print("\n=== Loss Making Sub-Categories ===")
query5 = """
    SELECT [Sub-Category],
           ROUND(SUM(Profit), 2) AS Total_Profit
    FROM sales
    GROUP BY [Sub-Category]
    HAVING Total_Profit < 0
    ORDER BY Total_Profit ASC
"""
result5 = pd.read_sql_query(query5, conn)
print(result5)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)
plt.figure()
sns.barplot(data=result1, x="Region", y="Total_Sales", palette="Blues_d")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("chart1_sales_by_region.png")
plt.show()
print("Chart 1 saved!")
plt.figure()
sns.barplot(data=result2, x="Category", y="Total_Profit", palette="Greens_d")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit ($)")
plt.tight_layout()
plt.savefig("chart2_profit_by_category.png")
plt.show()
print("Chart 2 saved!")
plt.figure()
plt.plot(result3["Order Year"], result3["Total_Sales"], marker="o", color="steelblue", linewidth=2.5, label="Sales")
plt.plot(result3["Order Year"], result3["Total_Profit"], marker="o", color="green", linewidth=2.5, label="Profit")
plt.title("Yearly Sales & Profit Trend (2014-2017)")
plt.xlabel("Year")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.savefig("chart3_yearly_trend.png")
plt.show()
print("Chart 3 saved!")
plt.figure()
sns.barplot(data=result4, x="Total_Profit", y="Sub-Category", palette="Oranges_d")
plt.title("Top 5 Most Profitable Sub-Categories")
plt.xlabel("Total Profit ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("chart4_top_subcategories.png")
plt.show()
print("Chart 4 saved!")
plt.figure()
sns.barplot(data=result5, x="Total_Profit", y="Sub-Category", palette="Reds_d")
plt.title("Loss Making Sub-Categories")
plt.xlabel("Total Profit ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("chart5_loss_subcategories.png")
plt.show()
print("Chart 5 saved!")