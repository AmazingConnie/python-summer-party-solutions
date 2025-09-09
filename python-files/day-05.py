#!/usr/bin/env python
# coding: utf-8

# # Day 5: Switch 2 Pre-sales Demand Forecasting

# You are a Product Analyst working with the Nintendo Switch 2 pre-sales team to analyze regional pre-order patterns and customer segmentation. Your team needs to understand how different demographics influence pre-sale volumes across regions. You will leverage historical pre-sale transaction data to extract meaningful insights that can guide marketing strategies.

# In[ ]:


import pandas as pd
import numpy as np

pre_sale_data_data = [
  {
    "region": "North America",
    "customer_id": "C001",
    "pre_order_date": "2024-07-02",
    "demographic_group": "Gamer",
    "pre_order_quantity": 1
  },
  {
    "region": "Europe",
    "customer_id": "C002",
    "pre_order_date": "2024-07-03",
    "demographic_group": "Casual",
    "pre_order_quantity": 2
  },
  {
    "region": "Asia",
    "customer_id": "C003",
    "pre_order_date": "2024-07-04",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 1
  },
  {
    "region": "Latin America",
    "customer_id": "C004",
    "pre_order_date": "2024-07-05",
    "demographic_group": "Family",
    "pre_order_quantity": 3
  },
  {
    "region": "Oceania",
    "customer_id": "C005",
    "pre_order_date": "2024-07-06",
    "demographic_group": "Student",
    "pre_order_quantity": 2
  },
  {
    "region": "North America",
    "customer_id": "C006",
    "pre_order_date": "2024-07-07",
    "demographic_group": "Gamer",
    "pre_order_quantity": 5
  },
  {
    "region": "Europe",
    "customer_id": "C007",
    "pre_order_date": "2024-07-08",
    "demographic_group": null,
    "pre_order_quantity": 2
  },
  {
    "region": null,
    "customer_id": "C008",
    "pre_order_date": "2024-07-09",
    "demographic_group": "Casual",
    "pre_order_quantity": 1
  },
  {
    "region": "Asia",
    "customer_id": "C009",
    "pre_order_date": "2024-07-10",
    "demographic_group": "Family",
    "pre_order_quantity": 4
  },
  {
    "region": "North America",
    "customer_id": "C010",
    "pre_order_date": "2024-07-11",
    "demographic_group": "Gamer",
    "pre_order_quantity": 1
  },
  {
    "region": "North America",
    "customer_id": "C010",
    "pre_order_date": "2024-07-11",
    "demographic_group": "Gamer",
    "pre_order_quantity": 1
  },
  {
    "region": "Europe",
    "customer_id": "C011",
    "pre_order_date": "2024-07-12",
    "demographic_group": "Student",
    "pre_order_quantity": 2
  },
  {
    "region": "Asia",
    "customer_id": "C012",
    "pre_order_date": "2024-07-13",
    "demographic_group": "Casual",
    "pre_order_quantity": 3
  },
  {
    "region": "Latin America",
    "customer_id": "C013",
    "pre_order_date": "2024-07-14",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 2
  },
  {
    "region": "Oceania",
    "customer_id": "C014",
    "pre_order_date": "2024-07-15",
    "demographic_group": "Gamer",
    "pre_order_quantity": 5
  },
  {
    "region": "North America",
    "customer_id": "C015",
    "pre_order_date": "2024-07-16",
    "demographic_group": "Casual",
    "pre_order_quantity": 1
  },
  {
    "region": "Europe",
    "customer_id": "C016",
    "pre_order_date": "2024-07-17",
    "demographic_group": "Family",
    "pre_order_quantity": 4
  },
  {
    "region": "Asia",
    "customer_id": "C017",
    "pre_order_date": "2024-07-18",
    "demographic_group": "Student",
    "pre_order_quantity": 3
  },
  {
    "region": "Latin America",
    "customer_id": "C018",
    "pre_order_date": "2024-07-19",
    "demographic_group": "Gamer",
    "pre_order_quantity": 1
  },
  {
    "region": "Oceania",
    "customer_id": "C019",
    "pre_order_date": "2024-07-20",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 2
  },
  {
    "region": "Oceania",
    "customer_id": "C019",
    "pre_order_date": "2024-07-20",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 2
  },
  {
    "region": "North America",
    "customer_id": "C020",
    "pre_order_date": "2024-07-21",
    "demographic_group": "Family",
    "pre_order_quantity": 3
  },
  {
    "region": "Europe",
    "customer_id": "C021",
    "pre_order_date": "2024-07-22",
    "demographic_group": "Gamer",
    "pre_order_quantity": 2
  },
  {
    "region": "Asia",
    "customer_id": "C022",
    "pre_order_date": "2024-07-23",
    "demographic_group": "Casual",
    "pre_order_quantity": 1
  },
  {
    "region": "Latin America",
    "customer_id": "C023",
    "pre_order_date": "2024-07-24",
    "demographic_group": "Student",
    "pre_order_quantity": 4
  },
  {
    "region": "Oceania",
    "customer_id": "C024",
    "pre_order_date": "2024-07-25",
    "demographic_group": "Family",
    "pre_order_quantity": 2
  },
  {
    "region": "North America",
    "customer_id": "C025",
    "pre_order_date": "2024-07-26",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 1
  },
  {
    "region": "Europe",
    "customer_id": "C026",
    "pre_order_date": "2024-07-27",
    "demographic_group": "Student",
    "pre_order_quantity": 5
  },
  {
    "region": "Asia",
    "customer_id": "C027",
    "pre_order_date": "2024-07-28",
    "demographic_group": "Gamer",
    "pre_order_quantity": 2
  },
  {
    "region": "Latin America",
    "customer_id": "C028",
    "pre_order_date": "2024-07-29",
    "demographic_group": "Casual",
    "pre_order_quantity": 3
  },
  {
    "region": "Oceania",
    "customer_id": "C029",
    "pre_order_date": "2024-07-30",
    "demographic_group": "Family",
    "pre_order_quantity": 1
  },
  {
    "region": "North America",
    "customer_id": "C030",
    "pre_order_date": "2024-08-01",
    "demographic_group": "Gamer",
    "pre_order_quantity": 1
  },
  {
    "region": "Asia",
    "customer_id": "C031",
    "pre_order_date": "2024-08-02",
    "demographic_group": null,
    "pre_order_quantity": 2
  },
  {
    "region": "Latin America",
    "customer_id": "C032",
    "pre_order_date": "2024-08-03",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 3
  },
  {
    "region": "Oceania",
    "customer_id": "C033",
    "pre_order_date": "2024-08-04",
    "demographic_group": "Student",
    "pre_order_quantity": 1
  },
  {
    "region": "North America",
    "customer_id": "C034",
    "pre_order_date": "2024-08-05",
    "demographic_group": "Family",
    "pre_order_quantity": 4
  },
  {
    "region": "Europe",
    "customer_id": "C035",
    "pre_order_date": "2024-08-06",
    "demographic_group": "Gamer",
    "pre_order_quantity": 2
  },
  {
    "region": "Asia",
    "customer_id": "C036",
    "pre_order_date": "2024-08-07",
    "demographic_group": "Casual",
    "pre_order_quantity": 5
  },
  {
    "region": "Latin America",
    "customer_id": "C037",
    "pre_order_date": "2024-08-08",
    "demographic_group": "Family",
    "pre_order_quantity": 1
  },
  {
    "region": "Oceania",
    "customer_id": "C038",
    "pre_order_date": "2024-08-09",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 2
  },
  {
    "region": "North America",
    "customer_id": "C039",
    "pre_order_date": "2024-08-10",
    "demographic_group": "Student",
    "pre_order_quantity": 10
  },
  {
    "region": "Europe",
    "customer_id": "C040",
    "pre_order_date": "2024-08-11",
    "demographic_group": "Family",
    "pre_order_quantity": 3
  },
  {
    "region": "Asia",
    "customer_id": "C041",
    "pre_order_date": "2024-08-12",
    "demographic_group": "Gamer",
    "pre_order_quantity": 1
  },
  {
    "region": "Latin America",
    "customer_id": "C042",
    "pre_order_date": "2024-08-13",
    "demographic_group": "Casual",
    "pre_order_quantity": 2
  },
  {
    "region": "Oceania",
    "customer_id": "C043",
    "pre_order_date": "2024-08-14",
    "demographic_group": "Student",
    "pre_order_quantity": 5
  },
  {
    "region": "North America",
    "customer_id": "C044",
    "pre_order_date": "2024-08-15",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 2
  },
  {
    "region": "Europe",
    "customer_id": "C045",
    "pre_order_date": "2024-08-16",
    "demographic_group": "Family",
    "pre_order_quantity": 1
  },
  {
    "region": "Asia",
    "customer_id": "C046",
    "pre_order_date": "2024-08-17",
    "demographic_group": "Gamer",
    "pre_order_quantity": 3
  },
  {
    "region": "Latin America",
    "customer_id": "C047",
    "pre_order_date": "2024-08-18",
    "demographic_group": "Casual",
    "pre_order_quantity": 2
  },
  {
    "region": "Oceania",
    "customer_id": "C048",
    "pre_order_date": "2024-08-19",
    "demographic_group": null,
    "pre_order_quantity": 4
  },
  {
    "region": "North America",
    "customer_id": "C049",
    "pre_order_date": "2024-08-20",
    "demographic_group": "Student",
    "pre_order_quantity": 1
  },
  {
    "region": "Europe",
    "customer_id": "C050",
    "pre_order_date": "2024-08-21",
    "demographic_group": "Gamer",
    "pre_order_quantity": 2
  },
  {
    "region": "Asia",
    "customer_id": "C051",
    "pre_order_date": "2024-08-22",
    "demographic_group": "Casual",
    "pre_order_quantity": 3
  },
  {
    "region": "Latin America",
    "customer_id": "C052",
    "pre_order_date": "2024-08-23",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 2
  },
  {
    "region": "Oceania",
    "customer_id": "C053",
    "pre_order_date": "2024-08-24",
    "demographic_group": "Family",
    "pre_order_quantity": 1
  },
  {
    "region": "North America",
    "customer_id": "C054",
    "pre_order_date": "2024-08-25",
    "demographic_group": "Gamer",
    "pre_order_quantity": 1
  },
  {
    "region": "Europe",
    "customer_id": "C055",
    "pre_order_date": "2024-08-26",
    "demographic_group": "Casual",
    "pre_order_quantity": 2
  },
  {
    "region": "Asia",
    "customer_id": "C056",
    "pre_order_date": "2024-08-27",
    "demographic_group": "Student",
    "pre_order_quantity": 3
  },
  {
    "region": "Latin America",
    "customer_id": "C057",
    "pre_order_date": "2024-08-28",
    "demographic_group": "Family",
    "pre_order_quantity": 4
  },
  {
    "region": "Oceania",
    "customer_id": "C058",
    "pre_order_date": "2024-08-29",
    "demographic_group": "Tech Enthusiast",
    "pre_order_quantity": 1
  }
]
pre_sale_data = pd.DataFrame(pre_sale_data_data)


