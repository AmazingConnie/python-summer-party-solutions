#!/usr/bin/env python
# coding: utf-8

# # Day 12: E-commerce Returns Customer Segmentation Model

# You are a Data Analyst on the Walmart.com Insights team investigating customer return patterns. The team aims to develop a predictive approach to understanding customer return behaviors across different time periods. Your goal is to leverage transaction data to create a comprehensive view of customer return likelihood.

# In[ ]:


import pandas as pd
import numpy as np

customer_returns_data = [
  {
    "order_id": "ORD0001",
    "order_date": "2024-07-05",
    "customer_id": "CUST001",
    "return_flag": true,
    "order_amount": 120.5
  },
  {
    "order_id": "ORD0002",
    "order_date": "2024-07-10",
    "customer_id": "CUST002",
    "return_flag": false,
    "order_amount": 75
  },
  {
    "order_id": "ORD0003",
    "order_date": "2024-08-15",
    "customer_id": "CUST001",
    "return_flag": true,
    "order_amount": 90
  },
  {
    "order_id": "ORD0004",
    "order_date": "2024/09/01",
    "customer_id": "CUST003",
    "return_flag": false,
    "order_amount": 45
  },
  {
    "order_id": "ORD0005",
    "order_date": "2024-10-20",
    "customer_id": "CUST004",
    "return_flag": true,
    "order_amount": 200
  },
  {
    "order_id": "ORD0006",
    "order_date": "2024-11-11",
    "customer_id": "CUST002",
    "return_flag": true,
    "order_amount": null
  },
  {
    "order_id": "ORD0007",
    "order_date": "2024-11-15",
    "customer_id": "CUST005",
    "return_flag": false,
    "order_amount": 60
  },
  {
    "order_id": "ORD0008",
    "order_date": "2024-12-05",
    "customer_id": "CUST006",
    "return_flag": true,
    "order_amount": 150
  },
  {
    "order_id": "ORD0009",
    "order_date": "2024-12-25",
    "customer_id": "CUST007",
    "return_flag": false,
    "order_amount": 85
  },
  {
    "order_id": "ORD0010",
    "order_date": "2025-01-10",
    "customer_id": "CUST001",
    "return_flag": true,
    "order_amount": 130
  },
  {
    "order_id": "ORD0011",
    "order_date": "2025-01-15",
    "customer_id": "CUST008",
    "return_flag": false,
    "order_amount": 50
  },
  {
    "order_id": "ORD0012",
    "order_date": "2025-02-10",
    "customer_id": "CUST009",
    "return_flag": true,
    "order_amount": 110
  },
  {
    "order_id": "ORD0013",
    "order_date": "2025-02-14",
    "customer_id": "CUST010",
    "return_flag": false,
    "order_amount": 100
  },
  {
    "order_id": "ORD0014",
    "order_date": "2025-03-03",
    "customer_id": "CUST005",
    "return_flag": true,
    "order_amount": 77.5
  },
  {
    "order_id": "ORD0015",
    "order_date": null,
    "customer_id": "CUST002",
    "return_flag": false,
    "order_amount": 65
  },
  {
    "order_id": "ORD0016",
    "order_date": "2025-03-20",
    "customer_id": "CUST003",
    "return_flag": true,
    "order_amount": 180
  },
  {
    "order_id": "ORD0017",
    "order_date": "2025-04-01",
    "customer_id": "CUST004",
    "return_flag": false,
    "order_amount": 95
  },
  {
    "order_id": "ORD0018",
    "order_date": "2025-04-15",
    "customer_id": "CUST006",
    "return_flag": true,
    "order_amount": 210
  },
  {
    "order_id": "ORD0019",
    "order_date": "2025-05-05",
    "customer_id": "CUST007",
    "return_flag": true,
    "order_amount": 55
  },
  {
    "order_id": "ORD0020",
    "order_date": "2025-05-20",
    "customer_id": "CUST008",
    "return_flag": false,
    "order_amount": 145
  },
  {
    "order_id": "ORD0021",
    "order_date": "2025-06-01",
    "customer_id": "CUST009",
    "return_flag": true,
    "order_amount": 85
  },
  {
    "order_id": "ORD0022",
    "order_date": "2025-06-10",
    "customer_id": "CUST010",
    "return_flag": false,
    "order_amount": 190
  },
  {
    "order_id": "ORD0023",
    "order_date": "2024-07-20",
    "customer_id": "CUST001",
    "return_flag": true,
    "order_amount": 130.5
  },
  {
    "order_id": "ORD0024",
    "order_date": "2024-08-05",
    "customer_id": "CUST002",
    "return_flag": false,
    "order_amount": 60
  },
  {
    "order_id": "ORD0025",
    "order_date": "2024-09-10",
    "customer_id": "CUST003",
    "return_flag": true,
    "order_amount": 300
  },
  {
    "order_id": "ORD0026",
    "order_date": "2024-10-30",
    "customer_id": "CUST004",
    "return_flag": false,
    "order_amount": null
  },
  {
    "order_id": "ORD0027",
    "order_date": "2024-11-20",
    "customer_id": "CUST005",
    "return_flag": true,
    "order_amount": 40
  },
  {
    "order_id": "ORD0028",
    "order_date": "2024-12-15",
    "customer_id": "CUST006",
    "return_flag": false,
    "order_amount": 65
  },
  {
    "order_id": "ORD0029",
    "order_date": "2025-01-05",
    "customer_id": "CUST007",
    "return_flag": true,
    "order_amount": 115
  },
  {
    "order_id": "ORD0030",
    "order_date": "2025-01-25",
    "customer_id": "CUST008",
    "return_flag": false,
    "order_amount": 68
  },
  {
    "order_id": "ORD0031",
    "order_date": "2025-02-20",
    "customer_id": "CUST009",
    "return_flag": true,
    "order_amount": 99.9
  },
  {
    "order_id": "ORD0032",
    "order_date": "2025-03-10",
    "customer_id": "CUST010",
    "return_flag": false,
    "order_amount": 47
  },
  {
    "order_id": "ORD0033",
    "order_date": "2025-03-15",
    "customer_id": "CUST001",
    "return_flag": true,
    "order_amount": 130
  },
  {
    "order_id": "ORD0034",
    "order_date": "2025-04-05",
    "customer_id": "CUST002",
    "return_flag": false,
    "order_amount": 80
  },
  {
    "order_id": "ORD0035",
    "order_date": "2025-04-20",
    "customer_id": "CUST003",
    "return_flag": true,
    "order_amount": 220
  },
  {
    "order_id": "ORD0036",
    "order_date": "2025-05-15",
    "customer_id": "CUST004",
    "return_flag": false,
    "order_amount": 90
  },
  {
    "order_id": "ORD0037",
    "order_date": "2025-06-05",
    "customer_id": "CUST005",
    "return_flag": true,
    "order_amount": 55.5
  },
  {
    "order_id": "ORD0038",
    "order_date": "2024-07-25",
    "customer_id": "CUST006",
    "return_flag": false,
    "order_amount": 105
  },
  {
    "order_id": "ORD0039",
    "order_date": "2024-08-15",
    "customer_id": "CUST007",
    "return_flag": true,
    "order_amount": null
  },
  {
    "order_id": "ORD0040",
    "order_date": "2024-09-05",
    "customer_id": "CUST008",
    "return_flag": false,
    "order_amount": 78
  },
  {
    "order_id": "ORD0041",
    "order_date": "2024-10-10",
    "customer_id": "CUST009",
    "return_flag": true,
    "order_amount": 165
  },
  {
    "order_id": "ORD0042",
    "order_date": "2024-11-30",
    "customer_id": "CUST010",
    "return_flag": false,
    "order_amount": 88
  },
  {
    "order_id": "ORD0043",
    "order_date": "2025-06-25",
    "customer_id": "CUST001",
    "return_flag": true,
    "order_amount": 250
  },
  {
    "order_id": "ORD0044",
    "order_date": "2025-06-28",
    "customer_id": "CUST002",
    "return_flag": false,
    "order_amount": 47.7
  },
  {
    "order_id": "ORD0045",
    "order_date": "2025-06-30",
    "customer_id": "CUST003",
    "return_flag": true,
    "order_amount": 99
  },
  {
    "order_id": "ORD0046",
    "order_date": "2024-07-07",
    "customer_id": "CUST004",
    "return_flag": false,
    "order_amount": 115
  },
  {
    "order_id": "ORD0047",
    "order_date": "2024-08-09",
    "customer_id": "CUST005",
    "return_flag": true,
    "order_amount": 152
  },
  {
    "order_id": "ORD0048",
    "order_date": "2024-09-11",
    "customer_id": "CUST006",
    "return_flag": false,
    "order_amount": 67
  },
  {
    "order_id": "ORD0049",
    "order_date": "2024-10-12",
    "customer_id": "CUST007",
    "return_flag": true,
    "order_amount": 190
  },
  {
    "order_id": "ORD0050",
    "order_date": "2024-11-13",
    "customer_id": "CUST008",
    "return_flag": false,
    "order_amount": 82
  },
  {
    "order_id": "ORD0051",
    "order_date": "2024-12-01",
    "customer_id": "CUST009",
    "return_flag": true,
    "order_amount": 140
  },
  {
    "order_id": "ORD0052",
    "order_date": "2024-12-15",
    "customer_id": "CUST010",
    "return_flag": false,
    "order_amount": 77
  },
  {
    "order_id": "ORD0052",
    "order_date": "2024-12-15",
    "customer_id": "CUST010",
    "return_flag": false,
    "order_amount": 77
  },
  {
    "order_id": "ORD0053",
    "order_date": "2025-01-20",
    "customer_id": "CUST001",
    "return_flag": true,
    "order_amount": 134
  },
  {
    "order_id": "ORD0054",
    "order_date": "2025-02-25",
    "customer_id": "CUST002",
    "return_flag": false,
    "order_amount": 95
  },
  {
    "order_id": "ORD0055",
    "order_date": "2025-03-25",
    "customer_id": "CUST003",
    "return_flag": true,
    "order_amount": 202
  },
  {
    "order_id": "ORD0056",
    "order_date": "2025-04-25",
    "customer_id": "CUST004",
    "return_flag": false,
    "order_amount": null
  },
  {
    "order_id": "ORD0057",
    "order_date": "2025-05-30",
    "customer_id": "CUST005",
    "return_flag": true,
    "order_amount": 65
  },
  {
    "order_id": "ORD0058",
    "order_date": "2025-06-12",
    "customer_id": "CUST006",
    "return_flag": false,
    "order_amount": 88.8
  },
  {
    "order_id": "ORD0059",
    "order_date": "2025-06-18",
    "customer_id": "CUST007",
    "return_flag": true,
    "order_amount": 320
  }
]
customer_returns = pd.DataFrame(customer_returns_data)


