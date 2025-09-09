#!/usr/bin/env python
# coding: utf-8

# # Day 1: WhatsApp Group Size Engagement Analysis

# You are a Product Analyst on the WhatsApp team investigating group messaging dynamics. Your team wants to understand how large groups are being used and their messaging patterns. You'll leverage data to uncover insights about group participation and communication behaviors.

# In[ ]:


import pandas as pd
import numpy as np

dim_groups_data = [
  {
    "group_id": 1,
    "created_date": "2024-10-01",
    "total_messages": 100,
    "participant_count": 25
  },
  {
    "group_id": 2,
    "created_date": "2024-10-10",
    "total_messages": 200,
    "participant_count": 55
  },
  {
    "group_id": 3,
    "created_date": "2024-11-05",
    "total_messages": 150,
    "participant_count": 40
  },
  {
    "group_id": 4,
    "created_date": "2024-10-15",
    "total_messages": 500,
    "participant_count": 100
  },
  {
    "group_id": 5,
    "created_date": "2024-12-01",
    "total_messages": 120,
    "participant_count": 35
  },
  {
    "group_id": 6,
    "created_date": "2024-10-20",
    "total_messages": 300,
    "participant_count": 50
  },
  {
    "group_id": 7,
    "created_date": "2024-10-25",
    "total_messages": 400,
    "participant_count": 60
  },
  {
    "group_id": 8,
    "created_date": "2024-11-10",
    "total_messages": 220,
    "participant_count": 45
  },
  {
    "group_id": 9,
    "created_date": "2024-10-30",
    "total_messages": 450,
    "participant_count": 80
  },
  {
    "group_id": 10,
    "created_date": "2024-12-15",
    "total_messages": 80,
    "participant_count": 15
  },
  {
    "group_id": 11,
    "created_date": "2024-10-05",
    "total_messages": 600,
    "participant_count": 90
  },
  {
    "group_id": 12,
    "created_date": "2024-10-12",
    "total_messages": 50,
    "participant_count": 10
  }
]
dim_groups = pd.DataFrame(dim_groups_data)


# ## Question 1
# 
# What is the maximum number of participants among WhatsApp groups that were created in October 2024? This metric will help us understand the largest group size available.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: dim_groups
# Please print your final result or dataframe

dim_groups["created_date"] = pd.to_datetime(dim_groups["created_date"])

dim_groups = dim_groups[(dim_groups["created_date"] >= '2024-10-01') &  (dim_groups["created_date"] <= '2024-10-31')]

dim_groups_max = dim_groups["participant_count"].max()

dim_groups_max


# ## Question 2
# 
# What is the average number of participants in WhatsApp groups that were created in October 2024? This number will indicate the typical group size and inform our group messaging feature considerations.

# In[ ]:


dim_groups['created_date'] = pd.to_datetime(dim_groups['created_date'])

dim_groups = dim_groups[(dim_groups['created_date'] >= '2024-10-01') & (dim_groups['created_date'] <= '2024-10-31')]

dim_groups_avg = dim_groups['participant_count'].mean()

dim_groups_avg


# ## Question 3
# 
# For WhatsApp groups with more than 50 participants that were created in October 2024, what is the average number of messages sent? This insight will help assess engagement in larger groups and support recommendations for group messaging features.

# In[ ]:


dim_groups['created_date'] = pd.to_datetime(dim_groups['created_date'])

dim_groups = dim_groups[(dim_groups['created_date'] >= '2024-10-01') & (dim_groups['created_date'] <= '2024-10-31')]

dim_groups = dim_groups[dim_groups['participant_count'] > 50]

dim_groups_mes_avg = dim_groups['total_messages'].mean()

dim_groups_mes_avg


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
