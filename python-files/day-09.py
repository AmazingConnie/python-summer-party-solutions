#!/usr/bin/env python
# coding: utf-8

# # Day 9: Instagram Stories Daily User Creation Patterns

# You are a Product Analyst on the Instagram Stories team investigating story creation patterns. The team wants to understand the distribution of stories created by users daily. You will analyze user storytelling behavior to optimize engagement strategies.

# In[ ]:


import pandas as pd
import numpy as np

stories_data_data = [
  {
    "user_id": "user_001",
    "story_date": "2024-07-03",
    "story_count": 3
  },
  {
    "user_id": "user_001",
    "story_date": "2024-07-03",
    "story_count": 3
  },
  {
    "user_id": "user_001",
    "story_date": "2024-08-15",
    "story_count": 5
  },
  {
    "user_id": "user_001",
    "story_date": "2024-09-10",
    "story_count": 0
  },
  {
    "user_id": "user_001",
    "story_date": "2024-10-05",
    "story_count": 20
  },
  {
    "user_id": "user_001",
    "story_date": "07/15/2024",
    "story_count": 2
  },
  {
    "user_id": "user_002",
    "story_date": "2024-07-03",
    "story_count": 4
  },
  {
    "user_id": " user_002",
    "story_date": "2024-07-04",
    "story_count": 3
  },
  {
    "user_id": "user_002",
    "story_date": null,
    "story_count": 6
  },
  {
    "user_id": "user_002",
    "story_date": "2024-12-25",
    "story_count": 1
  },
  {
    "user_id": "user_002",
    "story_date": "2025-01-15",
    "story_count": 7
  },
  {
    "user_id": "user_002",
    "story_date": "2025-06-29",
    "story_count": 10
  },
  {
    "user_id": "user_003",
    "story_date": "2024-07-10",
    "story_count": 2
  },
  {
    "user_id": "user_003",
    "story_date": "2024-08-20",
    "story_count": 8
  },
  {
    "user_id": "user_003",
    "story_date": "2024-08-20",
    "story_count": 8
  },
  {
    "user_id": "user_003",
    "story_date": "2025-03-11",
    "story_count": 5
  },
  {
    "user_id": null,
    "story_date": "2025-03-12",
    "story_count": 3
  },
  {
    "user_id": "USER_003",
    "story_date": "2025-04-01",
    "story_count": 4
  },
  {
    "user_id": "user_004",
    "story_date": "2024-07-15",
    "story_count": 6
  },
  {
    "user_id": "user_004",
    "story_date": "2024-09-30",
    "story_count": 7
  },
  {
    "user_id": "user_004",
    "story_date": "2024/10/10",
    "story_count": 4
  },
  {
    "user_id": "user_004",
    "story_date": "2024-11-11",
    "story_count": 3
  },
  {
    "user_id": "user_004",
    "story_date": "2025-02-28",
    "story_count": 12
  },
  {
    "user_id": "user_004",
    "story_date": "2025-03-01",
    "story_count": 0
  },
  {
    "user_id": "user_005",
    "story_date": "2024-08-01",
    "story_count": 1
  },
  {
    "user_id": "user_005",
    "story_date": "2024-08-02",
    "story_count": 2
  },
  {
    "user_id": "user_005",
    "story_date": "2024-08-03",
    "story_count": 3
  },
  {
    "user_id": "user_005",
    "story_date": "2024-08-04",
    "story_count": 4
  },
  {
    "user_id": "user_005",
    "story_date": "2024-08-05",
    "story_count": null
  },
  {
    "user_id": "user_005",
    "story_date": "2024-08-06",
    "story_count": 5
  },
  {
    "user_id": "user_006",
    "story_date": "2024-09-01",
    "story_count": 9
  },
  {
    "user_id": "user_006",
    "story_date": "2024-09-02",
    "story_count": 10
  },
  {
    "user_id": "user_006",
    "story_date": "2024-09-03",
    "story_count": 9
  },
  {
    "user_id": "user_006",
    "story_date": "2024-09-04",
    "story_count": 50
  },
  {
    "user_id": "user_006",
    "story_date": "2024-09-05",
    "story_count": 8
  },
  {
    "user_id": "user_006",
    "story_date": null,
    "story_count": 7
  },
  {
    "user_id": "user_007",
    "story_date": "2024-10-10",
    "story_count": 4
  },
  {
    "user_id": "user_007",
    "story_date": "2024-10-11",
    "story_count": 4
  },
  {
    "user_id": "user_007",
    "story_date": "2024-10-12",
    "story_count": 4
  },
  {
    "user_id": "user_007",
    "story_date": "2024-10-13",
    "story_count": 3
  },
  {
    "user_id": "user_007",
    "story_date": "2024-10-14",
    "story_count": 2
  },
  {
    "user_id": "user_007",
    "story_date": "2024-10-15",
    "story_count": 1
  },
  {
    "user_id": "user_008",
    "story_date": "2025-01-01",
    "story_count": 11
  },
  {
    "user_id": "user_008",
    "story_date": "2025-01-02",
    "story_count": 12
  },
  {
    "user_id": "user_008",
    "story_date": "2025-01-03",
    "story_count": 13
  },
  {
    "user_id": "user_008",
    "story_date": "2025-01-04",
    "story_count": 14
  },
  {
    "user_id": "user_008",
    "story_date": "2025-01-05",
    "story_count": 15
  },
  {
    "user_id": "user_008",
    "story_date": "2025-01-06",
    "story_count": 0
  },
  {
    "user_id": "user_009",
    "story_date": "2024-12-01",
    "story_count": 1
  },
  {
    "user_id": "user_009",
    "story_date": "2024-12-02",
    "story_count": 2
  },
  {
    "user_id": "user_009",
    "story_date": "2024-12-03",
    "story_count": 3
  },
  {
    "user_id": "user_009",
    "story_date": "2024-12-04",
    "story_count": 4
  },
  {
    "user_id": "user_009",
    "story_date": "2024-12-05",
    "story_count": 5
  },
  {
    "user_id": "user_009",
    "story_date": "invalid_date",
    "story_count": 6
  },
  {
    "user_id": "user_010",
    "story_date": "2025-03-15",
    "story_count": 7
  },
  {
    "user_id": "user_010",
    "story_date": "2025-03-16",
    "story_count": 8
  },
  {
    "user_id": "user_010",
    "story_date": "2025-03-17",
    "story_count": 9
  },
  {
    "user_id": "user_010",
    "story_date": "2025-03-18",
    "story_count": 10
  },
  {
    "user_id": "user_010",
    "story_date": "2025-03-19",
    "story_count": 11
  },
  {
    "user_id": "user_010",
    "story_date": "2025-03-20",
    "story_count": 12
  }
]
stories_data = pd.DataFrame(stories_data_data)


