#!/usr/bin/env python
# coding: utf-8

# # Day 8: Payment Method Impact on Athleisure Online Sales

# You are a Product Analyst for the Lululemon Online Store team investigating how alternative payment methods might influence sales performance. The team wants to understand the potential impact of introducing a new installment payment option. Your analysis will predict sales lift and customer conversion for the proposed payment method.

# In[ ]:


import pandas as pd
import numpy as np

fct_transactions_data = [
  {
    "customer_id": 201,
    "order_value": 250,
    "payment_method": "credit_card",
    "transaction_id": 1,
    "transaction_date": "2025-03-15"
  },
  {
    "customer_id": 202,
    "order_value": 95,
    "payment_method": "debit_card",
    "transaction_id": 2,
    "transaction_date": "2025-03-20"
  },
  {
    "customer_id": 203,
    "order_value": 75,
    "payment_method": "paypal",
    "transaction_id": 3,
    "transaction_date": "2025-03-25"
  },
  {
    "customer_id": 204,
    "order_value": 310,
    "payment_method": "credit_card",
    "transaction_id": 4,
    "transaction_date": "2024-11-10"
  },
  {
    "customer_id": 205,
    "order_value": 65,
    "payment_method": "paypal",
    "transaction_id": 5,
    "transaction_date": "2024-12-05"
  },
  {
    "customer_id": 206,
    "order_value": 265,
    "payment_method": "credit_card",
    "transaction_id": 6,
    "transaction_date": "2024-07-15"
  },
  {
    "customer_id": 207,
    "order_value": 290,
    "payment_method": "credit_card",
    "transaction_id": 7,
    "transaction_date": "2024-08-10"
  },
  {
    "customer_id": 208,
    "order_value": 275,
    "payment_method": "credit_card",
    "transaction_id": 8,
    "transaction_date": "2024-09-05"
  },
  {
    "customer_id": 209,
    "order_value": 280,
    "payment_method": "credit_card",
    "transaction_id": 9,
    "transaction_date": "2024-10-20"
  },
  {
    "customer_id": 210,
    "order_value": 90,
    "payment_method": "debit_card",
    "transaction_id": 10,
    "transaction_date": "2024-10-25"
  },
  {
    "customer_id": 101,
    "order_value": 275,
    "payment_method": "credit_card",
    "transaction_id": 11,
    "transaction_date": "2025-04-02"
  },
  {
    "customer_id": 102,
    "order_value": 285,
    "payment_method": "credit_card",
    "transaction_id": 12,
    "transaction_date": "2025-04-05"
  },
  {
    "customer_id": 103,
    "order_value": 280,
    "payment_method": "credit_card",
    "transaction_id": 13,
    "transaction_date": "2025-04-10"
  },
  {
    "customer_id": 104,
    "order_value": 290,
    "payment_method": "credit_card",
    "transaction_id": 14,
    "transaction_date": "2025-04-15"
  },
  {
    "customer_id": 105,
    "order_value": 270,
    "payment_method": "credit_card",
    "transaction_id": 15,
    "transaction_date": "2025-04-20"
  },
  {
    "customer_id": 106,
    "order_value": 295,
    "payment_method": "credit_card",
    "transaction_id": 16,
    "transaction_date": "2025-04-25"
  },
  {
    "customer_id": 107,
    "order_value": 280,
    "payment_method": "credit_card",
    "transaction_id": 17,
    "transaction_date": "2025-05-01"
  },
  {
    "customer_id": 108,
    "order_value": 275,
    "payment_method": "credit_card",
    "transaction_id": 18,
    "transaction_date": "2025-05-05"
  },
  {
    "customer_id": 109,
    "order_value": 285,
    "payment_method": "credit_card",
    "transaction_id": 19,
    "transaction_date": "2025-05-10"
  },
  {
    "customer_id": 110,
    "order_value": 290,
    "payment_method": "credit_card",
    "transaction_id": 20,
    "transaction_date": "2025-05-15"
  },
  {
    "customer_id": 111,
    "order_value": 270,
    "payment_method": "credit_card",
    "transaction_id": 21,
    "transaction_date": "2025-05-20"
  },
  {
    "customer_id": 112,
    "order_value": 280,
    "payment_method": "credit_card",
    "transaction_id": 22,
    "transaction_date": "2025-05-25"
  },
  {
    "customer_id": 113,
    "order_value": 295,
    "payment_method": "credit_card",
    "transaction_id": 23,
    "transaction_date": "2025-05-30"
  },
  {
    "customer_id": 114,
    "order_value": 285,
    "payment_method": "credit_card",
    "transaction_id": 24,
    "transaction_date": "2025-06-01"
  },
  {
    "customer_id": 115,
    "order_value": 280,
    "payment_method": "credit_card",
    "transaction_id": 25,
    "transaction_date": "2025-06-05"
  },
  {
    "customer_id": 116,
    "order_value": 275,
    "payment_method": "credit_card",
    "transaction_id": 26,
    "transaction_date": "2025-06-10"
  },
  {
    "customer_id": 117,
    "order_value": 285,
    "payment_method": "credit_card",
    "transaction_id": 27,
    "transaction_date": "2025-06-15"
  },
  {
    "customer_id": 118,
    "order_value": 290,
    "payment_method": "credit_card",
    "transaction_id": 28,
    "transaction_date": "2025-06-20"
  },
  {
    "customer_id": 119,
    "order_value": 270,
    "payment_method": "credit_card",
    "transaction_id": 29,
    "transaction_date": "2025-06-25"
  },
  {
    "customer_id": 120,
    "order_value": 280,
    "payment_method": "credit_card",
    "transaction_id": 30,
    "transaction_date": "2025-06-30"
  },
  {
    "customer_id": 121,
    "order_value": 275,
    "payment_method": "credit_card",
    "transaction_id": 31,
    "transaction_date": "2025-04-08"
  },
  {
    "customer_id": 122,
    "order_value": 285,
    "payment_method": "credit_card",
    "transaction_id": 32,
    "transaction_date": "2025-04-18"
  },
  {
    "customer_id": 123,
    "order_value": 290,
    "payment_method": "credit_card",
    "transaction_id": 33,
    "transaction_date": "2025-05-08"
  },
  {
    "customer_id": 124,
    "order_value": 280,
    "payment_method": "credit_card",
    "transaction_id": 34,
    "transaction_date": "2025-05-18"
  },
  {
    "customer_id": 125,
    "order_value": 275,
    "payment_method": "credit_card",
    "transaction_id": 35,
    "transaction_date": "2025-06-08"
  },
  {
    "customer_id": 126,
    "order_value": 92,
    "payment_method": "debit_card",
    "transaction_id": 36,
    "transaction_date": "2025-04-07"
  },
  {
    "customer_id": 127,
    "order_value": 88,
    "payment_method": "debit_card",
    "transaction_id": 37,
    "transaction_date": "2025-04-12"
  },
  {
    "customer_id": 128,
    "order_value": 90,
    "payment_method": "debit_card",
    "transaction_id": 38,
    "transaction_date": "2025-04-17"
  },
  {
    "customer_id": 129,
    "order_value": 85,
    "payment_method": "debit_card",
    "transaction_id": 39,
    "transaction_date": "2025-04-22"
  },
  {
    "customer_id": 130,
    "order_value": 95,
    "payment_method": "debit_card",
    "transaction_id": 40,
    "transaction_date": "2025-05-12"
  },
  {
    "customer_id": 131,
    "order_value": 90,
    "payment_method": "debit_card",
    "transaction_id": 41,
    "transaction_date": "2025-05-22"
  },
  {
    "customer_id": 132,
    "order_value": 92,
    "payment_method": "debit_card",
    "transaction_id": 42,
    "transaction_date": "2025-06-15"
  },
  {
    "customer_id": 133,
    "order_value": 88,
    "payment_method": "debit_card",
    "transaction_id": 43,
    "transaction_date": "2025-06-25"
  },
  {
    "customer_id": 134,
    "order_value": 70,
    "payment_method": "paypal",
    "transaction_id": 44,
    "transaction_date": "2025-04-07"
  },
  {
    "customer_id": 135,
    "order_value": 72,
    "payment_method": "paypal",
    "transaction_id": 45,
    "transaction_date": "2025-04-17"
  },
  {
    "customer_id": 136,
    "order_value": 68,
    "payment_method": "paypal",
    "transaction_id": 46,
    "transaction_date": "2025-04-27"
  },
  {
    "customer_id": 137,
    "order_value": 70,
    "payment_method": "paypal",
    "transaction_id": 47,
    "transaction_date": "2025-05-07"
  },
  {
    "customer_id": 138,
    "order_value": 69,
    "payment_method": "paypal",
    "transaction_id": 48,
    "transaction_date": "2025-05-27"
  },
  {
    "customer_id": 139,
    "order_value": 71,
    "payment_method": "paypal",
    "transaction_id": 49,
    "transaction_date": "2025-06-03"
  },
  {
    "customer_id": 140,
    "order_value": 70,
    "payment_method": "paypal",
    "transaction_id": 50,
    "transaction_date": "2025-06-12"
  }
]
fct_transactions = pd.DataFrame(fct_transactions_data)


