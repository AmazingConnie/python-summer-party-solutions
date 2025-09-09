#!/usr/bin/env python
# coding: utf-8

# # Day 14: Loyalty Program's Impact on Transaction Patterns

# You are a Business Analyst on the Starbucks Rewards team investigating customer transaction behavior. Your team wants to understand how loyalty program membership influences purchasing patterns. The goal is to compare transaction metrics between loyalty members and non-members.

# In[ ]:


import pandas as pd
import numpy as np

dim_customers_data = [
  {
    "customer_id": 1,
    "is_loyalty_member": 1
  },
  {
    "customer_id": 2,
    "is_loyalty_member": 0
  },
  {
    "customer_id": 3,
    "is_loyalty_member": 1
  },
  {
    "customer_id": 4,
    "is_loyalty_member": 0
  },
  {
    "customer_id": 5,
    "is_loyalty_member": 1
  },
  {
    "customer_id": 6,
    "is_loyalty_member": 1
  },
  {
    "customer_id": 7,
    "is_loyalty_member": 0
  },
  {
    "customer_id": 8,
    "is_loyalty_member": 1
  },
  {
    "customer_id": 9,
    "is_loyalty_member": 0
  },
  {
    "customer_id": 10,
    "is_loyalty_member": 0
  },
  {
    "customer_id": 11,
    "is_loyalty_member": 1
  },
  {
    "customer_id": 12,
    "is_loyalty_member": 0
  }
]
dim_customers = pd.DataFrame(dim_customers_data)

fct_transactions_data = [
  {
    "customer_id": 1,
    "transaction_id": 101,
    "transaction_date": "2024-07-05",
    "transaction_value": 5.5
  },
  {
    "customer_id": 1,
    "transaction_id": 102,
    "transaction_date": "2024-07-15",
    "transaction_value": 7.25
  },
  {
    "customer_id": 2,
    "transaction_id": 103,
    "transaction_date": "2024-07-10",
    "transaction_value": 4
  },
  {
    "customer_id": 3,
    "transaction_id": 104,
    "transaction_date": "2024-07-20",
    "transaction_value": 8.75
  },
  {
    "customer_id": 4,
    "transaction_id": 105,
    "transaction_date": "2024-07-03",
    "transaction_value": 6.5
  },
  {
    "customer_id": 5,
    "transaction_id": 106,
    "transaction_date": "2024-07-22",
    "transaction_value": 9
  },
  {
    "customer_id": 6,
    "transaction_id": 107,
    "transaction_date": "2024-07-11",
    "transaction_value": 10.5
  },
  {
    "customer_id": 7,
    "transaction_id": 108,
    "transaction_date": "2024-07-18",
    "transaction_value": 4.25
  },
  {
    "customer_id": 8,
    "transaction_id": 109,
    "transaction_date": "2024-07-25",
    "transaction_value": 12
  },
  {
    "customer_id": 9,
    "transaction_id": 110,
    "transaction_date": "2024-07-07",
    "transaction_value": 3.75
  },
  {
    "customer_id": 10,
    "transaction_id": 111,
    "transaction_date": "2024-07-12",
    "transaction_value": 5
  },
  {
    "customer_id": 11,
    "transaction_id": 112,
    "transaction_date": "2024-07-27",
    "transaction_value": 11.25
  },
  {
    "customer_id": 12,
    "transaction_id": 113,
    "transaction_date": "2024-07-08",
    "transaction_value": 6
  },
  {
    "customer_id": 3,
    "transaction_id": 114,
    "transaction_date": "2024-07-30",
    "transaction_value": 7.5
  },
  {
    "customer_id": 5,
    "transaction_id": 115,
    "transaction_date": "2024-07-29",
    "transaction_value": 10
  },
  {
    "customer_id": 1,
    "transaction_id": 116,
    "transaction_date": "2024-07-31",
    "transaction_value": 6.25
  }
]
fct_transactions = pd.DataFrame(fct_transactions_data)


# ## Question 1
# 
# For the month of July 2024, how many transactions did loyalty program members and non-members make? Compare the transaction counts between these two groups.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_customers
# Please print your final result or dataframe
full_table = pd.merge(fct_transactions, dim_customers, on='customer_id')

full_table['transaction_date'] = pd.to_datetime(full_table['transaction_date'])

full_table_july = full_table[(full_table['transaction_date'] >= '2024-07-01') & (full_table['transaction_date'] <= '2024-07-31')]
full_table_loyalty = full_table_july[full_table_july['is_loyalty_member'] == 1]

full_table_loyalty_count = full_table_loyalty['transaction_id'].count()

full_table_loyalty_count

full_table_regular = full_table_july[full_table_july['is_loyalty_member'] == 0]

full_table_regular_count = full_table_regular['transaction_id'].count()

full_table_loyalty_count, full_table_regular_count


# ## Question 2
# 
# What is the average transaction value for loyalty program members and non-members during July 2024? Use this to identify which group has a higher average transaction value.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_customers
# Please print your final result or dataframe
full_table = pd.merge(fct_transactions, dim_customers, on='customer_id')

full_table['transaction_date'] = pd.to_datetime(full_table['transaction_date'])

full_table_july = full_table[(full_table['transaction_date'] >= '2024-07-01') & (full_table['transaction_date'] <= '2024-07-31')]
full_table_loyalty = full_table_july[full_table_july['is_loyalty_member'] == 1]

full_table_loyalty_avg = full_table_loyalty['transaction_value'].mean()


full_table_regular = full_table_july[full_table_july['is_loyalty_member'] == 0]

full_table_regular_avg = full_table_regular['transaction_value'].mean()

full_table_loyalty_avg, full_table_regular_avg


# ## Question 3
# 
# Determine the percentage difference in average transaction value between loyalty program members and non-members for July 2024.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_customers
# Please print your final result or dataframe
full_table = pd.merge(fct_transactions, dim_customers, on='customer_id')

full_table['transaction_date'] = pd.to_datetime(full_table['transaction_date'])

full_table_july = full_table[(full_table['transaction_date'] >= '2024-07-01') & (full_table['transaction_date'] <= '2024-07-31')]
full_table_loyalty = full_table_july[full_table_july['is_loyalty_member'] == 1]

full_table_loyalty_avg = full_table_loyalty['transaction_value'].mean()


full_table_regular = full_table_july[full_table_july['is_loyalty_member'] == 0]

full_table_regular_avg = full_table_regular['transaction_value'].mean()

total_members = full_table_july['customer_id'].count()

percent_diff = ((full_table_loyalty_avg - full_table_regular_avg) / full_table_regular_avg) * 100

percent_diff


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
