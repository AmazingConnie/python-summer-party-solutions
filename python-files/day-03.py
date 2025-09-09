#!/usr/bin/env python
# coding: utf-8

# # Day 3: Disney Parks Guest Spending Behavior

# You are a data analyst working with the Disney Parks revenue team to understand nuanced guest spending patterns across different park experiences. The team wants to develop a comprehensive view of visitor purchasing behaviors. Your goal is to uncover meaningful insights that can drive personalized marketing strategies.

# In[ ]:


import pandas as pd
import numpy as np

fct_guest_spending_data = [
  {
    "guest_id": 1,
    "visit_date": "2024-07-05",
    "amount_spent": 50,
    "park_experience_type": "Attraction"
  },
  {
    "guest_id": 2,
    "visit_date": "2024-07-06",
    "amount_spent": 30,
    "park_experience_type": "Dining"
  },
  {
    "guest_id": 3,
    "visit_date": "2024-07-10",
    "amount_spent": 20.5,
    "park_experience_type": "Retail"
  },
  {
    "guest_id": 4,
    "visit_date": "2024-07-12",
    "amount_spent": 40,
    "park_experience_type": "Entertainment"
  },
  {
    "guest_id": 1,
    "visit_date": "2024-07-15",
    "amount_spent": 35,
    "park_experience_type": "Dining"
  },
  {
    "guest_id": 5,
    "visit_date": "2024-07-20",
    "amount_spent": 60,
    "park_experience_type": "Attraction"
  },
  {
    "guest_id": 6,
    "visit_date": "2024-07-25",
    "amount_spent": 25,
    "park_experience_type": "Retail"
  },
  {
    "guest_id": 1,
    "visit_date": "2024-08-03",
    "amount_spent": 55,
    "park_experience_type": "Attraction"
  },
  {
    "guest_id": 1,
    "visit_date": "2024-08-15",
    "amount_spent": 45,
    "park_experience_type": "Dining"
  },
  {
    "guest_id": 2,
    "visit_date": "2024-08-05",
    "amount_spent": 22,
    "park_experience_type": "Retail"
  },
  {
    "guest_id": 2,
    "visit_date": "2024-08-20",
    "amount_spent": 38,
    "park_experience_type": "Entertainment"
  },
  {
    "guest_id": 7,
    "visit_date": "2024-08-10",
    "amount_spent": 15,
    "park_experience_type": "Character Meet"
  },
  {
    "guest_id": 3,
    "visit_date": "2024-08-25",
    "amount_spent": 28,
    "park_experience_type": "Retail"
  },
  {
    "guest_id": 3,
    "visit_date": "2024-08-27",
    "amount_spent": 32,
    "park_experience_type": "Dining"
  },
  {
    "guest_id": 1,
    "visit_date": "2024-09-02",
    "amount_spent": 65,
    "park_experience_type": "Attraction"
  },
  {
    "guest_id": 8,
    "visit_date": "2024-09-05",
    "amount_spent": 50,
    "park_experience_type": "Retail"
  },
  {
    "guest_id": 9,
    "visit_date": "2024-09-15",
    "amount_spent": 40,
    "park_experience_type": "Dining"
  },
  {
    "guest_id": 10,
    "visit_date": "2024-09-20",
    "amount_spent": 70,
    "park_experience_type": "Entertainment"
  },
  {
    "guest_id": 1,
    "visit_date": "2024-09-25",
    "amount_spent": 35,
    "park_experience_type": "Dining"
  },
  {
    "guest_id": 8,
    "visit_date": "2024-09-28",
    "amount_spent": 10,
    "park_experience_type": "Character Meet"
  }
]
fct_guest_spending = pd.DataFrame(fct_guest_spending_data)


# ## Question 1
# 
# What is the average spending per guest per visit for each park experience type during July 2024? Ensure that park experience types with no recorded transactions are shown with an average spending of 0.0. This analysis helps establish baseline spending differences essential for later segmentation.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_guest_spending
# Please print your final result or dataframe
fct_guest_spending['visit_date'] = pd.to_datetime(fct_guest_spending['visit_date'])
start_date = '2024-07-01'
end_date = '2024-07-31'

fct_guest_spending_july = fct_guest_spending[(fct_guest_spending['visit_date'] >= start_date) & (fct_guest_spending['visit_date'] <= end_date)]

total_spending_guest = fct_guest_spending_july.groupby(['guest_id', 'visit_date', 'park_experience_type'])['amount_spent'].sum().reset_index()

avg_spending_guest = total_spending_guest.groupby('park_experience_type')['amount_spent'].mean().reset_index()

all_experience_types = fct_guest_spending['park_experience_type'].drop_duplicates()

final_avg = pd.merge(all_experience_types, avg_spending_guest, on='park_experience_type', how='left').fillna(0.0)

final_avg


# ## Question 2
# 
# For guests who visited our parks more than once in August 2024, what is the difference in spending between their first and their last visit? This investigation, using sequential analysis, will reveal any shifts in guest spending behavior over multiple visits.

# In[ ]:


fct_guest_spending['visit_date'] = pd.to_datetime(fct_guest_spending['visit_date'])

august_visits = fct_guest_spending[(fct_guest_spending['visit_date'] >= '2024-08-01') & (fct_guest_spending['visit_date'] <= '2024-08-31')]

repeat_visitors = august_visits.groupby('guest_id').filter(lambda x: len(x) > 1)

repeat_visitors = repeat_visitors.sort_values(by=['guest_id', 'visit_date'])

first_visit = repeat_visitors.groupby('guest_id')['amount_spent'].first()

last_visit = repeat_visitors.groupby('guest_id')['amount_spent'].last()

spending_diff = last_visit - first_visit

spending_diff


# ## Question 3
# 
# In September 2024, how can guests be categorized into distinct spending segments such as Low, Medium, and High based on their total spending? Use the following thresholds for categorization: 
# -Low: Includes values from $0 up to, but not including, $50.
# -Medium: Includes values from $50 up to, but not including, $100.
# -High: Includes values from $100 and above. 
# Exclude guests who did not make any purchases in the period.

# In[ ]:


fct_guest_spending['visit_date'] = pd.to_datetime(fct_guest_spending['visit_date'])

september_visits = fct_guest_spending[(fct_guest_spending['visit_date'] >= '2024-09-01') & (fct_guest_spending['visit_date'] <= '2024-09-30')]

september_money = september_visits.groupby('guest_id')['amount_spent'].sum().reset_index()

paying_guests = september_money[september_money['amount_spent'] > 0]

bins = [0,50,100, float('inf')]
labels = ['Low', 'Medium', 'High']

paying_guests['spending_segment'] = pd.cut(paying_guests['amount_spent'], bins=bins, labels=labels, right=False)

paying_guests['spending_segment']


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