# ## Question 1
# 
# What percentage of records have missing values in at least one column? Handle the missing values, so that we have a cleaned dataset to work with.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: pre_sale_data
# Please print your final result or dataframe

missing_rows = pre_sale_data.isnull().any(axis=1)

num_missing_rows = missing_rows.sum()

# num_missing_rows

total_rows = len(pre_sale_data)

percentage_missing_rows = (num_missing_rows / total_rows) * 100

pre_sale_data = pre_sale_data.dropna()

percentage_missing_rows


# ## Question 2
# 
# Using the cleaned data, calculate the total pre-sale orders per month for each region and demographic group.

# In[ ]:


pre_sale_data = pre_sale_data.dropna() 

pre_sale_data['pre_order_date'] = pre_sale_data['pre_order_date'].dt.to_period('M')

total_sales = pre_sale_data.groupby(['region', 'demographic_group', 'pre_order_date'])['pre_order_quantity'].sum()

total_sales


# ## Question 3
# 
# Predict the total pre-sales quantity for each region for September 2024. Assume that growth rate from August to September, is the same as the growth rate from July to August in each region.

# In[ ]:


pre_sale_data = pre_sale_data.dropna() 

pre_sale_data['pre_order_date'] = pre_sale_data['pre_order_date'].dt.to_period('M')

july_data = pre_sale_data[pre_sale_data['pre_order_date'] == '2024-07']

august_data = pre_sale_data[pre_sale_data['pre_order_date'] == '2024-08']

july_total = july_data.groupby('region')['pre_order_quantity'].sum()

august_total = august_data.groupby('region')['pre_order_quantity'].sum()

growth_rate = (august_total - july_total) / july_total

september_estimate = (august_total * (1 + growth_rate))

september_estimate


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