# ## Question 1
# 
# Between April 1st and June 30th, 2025, what is the count of transactions for each payment method? This analysis will establish the baseline distribution of how customers currently pay.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions
# Please print your final result or dataframe
fct_transactions['transaction_date'] = pd.to_datetime(fct_transactions['transaction_date']) 

start_date = '2025-04-01'
end_date = '2025-06-30'

filtered_transactions = fct_transactions[(fct_transactions['transaction_date'] >= start_date) & (fct_transactions['transaction_date'] <= end_date)]

trans_counts = filtered_transactions['payment_method'].value_counts()

trans_counts


# ## Question 2
# 
# Between April 1st and June 30th, 2025, what is the average order value for each payment method? This metric will help us assess which payment methods are tied to higher spending levels.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions
# Please print your final result or dataframe
fct_transactions['transaction_date'] = pd.to_datetime(fct_transactions['transaction_date']) 

start_date = '2025-04-01'
end_date = '2025-06-30'

filtered_transactions = fct_transactions[(fct_transactions['transaction_date'] >= start_date) & (fct_transactions['transaction_date'] <= end_date)]

# trans_counts = filtered_transactions['payment_method'].value_counts()

avg_order_values = filtered_transactions.groupby('payment_method')['order_value'].mean()

avg_order_values


# ## Question 3
# 
# Between April 1st and June 30th, 2025, what would be the predicted sales lift if a 'pay over time' option were introduced? Assume that 20% of credit card transactions during this period would switch to using the 'pay over time' option. And that for these switched transactions, the order value is expected to increase by 15% based on the average order value of all credit card transactions in that same time period.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions
# Please print your final result or dataframe
fct_transactions['transaction_date'] = pd.to_datetime(fct_transactions['transaction_date']) 

start_date = '2025-04-01'
end_date = '2025-06-30'

filtered_transactions = fct_transactions[(fct_transactions['transaction_date'] >= start_date) & (fct_transactions['transaction_date'] <= end_date) & 
  (fct_transactions['payment_method'] == 'credit_card')]

filtered_transactions_count = filtered_transactions['payment_method'].count()

filtered_transactions_switch = filtered_transactions_count * 0.20

cc_trans_total = filtered_transactions['order_value'].sum()
cc_trans_count = filtered_transactions['order_value'].count()

cc_trans = cc_trans_total / cc_trans_count
order_increase = cc_trans * 0.15

sales_lift = filtered_transactions_switch * order_increase

sales_lift


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
