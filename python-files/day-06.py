#!/usr/bin/env python
# coding: utf-8

# # Day 6: Ice Cream Sales Seasonal Performance Assessment

# You are a Product Insights Analyst working with the Ben & Jerry's sales strategy team to investigate seasonal sales patterns through comprehensive data analysis. The team wants to understand how temperature variations and unique transaction characteristics impact ice cream sales volume. Your goal is to perform detailed data cleaning and exploratory analysis to uncover meaningful insights about seasonal sales performance.

# In[ ]:


import pandas as pd
import numpy as np

ice_cream_sales_data_data = [
  {
    "sale_date": "2024-07-05",
    "temperature": 62,
    "product_name": "Cherry Garcia",
    "sales_volume": 23,
    "transaction_id": "TX0001"
  },
  {
    "sale_date": "2024-08-15",
    "temperature": 64,
    "product_name": "Chunky Monkey",
    "sales_volume": 26,
    "transaction_id": "TX0002"
  },
  {
    "sale_date": "2024-09-25",
    "temperature": 66,
    "product_name": "Phish Food",
    "sales_volume": 29,
    "transaction_id": "TX0003"
  },
  {
    "sale_date": "2024-10-05",
    "temperature": 68,
    "product_name": "Americone Dream",
    "sales_volume": 32,
    "transaction_id": "TX0004"
  },
  {
    "sale_date": "2024-11-15",
    "temperature": 70,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 35,
    "transaction_id": "TX0005"
  },
  {
    "sale_date": "2024-12-25",
    "temperature": 72,
    "product_name": "Half Baked",
    "sales_volume": 38,
    "transaction_id": "TX0006"
  },
  {
    "sale_date": "2025-01-05",
    "temperature": 74,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 41,
    "transaction_id": "TX0007"
  },
  {
    "sale_date": "2025-02-15",
    "temperature": 76,
    "product_name": "Cherry Garcia",
    "sales_volume": 44,
    "transaction_id": "TX0008"
  },
  {
    "sale_date": "2025-03-25",
    "temperature": 78,
    "product_name": "Chunky Monkey",
    "sales_volume": 47,
    "transaction_id": "TX0009"
  },
  {
    "sale_date": "2025-04-05",
    "temperature": 80,
    "product_name": "Phish Food",
    "sales_volume": 50,
    "transaction_id": "TX0010"
  },
  {
    "sale_date": "2025-05-15",
    "temperature": 82,
    "product_name": "Americone Dream",
    "sales_volume": 53,
    "transaction_id": "TX0011"
  },
  {
    "sale_date": "2025-06-25",
    "temperature": 84,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 1000,
    "transaction_id": "TX0012"
  },
  {
    "sale_date": "2024-07-05",
    "temperature": 86,
    "product_name": "Half Baked",
    "sales_volume": 59,
    "transaction_id": "TX0013"
  },
  {
    "sale_date": "2024-08-15",
    "temperature": 88,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 62,
    "transaction_id": "TX0014"
  },
  {
    "sale_date": "2024-09-25",
    "temperature": 90,
    "product_name": "Cherry Garcia",
    "sales_volume": 65,
    "transaction_id": "TX0015"
  },
  {
    "sale_date": "2024-10-05",
    "temperature": 61,
    "product_name": "Chunky Monkey",
    "sales_volume": 68,
    "transaction_id": "TX0016"
  },
  {
    "sale_date": "2024-11-15",
    "temperature": 63,
    "product_name": "Phish Food",
    "sales_volume": 71,
    "transaction_id": "TX0017"
  },
  {
    "sale_date": "2024-12-25",
    "temperature": 65,
    "product_name": "Americone Dream",
    "sales_volume": 74,
    "transaction_id": "TX0018"
  },
  {
    "sale_date": "2025-01-05",
    "temperature": 67,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 77,
    "transaction_id": "TX0019"
  },
  {
    "sale_date": "2025-02-15",
    "temperature": 105,
    "product_name": "Half Baked",
    "sales_volume": 80,
    "transaction_id": "TX0020"
  },
  {
    "sale_date": "2025-03-25",
    "temperature": 71,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 83,
    "transaction_id": "TX0021"
  },
  {
    "sale_date": "2025-04-05",
    "temperature": null,
    "product_name": "Cherry Garcia",
    "sales_volume": 86,
    "transaction_id": "TX0022"
  },
  {
    "sale_date": "2025-05-15",
    "temperature": 75,
    "product_name": "Chunky Monkey",
    "sales_volume": 89,
    "transaction_id": "TX0023"
  },
  {
    "sale_date": "2025-06-25",
    "temperature": 77,
    "product_name": "Phish Food",
    "sales_volume": 92,
    "transaction_id": "TX0024"
  },
  {
    "sale_date": "2024-07-05",
    "temperature": 79,
    "product_name": "Americone Dream",
    "sales_volume": 95,
    "transaction_id": "TX0025"
  },
  {
    "sale_date": "2024-08-15",
    "temperature": 81,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 98,
    "transaction_id": "TX0026"
  },
  {
    "sale_date": "2024-09-25",
    "temperature": 83,
    "product_name": "Half Baked",
    "sales_volume": 101,
    "transaction_id": "TX0027"
  },
  {
    "sale_date": "2024-10-05",
    "temperature": 85,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 104,
    "transaction_id": "TX0028"
  },
  {
    "sale_date": "2024-11-15",
    "temperature": 87,
    "product_name": "Cherry Garcia",
    "sales_volume": 107,
    "transaction_id": "TX0029"
  },
  {
    "sale_date": "2024-12-25",
    "temperature": 89,
    "product_name": "Chunky Monkey",
    "sales_volume": 110,
    "transaction_id": "TX0030"
  },
  {
    "sale_date": "2025-01-05",
    "temperature": 60,
    "product_name": "Phish Food",
    "sales_volume": 113,
    "transaction_id": "TX0031"
  },
  {
    "sale_date": "2025-02-15",
    "temperature": 62,
    "product_name": "Americone Dream",
    "sales_volume": 116,
    "transaction_id": "TX0032"
  },
  {
    "sale_date": "2025-03-25",
    "temperature": 64,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 119,
    "transaction_id": "TX0033"
  },
  {
    "sale_date": "2025-04-05",
    "temperature": 66,
    "product_name": "Half Baked",
    "sales_volume": 122,
    "transaction_id": "TX0034"
  },
  {
    "sale_date": "2025-05-15",
    "temperature": 68,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 125,
    "transaction_id": "TX0035"
  },
  {
    "sale_date": "2025-06-25",
    "temperature": 70,
    "product_name": "Cherry Garcia",
    "sales_volume": 128,
    "transaction_id": "TX0036"
  },
  {
    "sale_date": "2024-07-05",
    "temperature": 72,
    "product_name": "Chunky Monkey",
    "sales_volume": 1200,
    "transaction_id": "TX0037"
  },
  {
    "sale_date": "2024-08-15",
    "temperature": 74,
    "product_name": "Phish Food",
    "sales_volume": 134,
    "transaction_id": "TX0038"
  },
  {
    "sale_date": "2024-09-25",
    "temperature": 76,
    "product_name": "Americone Dream",
    "sales_volume": 137,
    "transaction_id": "TX0039"
  },
  {
    "sale_date": "2024-10-05",
    "temperature": 78,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 140,
    "transaction_id": "TX0040"
  },
  {
    "sale_date": "2024-11-15",
    "temperature": 80,
    "product_name": "Half Baked",
    "sales_volume": 143,
    "transaction_id": "TX0041"
  },
  {
    "sale_date": "2024-12-25",
    "temperature": 82,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 146,
    "transaction_id": "TX0042"
  },
  {
    "sale_date": "2025-01-05",
    "temperature": 84,
    "product_name": "Cherry Garcia",
    "sales_volume": 149,
    "transaction_id": "TX0043"
  },
  {
    "sale_date": "2025-02-15",
    "temperature": 86,
    "product_name": "Chunky Monkey",
    "sales_volume": 22,
    "transaction_id": "TX0044"
  },
  {
    "sale_date": "2025-03-25",
    "temperature": 40,
    "product_name": "Phish Food",
    "sales_volume": 25,
    "transaction_id": "TX0045"
  },
  {
    "sale_date": "2025-04-05",
    "temperature": 90,
    "product_name": "Americone Dream",
    "sales_volume": 28,
    "transaction_id": "TX0046"
  },
  {
    "sale_date": "2025-05-15",
    "temperature": 61,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 31,
    "transaction_id": "TX0047"
  },
  {
    "sale_date": "2025-06-25",
    "temperature": 63,
    "product_name": "Half Baked",
    "sales_volume": 34,
    "transaction_id": "TX0048"
  },
  {
    "sale_date": "2024-07-05",
    "temperature": 65,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 37,
    "transaction_id": "TX0049"
  },
  {
    "sale_date": "2024-08-15",
    "temperature": 67,
    "product_name": "Cherry Garcia",
    "sales_volume": 40,
    "transaction_id": "TX0050"
  },
  {
    "sale_date": "2024-09-25",
    "temperature": 69,
    "product_name": "Chunky Monkey",
    "sales_volume": 43,
    "transaction_id": "TX0051"
  },
  {
    "sale_date": "2024-10-05",
    "temperature": 71,
    "product_name": "Phish Food",
    "sales_volume": 46,
    "transaction_id": "TX0052"
  },
  {
    "sale_date": "2024-11-15",
    "temperature": 73,
    "product_name": "Americone Dream",
    "sales_volume": 49,
    "transaction_id": "TX0053"
  },
  {
    "sale_date": "2024-12-25",
    "temperature": 75,
    "product_name": "Chocolate Fudge Brownie",
    "sales_volume": 52,
    "transaction_id": "TX0054"
  },
  {
    "sale_date": "2025-01-05",
    "temperature": null,
    "product_name": "Half Baked",
    "sales_volume": 55,
    "transaction_id": "TX0055"
  },
  {
    "sale_date": "2025-02-15",
    "temperature": 79,
    "product_name": "New York Super Fudge Chunk",
    "sales_volume": 58,
    "transaction_id": "TX0056"
  },
  {
    "sale_date": "2025-03-25",
    "temperature": 81,
    "product_name": "Cherry Garcia",
    "sales_volume": 61,
    "transaction_id": "TX0057"
  },
  {
    "sale_date": "2025-04-05",
    "temperature": 83,
    "product_name": "Chunky Monkey",
    "sales_volume": 64,
    "transaction_id": "TX0058"
  },
  {
    "sale_date": "2025-05-15",
    "temperature": 85,
    "product_name": "Phish Food",
    "sales_volume": 67,
    "transaction_id": "TX0059"
  },
  {
    "sale_date": "2025-06-25",
    "temperature": 87,
    "product_name": "Americone Dream",
    "sales_volume": 70,
    "transaction_id": "TX0060"
  },
  {
    "sale_date": "2024-12-25",
    "temperature": 89,
    "product_name": "Chunky Monkey",
    "sales_volume": 110,
    "transaction_id": "TX0030"
  }
]
ice_cream_sales_data = pd.DataFrame(ice_cream_sales_data_data)


