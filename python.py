import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_excel(
    "online_retail_II.xlsx",
    sheet_name="Year 2010-2011"
)

# BASIC DATA UNDERSTANDING


print(data.head())

print(data.shape)

print(data.columns)

print(data.info())

print(data.isnull().sum())


# DATA CLEANING


# Remove extra spaces in column names
data.columns = data.columns.str.strip()

# Remove duplicate rows
data = data.drop_duplicates()

# Convert date column
data["InvoiceDate"] = pd.to_datetime(
    data["InvoiceDate"],
    errors="coerce"
)

# Remove missing important values
data = data.dropna(
    subset=[
        "Invoice",
        "StockCode",
        "Description",
        "Quantity",
        "Price",
        "InvoiceDate"
    ]
)

# Remove invalid quantity
data = data[data["Quantity"] > 0]

# Remove invalid price
data = data[data["Price"] > 0]


# FEATURE ENGINEERING


# Total sales column
data["TotalSales"] = (
    data["Quantity"] * data["Price"]
)

# Month column
data["Month"] = (
    data["InvoiceDate"].dt.month
)

# Year-Month column
data["YearMonth"] = (
    data["InvoiceDate"]
    .dt.to_period("M")
    .astype(str)
)

# Day name column
data["DayName"] = (
    data["InvoiceDate"]
    .dt.day_name()
)


# KPI ANALYSIS


total_revenue = data["TotalSales"].sum()

total_orders = data["Invoice"].nunique()

total_customers = data["Customer ID"].nunique()

avg_order_value = (
    data.groupby("Invoice")["TotalSales"]
    .sum()
    .mean()
)

print("Total Revenue:", total_revenue)

print("Total Orders:", total_orders)

print("Total Customers:", total_customers)

print("Average Order Value:", avg_order_value)

# TOP 10 COUNTRIES BY SALES


country_sales = (
    data.groupby("Country")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(country_sales)

# Bar chart
country_sales.plot(
    kind="bar",
    figsize=(10,5),
    title="Top 10 Countries by Revenue"
)

plt.ylabel("Revenue")
plt.show()


# TOP 10 PRODUCTS


top_products = (
    data.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

top_products.plot(
    kind="bar",
    figsize=(12,5),
    title="Top 10 Products Sold"
)

plt.ylabel("Quantity Sold")
plt.show()


# MONTHLY SALES TREND


monthly_sales = (
    data.groupby("YearMonth")["TotalSales"]
    .sum()
)

print(monthly_sales)

monthly_sales.plot(
    kind="line",
    figsize=(12,5),
    title="Monthly Revenue Trend"
)

plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()


# TOP 10 CUSTOMERS BY REVENUE


top_customers = (
    data.groupby("Customer ID")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)

top_customers.plot(
    kind="bar",
    figsize=(10,5),
    title="Top 10 Customers by Revenue"
)

plt.ylabel("Revenue")
plt.show()


# REPEAT CUSTOMER ANALYSIS


customer_orders = (
    data.groupby("Customer ID")["Invoice"]
    .nunique()
)

repeat_customers = (
    customer_orders[customer_orders > 1]
    .count()
)

one_time_customers = (
    customer_orders[customer_orders == 1]
    .count()
)

print("Repeat Customers:", repeat_customers)

print("One-Time Customers:", one_time_customers)


# TOP DAYS FOR SALES


day_sales = (
    data.groupby("DayName")["TotalSales"]
    .sum()
)

print(day_sales)

day_sales.plot(
    kind="bar",
    figsize=(10,5),
    title="Revenue by Day"
)

plt.ylabel("Revenue")
plt.show()'''