# ## Question 1
# 
# Take a look at the data in the story_date column. Correct any data type inconsistencies in that column.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: stories_data
# Please print your final result or dataframe

stories_data['story_date'] = pd.to_datetime(stories_data['story_date'], format='%Y-%m-%d')

clean_stories_data = stories_data[stories_data['story_date'].notna()]

clean_stories_data


# ## Question 2
# 
# Calculate the 25th, 50th, and 75th percentiles of the number of stories created per user per day.

# In[ ]:


user_stories = stories_data.groupby(['user_id', 'story_date'])['story_count'].sum()

user_stories_25 = user_stories.quantile(0.25)

user_stories_50 = user_stories.quantile(0.5)

user_stories_75 = user_stories.quantile(0.75)

print(user_stories_25, user_stories_50, user_stories_75)


# ## Question 3
# 
# What percentage of users have had at least one day, where they posted more than 10 stories on that day?

# In[ ]:


stories_data = stories_data.drop_duplicates()
stories_data['user_id'] = stories_data['user_id'].str.lower()
stories_data['user_id'] = stories_data['user_id'].str.strip()

stories_data_10 = stories_data[stories_data['story_count'] > 10]

stories_data_10_users = stories_data_10['user_id'].nunique()

total_users = stories_data['user_id'].nunique()

percentage = (stories_data_10_users / total_users) * 100

percentage


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