# ## Question 1
# 
# Identify and remove any duplicate sales transactions from the dataset to ensure accurate analysis of seasonal patterns.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: ice_cream_sales_data
# Please print your final result or dataframe
ice_cream_sales_data = ice_cream_sales_data.sort_values(by='transaction_id', ascending=True)

clean_data =  ice_cream_sales_data.drop_duplicates('transaction_id')

clean_data


# ## Question 2
# 
# Create a pivot table to summarize the total sales volume of ice cream products by month and temperature range.
# Use the following temperature bins where each bin excludes the upper bound but includes the lower bound:
# - Less than 60 degrees
# - 60 to less than 70 degrees
# - 70 to less than 80 degrees
# - 80 to less than 90 degrees
# - 90 to less than 100 degrees
# - 100 degrees or more

# In[ ]:


bins = [-np.inf, 60, 70, 80, 90, 100, np.inf]
ice_cream_sales_data['temperature_range'] = pd.cut(ice_cream_sales_data['temperature'], bins=bins, right=False)
ice_cream_sales_data['month'] = ice_cream_sales_data['sale_date'].dt.to_period('M')
pivot_table = pd.pivot_table(ice_cream_sales_data, index='month', columns='temperature_range', values='sales_volume', aggfunc='sum')

pivot_table


# ## Question 3
# 
# Can you detect any outliers in the monthly sales volume using the Inter Quartile Range (IQR) method? A month is considered an outlier if falls below Q1 minus 1.5 times the IQR or above Q3 plus 1.5 times the IQR.

# In[ ]:


bins = [-np.inf, 60, 70, 80, 90, 100, np.inf]
ice_cream_sales_data['temperature_range'] = pd.cut(ice_cream_sales_data['temperature'], bins=bins, right=False)
ice_cream_sales_data['month'] = ice_cream_sales_data['sale_date'].dt.to_period('M')
pivot_table = pd.pivot_table(ice_cream_sales_data, index='month', columns='temperature_range', values='sales_volume', aggfunc='sum')

total_sales = ice_cream_sales_data.groupby('month')['sales_volume'].sum()

Q1 = total_sales.quantile(0.25)

Q3 = total_sales.quantile(0.75)

IQR = Q3-Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outliers = total_sales[(total_sales < lower_bound) | (total_sales > upper_bound)]
outliers


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
