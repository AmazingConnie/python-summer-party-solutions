#!/usr/bin/env python
# coding: utf-8

# # Day 4: Search Results Page: User Interaction Patterns

# You are a Product Analyst on the Google Search team investigating user engagement with search result pages. The team wants to understand how different numbers of search results impact user interaction time. Your analysis will help optimize the current search results presentation strategy.

# In[ ]:


import pandas as pd
import numpy as np

user_engagement_data_data = [
  {
    "user_id": "user_1",
    "interaction_date": "2024-07-05",
    "interaction_time": 35.5,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_2",
    "interaction_date": "2024-07-10",
    "interaction_time": 22.3,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_1",
    "interaction_date": "2024-07-05",
    "interaction_time": 35.5,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_3",
    "interaction_date": "2024-08-01",
    "interaction_time": 48,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_4",
    "interaction_date": "2024-08-15",
    "interaction_time": null,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_5",
    "interaction_date": "2024-09-05",
    "interaction_time": 60.2,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_6",
    "interaction_date": "2024-10-10",
    "interaction_time": 12,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_7",
    "interaction_date": "2024-11-20",
    "interaction_time": 80,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_8",
    "interaction_date": "2024-12-31",
    "interaction_time": 55,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_9",
    "interaction_date": "2025-01-15",
    "interaction_time": 75.5,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_10",
    "interaction_date": "2025-02-20",
    "interaction_time": 30,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_2",
    "interaction_date": "2024-07-10",
    "interaction_time": 22.3,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_11",
    "interaction_date": "2025-03-01",
    "interaction_time": 92.5,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_12",
    "interaction_date": "2025-03-05",
    "interaction_time": 15,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_13",
    "interaction_date": "2025-03-10",
    "interaction_time": 45.3,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_14",
    "interaction_date": "2025-03-15",
    "interaction_time": 5,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_15",
    "interaction_date": "2025-03-20",
    "interaction_time": 68,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_16",
    "interaction_date": "2025-03-25",
    "interaction_time": 110,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_17",
    "interaction_date": "2025-04-01",
    "interaction_time": 29.9,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_18",
    "interaction_date": "2025-04-05",
    "interaction_time": 150,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_19",
    "interaction_date": "2025-04-10",
    "interaction_time": 33.3,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_20",
    "interaction_date": "2025-04-15",
    "interaction_time": 25,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_21",
    "interaction_date": "2025-04-20",
    "interaction_time": 40,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_22",
    "interaction_date": "2025-04-25",
    "interaction_time": 85.5,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_23",
    "interaction_date": "2025-04-30",
    "interaction_time": null,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_24",
    "interaction_date": "2025-05-05",
    "interaction_time": 55.5,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_25",
    "interaction_date": "2025-05-10",
    "interaction_time": 65,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_26",
    "interaction_date": "2025-05-15",
    "interaction_time": 70,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_27",
    "interaction_date": "2025-05-20",
    "interaction_time": 95,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_28",
    "interaction_date": "2025-05-25",
    "interaction_time": 50,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_29",
    "interaction_date": "2025-06-01",
    "interaction_time": 88,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_30",
    "interaction_date": "2025-06-05",
    "interaction_time": 42,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_31",
    "interaction_date": "2025-06-10",
    "interaction_time": 37,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_32",
    "interaction_date": "2025-06-15",
    "interaction_time": 82,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_33",
    "interaction_date": "2025-06-20",
    "interaction_time": 20,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_34",
    "interaction_date": "2025-06-25",
    "interaction_time": 90,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_35",
    "interaction_date": "2025-06-29",
    "interaction_time": 77,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_36",
    "interaction_date": "2025-06-30",
    "interaction_time": 66.6,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_37",
    "interaction_date": "2024-07-15",
    "interaction_time": 100,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_38",
    "interaction_date": "2024-07-20",
    "interaction_time": 110.5,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_39",
    "interaction_date": "2024-08-05",
    "interaction_time": 35,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_40",
    "interaction_date": "2024-08-10",
    "interaction_time": 59.9,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_41",
    "interaction_date": "2024-08-15",
    "interaction_time": 47.3,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_42",
    "interaction_date": "2024-08-20",
    "interaction_time": null,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_43",
    "interaction_date": "2024-09-01",
    "interaction_time": 68.5,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_44",
    "interaction_date": "2024-09-05",
    "interaction_time": 72.7,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_45",
    "interaction_date": "2024-09-10",
    "interaction_time": 55.5,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_46",
    "interaction_date": "2024-09-15",
    "interaction_time": 62,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_47",
    "interaction_date": "2024-09-20",
    "interaction_time": 40,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_48",
    "interaction_date": "2024-09-25",
    "interaction_time": 85,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_49",
    "interaction_date": "2024-10-01",
    "interaction_time": 95,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_50",
    "interaction_date": "2024-10-05",
    "interaction_time": 33.3,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_51",
    "interaction_date": "2024-10-10",
    "interaction_time": 44.4,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_52",
    "interaction_date": "2024-10-15",
    "interaction_time": 88.8,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_53",
    "interaction_date": "2024-10-20",
    "interaction_time": 76.5,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_54",
    "interaction_date": "2024-10-25",
    "interaction_time": 90,
    "search_results_displayed": 10
  },
  {
    "user_id": "user_55",
    "interaction_date": "2024-10-30",
    "interaction_time": null,
    "search_results_displayed": 5
  },
  {
    "user_id": "user_56",
    "interaction_date": "2024-11-01",
    "interaction_time": 101,
    "search_results_displayed": 15
  },
  {
    "user_id": "user_57",
    "interaction_date": "2024-11-05",
    "interaction_time": 59,
    "search_results_displayed": 20
  },
  {
    "user_id": "user_58",
    "interaction_date": "2024-11-10",
    "interaction_time": 66,
    "search_results_displayed": 10
  }
]
user_engagement_data = pd.DataFrame(user_engagement_data_data)


# ## Question 1
# 
# Identify and remove any duplicate entries in the dataset to ensure data quality. How many duplicates were found and removed?

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: user_engagement_data
# Please print your final result or dataframe
# initial_rows = len(user_engagement_data)

which_duplicates = user_engagement_data.duplicated()

count_duplicates = which_duplicates.value_counts()

count_duplicates_true = count_duplicates.get(True, 0)

clean_data = user_engagement_data.drop_duplicates()

# final_rows = len(user_engagement_data)

count_duplicates_true


# ## Question 2
# 
# After dropping duplicates, aggregate the data to find the average user interaction time for each number of search results displayed per page. What are the average interaction times?

# In[ ]:


user_engagement_data = user_engagement_data.drop_duplicates()

user_engagement_data = user_engagement_data[user_engagement_data['interaction_time'].notna()]

average_times = user_engagement_data.groupby('search_results_displayed')['interaction_time'].mean()

average_times


# ## Question 3
# 
# Sort the aggregated results from Q2 to determine which number of search results per page has the highest average user interaction time. What is the optimal number of search results per page?

# In[ ]:


user_engagement_data = user_engagement_data.drop_duplicates()

user_engagement_data = user_engagement_data[user_engagement_data['interaction_time'].notna()]

average_times = user_engagement_data.groupby('search_results_displayed')['interaction_time'].mean()

average_times = average_times.sort_values(ascending=False)

max_time = average_times.idxmax()

max_time


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
