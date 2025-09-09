#!/usr/bin/env python
# coding: utf-8

# # Day 7: Celebrity Product Drops Sales Performance Analysis

# You are a Product Analyst working on Nike's marketing performance team. Your team wants to evaluate the effectiveness of celebrity product collaborations by analyzing sales data. You will investigate the performance of celebrity product drops to inform future marketing strategies.

# In[ ]:


import pandas as pd
import numpy as np

fct_sales_data = [
  {
    "sale_id": 1,
    "sale_date": "2025-01-10",
    "product_id": 901,
    "sale_amount": null,
    "celebrity_id": 101
  },
  {
    "sale_id": 2,
    "sale_date": "2025-01-15",
    "product_id": 901,
    "sale_amount": 1500,
    "celebrity_id": 101
  },
  {
    "sale_id": 3,
    "sale_date": "2025-02-03",
    "product_id": 902,
    "sale_amount": 2000.5,
    "celebrity_id": 102
  },
  {
    "sale_id": 4,
    "sale_date": "2025-03-12",
    "product_id": 903,
    "sale_amount": 2500.75,
    "celebrity_id": 103
  },
  {
    "sale_id": 5,
    "sale_date": "2025-03-20",
    "product_id": 904,
    "sale_amount": null,
    "celebrity_id": 104
  },
  {
    "sale_id": 6,
    "sale_date": "2025-02-28",
    "product_id": 901,
    "sale_amount": 1000,
    "celebrity_id": 101
  },
  {
    "sale_id": 7,
    "sale_date": "2025-03-25",
    "product_id": 902,
    "sale_amount": 300,
    "celebrity_id": 102
  },
  {
    "sale_id": 8,
    "sale_date": "2025-03-30",
    "product_id": 905,
    "sale_amount": 1800,
    "celebrity_id": 105
  },
  {
    "sale_id": 9,
    "sale_date": "2025-01-20",
    "product_id": 903,
    "sale_amount": 1200,
    "celebrity_id": 103
  },
  {
    "sale_id": 10,
    "sale_date": "2025-02-05",
    "product_id": 906,
    "sale_amount": 500,
    "celebrity_id": 106
  },
  {
    "sale_id": 11,
    "sale_date": "2025-03-01",
    "product_id": 907,
    "sale_amount": 2200,
    "celebrity_id": 107
  },
  {
    "sale_id": 12,
    "sale_date": "2025-02-15",
    "product_id": 908,
    "sale_amount": 1300,
    "celebrity_id": 101
  },
  {
    "sale_id": 13,
    "sale_date": "2025-03-15",
    "product_id": 909,
    "sale_amount": null,
    "celebrity_id": 102
  },
  {
    "sale_id": 14,
    "sale_date": "2025-01-25",
    "product_id": 910,
    "sale_amount": 900,
    "celebrity_id": 108
  },
  {
    "sale_id": 15,
    "sale_date": "2025-02-20",
    "product_id": 905,
    "sale_amount": 700,
    "celebrity_id": 105
  },
  {
    "sale_id": 16,
    "sale_date": "2025-03-28",
    "product_id": 902,
    "sale_amount": 1500,
    "celebrity_id": 102
  },
  {
    "sale_id": 17,
    "sale_date": "2024-11-15",
    "product_id": 901,
    "sale_amount": 800,
    "celebrity_id": 101
  },
  {
    "sale_id": 18,
    "sale_date": "2024-07-30",
    "product_id": 902,
    "sale_amount": 1000,
    "celebrity_id": 102
  },
  {
    "sale_id": 19,
    "sale_date": "2025-04-10",
    "product_id": 905,
    "sale_amount": 2000,
    "celebrity_id": 105
  },
  {
    "sale_id": 20,
    "sale_date": "2024-09-05",
    "product_id": 903,
    "sale_amount": 1100,
    "celebrity_id": 103
  }
]
fct_sales = pd.DataFrame(fct_sales_data)


# ## Question 1
# 
# For Q1 2025 (January 1st through March 31st, 2025), can you identify all records of celebrity collaborations from the sales data where the sale_amount is missing? This will help us flag incomplete records that could impact the analysis of Nike's product performance.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales
# Please print your final result or dataframe
fct_sales['sale_date'] = pd.to_datetime(fct_sales['sale_date'])

starting_date = '2025-01-01'
ending_date = '2025-03-31'
q1_records = fct_sales[(fct_sales['sale_date'] >= starting_date) & (fct_sales['sale_date'] <= ending_date) & (fct_sales['sale_amount'].isna())]

q1_records


# ## Question 2
# 
# For Q1 2025 (January 1st through March 31st, 2025), can you list the unique combinations of celebrity_id and product_id from the sales table? This will ensure that each collaboration is accurately accounted for in the analysis of Nike's marketing performance.

# In[ ]:


fct_sales['sale_date'] = pd.to_datetime(fct_sales['sale_date'])

starting_date = '2025-01-01'
ending_date = '2025-03-31'
q1_records = fct_sales[(fct_sales['sale_date'] >= starting_date) & (fct_sales['sale_date'] <= ending_date)]

q1_records = q1_records.dropna(subset=['celebrity_id', 'product_id'])

unique_combinations = q1_records[['celebrity_id', 'product_id']].drop_duplicates()

unique_combinations


# ## Question 3
# 
# For Q1 2025 (January 1st through March 31st, 2025), can you rank the unique celebrity collaborations based on their total sales amounts and list the top 3 collaborations in descending order? This will help recommend the most successful partnerships for Nike's future product drop strategies.

# In[ ]:


fct_sales['sale_date'] = pd.to_datetime(fct_sales['sale_date'])

starting_date = '2025-01-01'
ending_date = '2025-03-31'
q1_records = fct_sales[(fct_sales['sale_date'] >= starting_date) & (fct_sales['sale_date'] <= ending_date) & (fct_sales['sale_amount'].notna())]

collab_sales = q1_records.groupby(['celebrity_id', 'product_id'])['sale_amount'].sum()

top_3 = collab_sales.sort_values(ascending=False).head(3)

top_3


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
