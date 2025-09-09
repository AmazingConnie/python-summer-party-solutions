#!/usr/bin/env python
# coding: utf-8

# # Day 11: Payment Fraud Risk Detection in Online Transactions

# You are a data analyst in Stripe's risk management team investigating transaction patterns to identify potential fraud. The team needs to develop a systematic approach to screen transactions for financial risks. Your goal is to create an initial risk assessment methodology using transaction characteristics.

# In[ ]:


import pandas as pd
import numpy as np

dim_risk_flags_data = [
  {
    "risk_level": "Low",
    "risk_flag_id": 1,
    "transaction_id": 2
  },
  {
    "risk_level": "Medium",
    "risk_flag_id": 2,
    "transaction_id": 7
  },
  {
    "risk_level": "High",
    "risk_flag_id": 3,
    "transaction_id": 11
  },
  {
    "risk_level": "High",
    "risk_flag_id": 4,
    "transaction_id": 12
  },
  {
    "risk_level": "High",
    "risk_flag_id": 5,
    "transaction_id": 13
  },
  {
    "risk_level": "Medium",
    "risk_flag_id": 6,
    "transaction_id": 14
  },
  {
    "risk_level": "High",
    "risk_flag_id": 7,
    "transaction_id": 15
  },
  {
    "risk_level": "Low",
    "risk_flag_id": 8,
    "transaction_id": 1
  },
  {
    "risk_level": "Medium",
    "risk_flag_id": 9,
    "transaction_id": 6
  },
  {
    "risk_level": "Low",
    "risk_flag_id": 10,
    "transaction_id": 3
  }
]
dim_risk_flags = pd.DataFrame(dim_risk_flags_data)

fct_transactions_data = [
  {
    "customer_email": "alice@gmail.com",
    "transaction_id": 1,
    "transaction_date": "2024-10-05",
    "transaction_amount": 120,
    "fraud_detection_score": 10
  },
  {
    "customer_email": "bob@customdomain.com",
    "transaction_id": 2,
    "transaction_date": "2024-10-15",
    "transaction_amount": 250.5,
    "fraud_detection_score": 20
  },
  {
    "customer_email": "charlie@yahoo.com",
    "transaction_id": 3,
    "transaction_date": "2024-10-20",
    "transaction_amount": 75.25,
    "fraud_detection_score": 15
  },
  {
    "customer_email": "dana@hotmail.com",
    "transaction_id": 4,
    "transaction_date": "2024-10-25",
    "transaction_amount": 100,
    "fraud_detection_score": 30
  },
  {
    "customer_email": "eve@biz.org",
    "transaction_id": 5,
    "transaction_date": "2024-10-30",
    "transaction_amount": 300,
    "fraud_detection_score": 40
  },
  {
    "customer_email": "frank@gmail.com",
    "transaction_id": 6,
    "transaction_date": "2024-11-03",
    "transaction_amount": 150.75,
    "fraud_detection_score": 25
  },
  {
    "customer_email": "grace@outlook.com",
    "transaction_id": 7,
    "transaction_date": "2024-11-10",
    "transaction_amount": null,
    "fraud_detection_score": 50
  },
  {
    "customer_email": "ivan@yahoo.com",
    "transaction_id": 8,
    "transaction_date": "2024-11-15",
    "transaction_amount": 200,
    "fraud_detection_score": 35
  },
  {
    "customer_email": "judy@hotmail.com",
    "transaction_id": 9,
    "transaction_date": "2024-11-21",
    "transaction_amount": 250,
    "fraud_detection_score": 45
  },
  {
    "customer_email": "ken@domain.net",
    "transaction_id": 10,
    "transaction_date": "2024-11-29",
    "transaction_amount": 300,
    "fraud_detection_score": 55
  },
  {
    "customer_email": "laura@riskmail.com",
    "transaction_id": 11,
    "transaction_date": "2024-12-02",
    "transaction_amount": 100,
    "fraud_detection_score": 80
  },
  {
    "customer_email": "mike@securepay.com",
    "transaction_id": 12,
    "transaction_date": "2024-12-03",
    "transaction_amount": 180,
    "fraud_detection_score": 85
  },
  {
    "customer_email": "nina@trusthub.com",
    "transaction_id": 13,
    "transaction_date": "2024-12-09",
    "transaction_amount": 220,
    "fraud_detection_score": 90
  },
  {
    "customer_email": "oscar@fintech.com",
    "transaction_id": 14,
    "transaction_date": "2024-12-16",
    "transaction_amount": 140,
    "fraud_detection_score": 70
  },
  {
    "customer_email": "paula@alertsys.com",
    "transaction_id": 15,
    "transaction_date": "2024-12-23",
    "transaction_amount": 260,
    "fraud_detection_score": 95
  }
]
fct_transactions = pd.DataFrame(fct_transactions_data)


# ## Question 1
# 
# How many transactions in October 2024 have a customer email ending with a domain other than 'gmail.com', 'yahoo.com', or 'hotmail.com'? This metric will help us identify transactions associated with less common email providers that may indicate emerging risk patterns.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_risk_flags
# Please print your final result or dataframe
fct_transactions['transaction_date'] = pd.to_datetime(fct_transactions['transaction_date'])


fct_transactions_october = fct_transactions[(fct_transactions['transaction_date'] >= '2024-10-01') & (fct_transactions['transaction_date'] <= '2024-10-31')]

fct_transactions_october['domain'] = fct_transactions_october['customer_email'].str.split('@').str[1]

fct_transactions_october

uncommon_domains = fct_transactions_october[(fct_transactions_october['domain'] != 'gmail.com') & (fct_transactions_october['domain'] != 'yahoo.com') & (fct_transactions_october['domain'] != 'hotmail.com')]

uncommon_domains_count = uncommon_domains['domain'].count()

uncommon_domains_count


# ## Question 2
# 
# For transactions occurring in November 2024, what is the average transaction amount, using 0 as a default for any missing values? This calculation will help us detect abnormal transaction amounts that could be related to fraudulent activity.

# In[ ]:


fct_transactions['transaction_amount'] = fct_transactions['transaction_amount'].fillna(0)

fct_transactions['transaction_date'] = pd.to_datetime(fct_transactions['transaction_date'])
tran_start_date = fct_transactions['transaction_date'] >= '2024-11-01'
tran_end_date = fct_transactions['transaction_date'] <= '2024-11-30'
november_transactions = fct_transactions[(tran_start_date) & (tran_end_date)]

november_transactions_avg = november_transactions['transaction_amount'].mean()

november_transactions_avg


# ## Question 3
# 
# Among transactions flagged as 'High' risk in December 2024, which day of the week recorded the highest number of such transactions? This analysis is intended to pinpoint specific days with concentrated high-risk activity and support the development of our preliminary fraud detection score.

# In[ ]:


full_table = pd.merge(fct_transactions, dim_risk_flags, on='transaction_id')

full_table['transaction_date'] = pd.to_datetime(full_table['transaction_date'])

filter_1 = full_table['transaction_date'] >= '2024-12-01'
filter_2 = full_table['transaction_date'] <= '2024-12-31'
filter_3 = full_table['risk_level'] == 'High'
december_high = full_table[(filter_1) & (filter_2) & (filter_3)]

december_days = december_high.groupby(december_high['transaction_date'].dt.day_name())['transaction_amount'].count()

december_days_max = december_days.idxmax()

december_days_max


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