# ## Question 1
# 
# Identify and list all unique customer IDs who have made returns between July 1st 2024 and June 30th 2025. This will help us understand the base set of customers involved in returns during the specified period.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: customer_returns
# Please print your final result or dataframe

customer_returns['order_date'] = pd.to_datetime(customer_returns['order_date'], format='ISO8601')

start_date = customer_returns['order_date'] >= '2024-07-01'
end_date = customer_returns['order_date'] <= '2025-06-30'

return_period = customer_returns[(start_date) & (end_date)]

unique_ids = return_period['customer_id'].unique()

unique_ids


# ## Question 2
# 
# Convert the 'order_date' column to a datetime format and create a MultiIndex with 'customer_id' and 'order_date'. Then, calculate the total number of returns per customer for each month. This will provide insights into monthly return patterns for each customer.

# In[ ]:


customer_returns['order_date'] = pd.to_datetime(customer_returns['order_date'], format='ISO8601') 

customer_returns['order_date'] = customer_returns['order_date'].dt.to_period('M')

customer_returns = customer_returns[customer_returns['return_flag'] == True]
customer_total_multi = customer_returns.set_index(['customer_id', 'order_date'])

total_returns = customer_total_multi.groupby(['customer_id', 'order_date'])['return_flag'].sum()

total_returns


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
