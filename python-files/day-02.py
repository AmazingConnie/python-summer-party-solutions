#!/usr/bin/env python
# coding: utf-8

# # Day 2: Sponsored Posts Click Performance

# You are a Product Analyst on the Amazon Sponsored Advertising team investigating sponsored product ad engagement across electronics categories. Your team wants to understand CTR variations to optimize targeted advertising strategies.

# In[ ]:


import pandas as pd
import numpy as np

dim_product_data = [
  {
    "product_id": 1,
    "product_name": "Smart TV",
    "product_category": "Home Electronics"
  },
  {
    "product_id": 2,
    "product_name": "Wireless Earbuds",
    "product_category": "Electronics & Gadgets"
  },
  {
    "product_id": 3,
    "product_name": "Refrigerator",
    "product_category": "Electronics Appliances"
  },
  {
    "product_id": 4,
    "product_name": "Bestselling Novel",
    "product_category": "Books"
  },
  {
    "product_id": 5,
    "product_name": "Designer Jeans",
    "product_category": "Fashion"
  },
  {
    "product_id": 6,
    "product_name": "Blender",
    "product_category": "Kitchen"
  },
  {
    "product_id": 7,
    "product_name": "Tent",
    "product_category": "Outdoor"
  },
  {
    "product_id": 8,
    "product_name": "Smart Home Hub",
    "product_category": "Home Electronics"
  },
  {
    "product_id": 9,
    "product_name": "Phone Charger",
    "product_category": "Electronics Accessories"
  },
  {
    "product_id": 10,
    "product_name": "Skincare Set",
    "product_category": "Health & Beauty"
  },
  {
    "product_id": 11,
    "product_name": "Drone",
    "product_category": "Electronics Gadgets"
  },
  {
    "product_id": 12,
    "product_name": "Car Charger",
    "product_category": "Automotive"
  }
]
dim_product = pd.DataFrame(dim_product_data)

fct_ad_performance_data = [
  {
    "ad_id": 101,
    "clicks": 10,
    "product_id": 1,
    "impressions": 200,
    "recorded_date": "2024-10-02"
  },
  {
    "ad_id": 102,
    "clicks": 15,
    "product_id": 1,
    "impressions": 300,
    "recorded_date": "2024-10-12"
  },
  {
    "ad_id": 103,
    "clicks": 20,
    "product_id": 2,
    "impressions": 250,
    "recorded_date": "2024-10-05"
  },
  {
    "ad_id": 104,
    "clicks": 18,
    "product_id": 2,
    "impressions": 230,
    "recorded_date": "2024-10-20"
  },
  {
    "ad_id": 105,
    "clicks": 5,
    "product_id": 3,
    "impressions": 150,
    "recorded_date": "2024-10-15"
  },
  {
    "ad_id": 106,
    "clicks": 12,
    "product_id": 3,
    "impressions": 180,
    "recorded_date": "2024-10-25"
  },
  {
    "ad_id": 107,
    "clicks": 50,
    "product_id": 4,
    "impressions": 500,
    "recorded_date": "2024-10-07"
  },
  {
    "ad_id": 108,
    "clicks": 8,
    "product_id": 5,
    "impressions": 250,
    "recorded_date": "2024-10-18"
  },
  {
    "ad_id": 109,
    "clicks": 14,
    "product_id": 6,
    "impressions": 200,
    "recorded_date": "2024-10-10"
  },
  {
    "ad_id": 110,
    "clicks": 22,
    "product_id": 8,
    "impressions": 220,
    "recorded_date": "2024-10-30"
  },
  {
    "ad_id": 111,
    "clicks": 30,
    "product_id": 9,
    "impressions": 300,
    "recorded_date": "2024-10-08"
  },
  {
    "ad_id": 112,
    "clicks": 7,
    "product_id": 11,
    "impressions": 120,
    "recorded_date": "2024-10-22"
  },
  {
    "ad_id": 113,
    "clicks": 13,
    "product_id": 11,
    "impressions": 150,
    "recorded_date": "2024-10-28"
  },
  {
    "ad_id": 114,
    "clicks": 9,
    "product_id": 12,
    "impressions": 190,
    "recorded_date": "2024-10-11"
  },
  {
    "ad_id": 115,
    "clicks": 16,
    "product_id": 2,
    "impressions": 160,
    "recorded_date": "2024-11-01"
  }
]
fct_ad_performance = pd.DataFrame(fct_ad_performance_data)


# ## Question 1
# 
# What is the average click-through rate (CTR) for sponsored product ads for each product category that contains the substring 'Electronics' in its name during October 2024? This analysis will help determine which electronics-related categories are performing optimally.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_ad_performance, dim_product
# Please print your final result or dataframe
new_table = pd.merge(fct_ad_performance, dim_product, on='product_id')

new_table['recorded_date'] = pd.to_datetime(new_table['recorded_date'])

start_date = '2024-10-01'
end_date = '2024-10-31'
new_table = new_table[(new_table['recorded_date'] >= start_date) 
  & (new_table['recorded_date'] <= end_date) ]

new_table = new_table[(new_table['product_category'].str.contains('Electronics', case=False)) ]

new_table['CTR'] = (new_table['clicks'] / new_table['impressions'] ) * 100

ctr_electronics = new_table.groupby('product_category')['CTR'].mean()

ctr_electronics


# ## Question 2
# 
# Which product categories have a CTR greater than the aggregated overall average CTR for sponsored product ads during October 2024? This analysis will identify high-performing categories for further optimization. For this question, we want to calculate CTR for each ad, then get the average across ads by product category & overall.

# In[ ]:


new_table = pd.merge(fct_ad_performance, dim_product, on='product_id')

new_table['recorded_date'] = pd.to_datetime(new_table['recorded_date'])

start_date = '2024-10-01'
end_date = '2024-10-31'
new_table = new_table[(new_table['recorded_date'] >= start_date) 
  & (new_table['recorded_date'] <= end_date) ]

new_table['CTR'] = (new_table['clicks'] / new_table['impressions'] )

ctr_average = new_table['CTR'].mean()
ctr_category_average = new_table.groupby('product_category')['CTR'].mean() > ctr_average

ctr_category_average


# ## Question 3
# 
# For the product categories identified in the previous question, what is the percentage difference between their CTR and the overall average CTR for October 2024? This analysis will quantify the performance gap to recommend specific categories for targeted advertising optimization.

# In[ ]:


new_table = pd.merge(fct_ad_performance, dim_product, on='product_id')

new_table['recorded_date'] = pd.to_datetime(new_table['recorded_date'])

start_date = '2024-10-01'
end_date = '2024-10-31'
new_table = new_table[(new_table['recorded_date'] >= start_date) 
  & (new_table['recorded_date'] <= end_date) ]

new_table['CTR'] = (new_table['clicks'] / new_table['impressions'] )

ctr_average = new_table['CTR'].mean()
ctr_categories = new_table.groupby('product_category')['CTR'].mean()



ctr_category_average = ctr_categories[ctr_categories > ctr_average]


# CTR Average: 0.06804494932984635


ctr_category_average['percent_diff'] = ((ctr_category_average - ctr_average) / ctr_average) * 100

# ctr_categories

ctr_category_average['percent_diff']


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
